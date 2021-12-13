import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal

BAUD = 9600
LIQUID_WATER_HIGH = 0
LIQUID_CH_A = 1
LIQUID_CH_B = 2
LIQUID_CH_WHL = 3
LIQUID_CH_WAX = 4


class _OneSensor(QObject):

    def __init__(self, pin_rx, pin_tx):
        super().__init__()
        self._pin_rx = pin_rx
        self._err = False
        try:
            # GPIO
            import pigpio
            self._pi = pigpio.pi()
            self._pi.set_mode(pin_rx, pigpio.INPUT)
            self._pi.set_mode(pin_tx, pigpio.OUTPUT)
            pigpio.exceptions = False
            self._pi.bb_serial_read_close(pin_rx)
            pigpio.exceptions = True
            self._pi.bb_serial_read_open(pin_rx, BAUD, 8)
        except ImportError as err:
            # print(err)
            self._err = True

    def get_level(self):
        sensor_data = bytes()
        if not self._err:
            _, data = self._pi.bb_serial_read(self._pin_rx)
            if data:
                for i in range(4):
                    sensor_data += data
                if (sensor_data[0] + sensor_data[1] + sensor_data[2]) & 0x00ff == sensor_data[3]:
                    sensor_data = sensor_data[1] * 256 + sensor_data[2]
                    return sensor_data


class LevelSensors(QObject):

    sign_sensor_level = pyqtSignal(int, int)  # liquid_id, sensor_level(mm)

    def __init__(self, pins_rx=(15, 24, 8, 12, 20), pins_tx=(14, 23, 25, 7, 16), sampling_frequency=1):
        super().__init__()
        # SENSORS
        self._sensors = dict()
        for sensor_id, pin_rx in enumerate(pins_rx):
            self._sensors[sensor_id] = _OneSensor(pin_rx=pin_rx, pin_tx=pins_tx[sensor_id])
        # THREAD
        self._sampling_frequency = sampling_frequency
        self._thread = threading.Thread(target=self._working)
        self._thread_switch = True
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while self._thread_switch:
            for sensor_id in self._sensors.keys():
                one_sensor_level = self._sensors[sensor_id].get_level()
                if one_sensor_level is not None:
                    self.sign_sensor_level.emit(sensor_id, one_sensor_level)
            time.sleep(self._sampling_frequency)

    def exit(self):
        self._thread_switch = False
