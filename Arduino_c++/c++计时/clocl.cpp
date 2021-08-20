#include <iostream>
#include <cmath>
#include <time.h>
#include <string.h>

using namespace std;
string a;

int main()
{
    // 使用clock()构造clock_t对象(实际上是long类型的变量)
    clock_t t1 = clock();
    a = "off";

    // 一段计算
    for(int i = 0; i < 1000000; i++) {
//        pow(2, i);
        if (i % 2 == 0) {
            a = "off";
        } else {a = "on";}
    }


    // 计算clock差，除以clock数/每秒，即可求出秒数
    // 将秒数乘以1000得到毫秒数
    cout << (clock() - t1) * 1.0 / CLOCKS_PER_SEC * 1000 << endl;
    return 0;
}
