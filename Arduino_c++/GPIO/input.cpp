#include <Arduino.h>

int inputPin = 14;
int outputPin = 15;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);  // debug
  pinMode(inputPin, INPUT);  // 设置输入pin
  pinMode(outputPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.printf("Hello world\n");
  Serial.printf("%d", digitalRead(inputPin));
  delay(1000);
  digitalWrite(outputPin, true);  // 给输出pin设置高低电平
}
