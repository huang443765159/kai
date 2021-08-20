#include "register.h"
#include <stdio.h>


// 回调函数 被调用的函数
void callback_btn_ena(u_int8_t id, bool ena)
{
  Serial.println(id);
  Serial.println(ena);
}

void main()
{
    test.register_callback_conn(callback_btn_ena);  //注册后调用
}