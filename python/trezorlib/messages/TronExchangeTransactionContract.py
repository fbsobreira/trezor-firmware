# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TronExchangeTransactionContract(p.MessageType):

    def __init__(
        self,
        exchange_id: int = None,
        token_id: bytes = None,
        quant: int = None,
        expected: int = None,
    ) -> None:
        self.exchange_id = exchange_id
        self.token_id = token_id
        self.quant = quant
        self.expected = expected

    @classmethod
    def get_fields(cls):
        return {
            2: ('exchange_id', p.UVarintType, 0),
            3: ('token_id', p.BytesType, 0),
            4: ('quant', p.UVarintType, 0),
            5: ('expected', p.UVarintType, 0),
        }
