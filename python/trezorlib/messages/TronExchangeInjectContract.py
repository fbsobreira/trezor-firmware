# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TronExchangeInjectContract(p.MessageType):

    def __init__(
        self,
        exchange_id: int = None,
        token_id: str = None,
        quant: int = None,
        first_asset_id: str = None,
        first_asset_name: str = None,
        first_asset_decimals: int = None,
        second_asset_id: str = None,
        second_asset_name: str = None,
        second_asset_decimals: int = None,
        exachange_signature: str = None,
    ) -> None:
        self.exchange_id = exchange_id
        self.token_id = token_id
        self.quant = quant
        self.first_asset_id = first_asset_id
        self.first_asset_name = first_asset_name
        self.first_asset_decimals = first_asset_decimals
        self.second_asset_id = second_asset_id
        self.second_asset_name = second_asset_name
        self.second_asset_decimals = second_asset_decimals
        self.exachange_signature = exachange_signature

    @classmethod
    def get_fields(cls):
        return {
            1: ('exchange_id', p.UVarintType, 0),
            2: ('token_id', p.UnicodeType, 0),
            3: ('quant', p.UVarintType, 0),
            4: ('first_asset_id', p.UnicodeType, 0),
            5: ('first_asset_name', p.UnicodeType, 0),
            6: ('first_asset_decimals', p.UVarintType, 0),
            7: ('second_asset_id', p.UnicodeType, 0),
            8: ('second_asset_name', p.UnicodeType, 0),
            9: ('second_asset_decimals', p.UVarintType, 0),
            10: ('exachange_signature', p.UnicodeType, 0),
        }
