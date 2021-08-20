byte crc_buff[2];


byte* get_crc_data(uint8_t *buff, uint32_t len)
{
  uint16_t wcrc = 0XFFFF;//16位crc寄存器预置
  uint8_t temp;
  uint32_t i = 0, j = 0;//计数
  for (i = 0; i < len; i++)//循环计算每个数据
  {
    temp = *buff & 0X00FF;//将八位数据与crc寄存器亦或
    buff++;//指针地址增加，指向下个数据
    wcrc ^= temp;//将数据存入crc寄存器
    for (j = 0; j < 8; j++)//循环计算数据的
    {
      if (wcrc & 0X0001)//判断右移出的是不是1，如果是1则与多项式进行异或。
      {
        wcrc >>= 1;//先将数据右移一位
        wcrc ^= 0XA001;//与上面的多项式进行异或
      }
      else//如果不是1，则直接移出
      {
        wcrc >>= 1;//直接移出
      }
    }
  }
  uint8_t CRC_L;//定义数组
  uint8_t CRC_H;
  CRC_L = wcrc & 0xff;//crc的低八位
  CRC_H = wcrc >> 8;//crc的高八位
//  Serial.println(CRC_L, HEX);
//  Serial.println(CRC_H, HEX);
  crc_buff[0] = CRC_L;
  crc_buff[1] = CRC_H;
  return crc_buff;
//  return ((CRC_L << 8) | CRC_H);
}


void setup() {
  Serial.begin(115200);
  // put your setup code here, to run once:

}

void loop() {
  uint8_t buffer[5] = {0x01, 0x03, 0x02, 0x00, 0xd2};
  auto data = get_crc_data(buffer, 5);
  Serial.println(data[0], HEX);
  delay(1000);
  // put your main code here, to run repeatedly:
}