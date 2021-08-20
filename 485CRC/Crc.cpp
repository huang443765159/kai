uint8_t buff[6] = {0x02, 0x03, 0x00, 0x01, 0x00, 0x01};
//uint8_t buff1[6] = {0x01, 0x03, 0x00, 0x01, 0x00, 0x01};
uint8_t crc_buff[2];
uint8_t recv_buff[7];

void get_crc_data(uint8_t *buff, uint8_t len)
{
  uint16_t crc_init = 0XFFFF;
  uint8_t temp;
  uint8_t i = 0, j = 0;
  for (i = 0; i < len; i++) {
    temp = *buff & 0x00FF;
    buff++;
    crc_init ^= temp;
    for (j = 0; j < 8; j++) {
      if (crc_init & 0x0001) {
        crc_init >>= 1;
        crc_init ^= 0xA001;
      } else {
        crc_init >>= 1;
      }
    }
  }
  crc_buff[0] = crc_init & 0xff;  //CRC_HIGH
  crc_buff[1] = crc_init >> 8;  //CRC_LOW
}