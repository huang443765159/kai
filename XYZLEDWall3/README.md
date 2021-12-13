# XYZLEDWall3


### 概览
本模块用于控制led灯带显示动画效果

### 使用设备
灯带：WS2815
* 功率：0.24w(max)/珠
* 电压：DC12V
* 灯珠：60珠/m
控制器：ArtNet协议16通道控制器：最多可控制10880个单IC灯珠

### 使用教程
1-安装opencv不含gui版本：否则会和pyqt5冲突
* pip3 install opencv-contrib-python-headless
2-设置树莓派静态IP：需要和控制器IP在同频段
* sudo nano /etc/dhcpcd.conf
* 添加以下内容
  interface eth0
  static ip_address=192.168.1.100 
3-灯带接线方式
  DI和BI短接然后接到控制器DAT口
  供电负级接到控制器GND口
  