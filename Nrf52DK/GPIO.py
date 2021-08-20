"""
注：官方建议使用gpiote库，有中断能力，性能会更好。
使用nrf52DK空模版开发
模版在SDK安装文件/examples/peripheral/template_project/pca10040/blank/ses下
在peripheral文件下有好多空模版，可以拿来开发使用
使用前提条件
1.将micro-ecc库git到SDK安装文件/external/micro-ecc文件下，并将文件名也改成micro-ecc
    git clone https://github.com/kmackay/micro-ecc
2.安装GNU-ARM工具
    先安装brew
    brew tap PX4/homebrew-px4
    brew update
    brew install gcc-arm-none-eabi
3.安装GNU make
    mac自带
4.使用文本打开SDK安装文件/components/toolchain/gcc/Makefile.posix，更改gcc路径
5.找到gcc-arm-none-eabi文件夹(mac默认在/usr/local/Cellar)，把其子文件bin的绝对路径粘贴到Makefile.posix中gcc路径
6.进入到SDK安装文件/external/micro-ecc/nrf52hr_armgcc_armgcc文件下
    执行make指令，无报错则完成
"""

"""
#main.c文件内容

#include <stdbool.h>
#include <stdint.h>

#include "nrf.h"
#include "nordic_common.h"
#include "boards.h"
#include "nrf_delay.h"
#include "nrf_gpio.h"

#define LED1_PIN 30

/**
 * @brief Function for application main entry.
 */
#define LED1_PIN 30

int main (void)
{
   nrf_gpio_cfg_input(LED1_PIN, NRF_GPIO_PIN_PULLUP);
   while(1)
   {
       nrf_delay_ms(1000);
       printf("%u", nrf_gpio_pin_read(LED1_PIN));
   }
}
/** @} */
"""
# Build--> build and debug
# Target --> connect J-Link --> Erase All
# Debug --> go 拷入文件
# Debug --> go 执行文件
