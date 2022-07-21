from XYZUtil4.customclass.Signal import Signal

from .Singleton import singleton


@singleton
class Signals:

    pump_ena = Signal(int, bool)  # bot_id, ena
    channel_switch = Signal(int, int, bool)  # bot_id, chem_id, is_open
    cur_level = Signal(int, int, int)  # bot_id, chem_id, level
    cur_flow = Signal(int, int, float)  # bot_id, chem_id, flow
    cur_pressure = Signal(int, int, int)  # bot_id, chem_id, pressure
    temp_humi_data = Signal(int, float, float)  # bot_id, temp, humi
