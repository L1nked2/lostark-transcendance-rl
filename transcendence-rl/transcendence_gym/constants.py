from enum import IntEnum, StrEnum, EnumMeta

DEFAULT_DISTORT_SIDE_EFFECT_BLOCK_NUM = 3
MAX_BOARD_SIZE = 8
BASE_CARD_TYPE_SIZE = 10
MAX_CARD_STRENGTH = 2

HAND_SIZE = 2
QUEUE_SIZE = 3

class CardType(IntEnum):
    LIGHTNING = 0
    RISING_FIRE = 1
    SHOCKWAVE = 2
    TSUNAMI = 3
    MASSIVE_EXPLOSION = 4
    STORM = 5
    THUNDERBOLT = 6
    EARTHQUAKE = 7
    PURIFICATION = 8
    TORNADO = 9
    EXPULSION = 30
    RESONANCE_OF_WORLD_TREE = 31

class BaseBlockType(IntEnum):
    EMPTY = 0
    DESTROYED = 1
    DISTORTED = 2
    NORMAL = 3  # Normal block that can be destroyed

class SpecialBlockType(IntEnum):
    ENHANCE = 0
    DUPLICATE = 1
    MYSTIC = 2
    ADDITION = 3
    REARRANGE = 4
    BLESS = 5

class CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        if isinstance(name, str):
            name = name.upper()
        return super().__getitem__(name)

class DistortModeType(StrEnum, metaclass=CaseInsensitiveEnumMeta):
    DEFAULT = "default"
    BREAK = "break"
    IGNORE = "ignore"

class DistortApplicapableEffects(StrEnum, metaclass=CaseInsensitiveEnumMeta):
    PURIFICATION = "applyPurification"
    RESONANCE_OF_WORLD_TREE = "applyResonanceOfWorldTree"



