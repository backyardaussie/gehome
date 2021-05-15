import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdMachineState, MachineState, MACHINE_STATE_MAP

_LOGGER = logging.getLogger(__name__)

class MachineStateConverter(ErdReadOnlyConverter[MachineState]):
    def erd_decode(self, value: str) -> MachineState:
        try:
            om = ErdMachineState(erd_decode_int(value))
            return MACHINE_STATE_MAP[om].value
        except (KeyError, ValueError):
            return ErdMachineState.NA