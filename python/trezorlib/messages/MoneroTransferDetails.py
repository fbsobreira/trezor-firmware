# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class MoneroTransferDetails(p.MessageType):

    def __init__(
        self,
        out_key: bytes = None,
        tx_pub_key: bytes = None,
        additional_tx_pub_keys: List[bytes] = None,
        internal_output_index: int = None,
    ) -> None:
        self.out_key = out_key
        self.tx_pub_key = tx_pub_key
        self.additional_tx_pub_keys = additional_tx_pub_keys if additional_tx_pub_keys is not None else []
        self.internal_output_index = internal_output_index

    @classmethod
    def get_fields(cls):
        return {
            1: ('out_key', p.BytesType, 0),
            2: ('tx_pub_key', p.BytesType, 0),
            3: ('additional_tx_pub_keys', p.BytesType, p.FLAG_REPEATED),
            4: ('internal_output_index', p.UVarintType, 0),
        }
