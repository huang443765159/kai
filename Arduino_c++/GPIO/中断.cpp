// 用2号引脚作为中断触发引脚

const byte interruptPin = 2;
volatile byte state = LOW;

void
setup()
{
    Serial.begin(115200);
    pinMode(interruptPin, INPUT);

    // 将中断触发引脚（2号引脚）设置为INPUT_PULLUP（输入上拉）模式
    pinMode(interruptPin, INPUT_PULLUP);
    // 设置中断触发程序
    attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
}

void loop()
{
  digitalRead(interruptPin);
}

// 中断服务程序
void blink()
{
    state = !state;
    Serial.println(state);
}