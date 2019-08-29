from enum import Enum, unique


@unique
class IntegrationType(Enum):
    LIVE = 1
    TEST = 2
    MOCK = 3
