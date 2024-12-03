from .laundry_enums import ErdWashTempOption
from .washtemp_option import WashTempOption

WASHTEMP_OPTION_MAP = {
    ErdWashTempOption.COLD: WashTempOption.COLD,
    ErdWashTempOption.THIRTY: WashTempOption.THIRTY,
    ErdWashTempOption.FOURTY: WashTempOption.FOURTY,
    ErdWashTempOption.SIXTY: WashTempOption.SIXTY,
    ErdWashTempOption.NINETY: WashTempOption.NINETY
}
