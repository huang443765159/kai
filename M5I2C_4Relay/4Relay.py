

class OneChannel(object):

    def __init__(self, hub_id: int, channel_id: int, dev_reg, dev_address, hub_address, i2c_bus):
        self._hub_id = hub_id
        self._channel_id = channel_id
        self._dev_reg = dev_reg
        self._dev_address = dev_address
        self._hub_address = hub_address
        self._bus = i2c_bus
        # ATTR
        self._state = False

    def _choose_hub_channel(self):
        self._bus.write_byte(self._hub_address, 1 << self._hub_id)

    def _read_byte_data(self):
        self._bus.write_byte(self._dev_address, self._dev_reg)
        data = self._bus.read_byte(self._dev_address)
        return data

    def _write_byte_data(self, data: int):
        self._bus.write_byte_data(self._dev_address, self._dev_reg, data)

    def set_power(self, switch: bool):
        if self._bus:
            self._choose_hub_channel()
            if self._state != switch:
                self._state = switch
                data_from_dev = self._read_byte_data()
                if switch:
                    data_from_dev |= (0x01 << self._channel_id)
                else:
                    data_from_dev &= ~(0x01 << self._channel_id)
                self._write_byte_data(data=data_from_dev)
