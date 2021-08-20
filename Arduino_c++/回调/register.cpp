#include "register.h"


Test::test()  //类的构造, 可传参数进去
{
   //CALLBACK_INIT
  _conn_cb = nullptr;
  _ena = false;
}

void Test::update()
{
    for (int i=0; i<5; i++)
    {
        if (i%2==0){
        _ena = true;} else {_ena = false;}
        // 如果有调用就赋值
        if(_conn_cb != nullptr) {
        _conn_cb(_i, _ena);
    }
}

void Test::register_callback_conn(conn_cb func)
{
    _conn_cb = func; //有调用就临时生成一个函数
}

Test::test; //生成类的单例
