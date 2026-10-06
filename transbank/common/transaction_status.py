from enum import Enum, unique


@unique
class TransactionStatus(str, Enum):
    INITIALIZED = "INITIALIZED"
    AUTHORIZED = "AUTHORIZED"
    REVERSED = "REVERSED"
    FAILED = "FAILED"
    NULLIFIED = "NULLIFIED"
    PARTIALLY_NULLIFIED = "PARTIALLY_NULLIFIED"
    CAPTURED = "CAPTURED"

    def __str__(self):
        return self.value
