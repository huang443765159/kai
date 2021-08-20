"""
北欧指定使用ses IDE而且全免费
1.激活IDE
    mac物理地址查询：点击左上角苹果标志 --> 系统偏好设置 --> 网络 --> 高级 --> 硬件
    即可看见MAC物理地址
    win物理地址：在终端输入ipconfig -all 在网卡地址那就是物理地址
2.登录SES时有一个获取License，点击进入Ses官网，然后填写邮箱和电脑物理地址，去邮箱粘贴许可密码
    在Tools --> License Manager --> Activate Embedded Studio，将许可密码粘贴到此位置，然后点击Install，完成

----   ----    ---   ----
测试和编写MESH通信
SDK17.0往上版本和SES有兼容问题，网上说16.0无问题
1.将for mesh 文件和nrf5_SDK_xxxx_d674dde压缩到同级目录下
2.在for mesh文件的example里打开一个模版，然后设置SDK路径，不然找不到SDK编译会报错
    在SES IDE选择Tools --> Options --> Building --> Build --> Global Macos
    点击后面... 然后修改成SKD_ROOT=SDK文件的绝对路径
3.在mesh example文件下的client和server文件里找到flash_placement.xml文件
    MemorySegment name must be changed from "RAM" to "RAM1":
    将文件其中一句中的name="RAM"中的RAM修改成RAM1
   <MemorySegment name="RAM1" start="$(RAM_PH_START)" size="$(RAM_PH_SIZE)">
4.同在client和server文件里找到相对应芯片的.emProject文件，使用文本编辑打开
    In "linker_section_placements_segments" you must refer to "RAM1", replacing "RAM":
    将文件以下语句中的RAM修改成RAM1
    linker_section_placements_segments="FLASH RX 0x0 0x100000;RAM1 RWX 0x20000000 0x40000"
5.此时就可以编译成功了，但是编译成功后执行debug --> go 会报错找不多hex文件
    因为编译好的hex文件在mesh的build里面
    解决办法：右键点击主工程文件 --> Options --> 顶部左侧下拉选择Common --> Debug (Loader) --> Additional Load File[0]
    添加编译好的路径到hex即可
"""


"""
https://devzone.nordicsemi.com/f/nordic-q-a/23983/how-do-i-calculate-throughput-for-a-ble-mesh
蓝牙mesh通信测试，mesh网络最大发送11个字节，3.46kb/s,延迟20ms

"""
