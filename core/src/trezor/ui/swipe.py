from micropython import const

from trezor import io, loop, ui

SWIPE_UP = const(0x01)
SWIPE_DOWN = const(0x02)
SWIPE_LEFT = const(0x04)
SWIPE_RIGHT = const(0x08)
SWIPE_VERTICAL = const(SWIPE_UP | SWIPE_DOWN)
SWIPE_HORIZONTAL = const(SWIPE_LEFT | SWIPE_RIGHT)
SWIPE_ALL = const(SWIPE_VERTICAL | SWIPE_HORIZONTAL)

_SWIPE_DISTANCE = const(120)
_SWIPE_TRESHOLD = const(30)


class Swipe(ui.Control):
    def __init__(self, directions=SWIPE_ALL, area=None):
        if area is None:
            area = (0, 0, ui.WIDTH, ui.HEIGHT)
        self.area = area
        self.directions = directions
        self.start_x = None
        self.start_y = None
        self.light_origin = None
        self.light_target = ui.BACKLIGHT_NONE

    def on_touch_start(self, x, y):
        if ui.in_area(self.area, x, y):
            self.start_x = x
            self.start_y = y
            self.light_origin = ui.BACKLIGHT_NORMAL

    def on_touch_move(self, x, y):
        if self.start_x is None:
            return  # not started in our area

        dirs = self.directions
        pdx = x - self.start_x
        pdy = y - self.start_y
        pdxa = abs(pdx)
        pdya = abs(pdy)
        if pdxa > pdya and dirs & SWIPE_HORIZONTAL:
            # horizontal direction
            if (pdx > 0 and dirs & SWIPE_RIGHT) or (pdx < 0 and dirs & SWIPE_LEFT):
                ui.display.backlight(
                    ui.lerpi(
                        self.light_origin,
                        self.light_target,
                        min(pdxa / _SWIPE_DISTANCE, 1),
                    )
                )
        elif pdxa < pdya and dirs & SWIPE_VERTICAL:
            # vertical direction
            if (pdy > 0 and dirs & SWIPE_DOWN) or (pdy < 0 and dirs & SWIPE_UP):
                ui.display.backlight(
                    ui.lerpi(
                        self.light_origin,
                        self.light_target,
                        min(pdya / _SWIPE_DISTANCE, 1),
                    )
                )

    def on_touch_end(self, x, y):
        if self.start_x is None:
            return  # not started in our area

        dirs = self.directions
        pdx = x - self.start_x
        pdy = y - self.start_y
        pdxa = abs(pdx)
        pdya = abs(pdy)
        if pdxa > pdya and dirs & SWIPE_HORIZONTAL:
            # horizontal direction
            ratio = min(pdxa / _SWIPE_DISTANCE, 1)
            if ratio * 100 >= _SWIPE_TRESHOLD:
                if pdx > 0 and dirs & SWIPE_RIGHT:
                    self.on_swipe(SWIPE_RIGHT)
                    return
                elif pdx < 0 and dirs & SWIPE_LEFT:
                    self.on_swipe(SWIPE_LEFT)
                    return
        elif pdxa < pdya and dirs & SWIPE_VERTICAL:
            # vertical direction
            ratio = min(pdya / _SWIPE_DISTANCE, 1)
            if ratio * 100 >= _SWIPE_TRESHOLD:
                if pdy > 0 and dirs & SWIPE_DOWN:
                    self.on_swipe(SWIPE_DOWN)
                    return
                elif pdy < 0 and dirs & SWIPE_UP:
                    self.on_swipe(SWIPE_UP)
                    return

        # no swipe detected, reset the state
        ui.display.backlight(self.light_origin)
        self.start_x = None
        self.start_y = None

    def on_swipe(self, swipe):
        raise ui.Result(swipe)

    def __iter__(self):
        try:
            touch = loop.wait(io.TOUCH)
            while True:
                event, x, y = yield touch
                self.dispatch(event, x, y)
        except ui.Result as result:
            return result.value
