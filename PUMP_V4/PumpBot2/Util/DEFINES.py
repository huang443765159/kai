class CHANNEL:

    WATER = 0
    CH_A = 1
    CH_B = 2
    CH_WHL = 3
    CH_WAX = 4


class NETWORK:

    PUMP_ENA = b'\x20'


class STATE:  # PUMP_CHANNEL_STATE

    ENA_OFF = 0
    ENA_ON = 1
    SHOOTING = 2
