# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeTronResourceCode = Literal[0, 1]
    except ImportError:
        pass


class TronUnfreezeAssetContract(p.MessageType):

    def __init__(
        self,
        resource: EnumTypeTronResourceCode = None,
        receiver_address: str = None,
    ) -> None:
        self.resource = resource
        self.receiver_address = receiver_address

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('resource', p.EnumType("TronResourceCode", (0, 1)), 0),
            2: ('receiver_address', p.UnicodeType, 0),
        }
