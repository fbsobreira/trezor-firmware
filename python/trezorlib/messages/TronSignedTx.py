# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TronSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 803

    def __init__(
        self,
        signature: bytes = None,
        serialized_tx: bytes = None,
    ) -> None:
        self.signature = signature
        self.serialized_tx = serialized_tx

    @classmethod
    def get_fields(cls):
        return {
            1: ('signature', p.BytesType, 0),
            2: ('serialized_tx', p.BytesType, 0),
        }
