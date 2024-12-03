import enum

@enum.unique
class WashTempOption(enum.Enum):
    DASH = "---"
    COLD = "Cold"
    THIRTY = "30"
    FOURTY = "40"
    SIXTY = "60"
    NINETY = "90"
    
    def stringify(self, **kwargs):
        return self.value
