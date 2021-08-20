byte* get_data() {
    byte data[3] = (01, 02, 03);
    return data;
}

//如果想要返回array的话，函数应该使用指针模式

//取指针的返回值的时候应该也用指针类型获取，或者使用auto类型

#include "func.cpp"

byte* new_data = get_data()
printf(new_data[0])
printf(new_data[1])
printf(new_data[2])
