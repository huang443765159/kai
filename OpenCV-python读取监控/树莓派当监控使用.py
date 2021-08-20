"""
1、安装motion
sudo apt install motion
2、配置
nano /etc/motion/motion.conf
修改以下内容
#  #  #  #  #  #  #  #  #  #  #  #  #  #
# Start in daemon (background) mode and release terminal (default: off)
# 在后台运行。设置为off将在前台运行
daemon on
# Videodevice to be used for capturing  (default /dev/video0)
# for FreeBSD default is /dev/bktr0
# 视频设备，刚才ls看到的
videodevice /dev/video0
# Image width (pixels). Valid range: Camera dependent, default: 352
# 图像宽
width 320
# Image height (pixels). Valid range: Camera dependent, default: 288
# 图像高
height 240
# The setting for keep-alive of network socket, should improve performance on compatible net cameras.
# off: The historical implementation using HTTP/1.0, closing the socket after each http request.
# force: Use HTTP/1.0 requests with keep alive header to reuse the same connection.
# on: Use HTTP/1.1 requests that support keep alive as default.
# Default: off
# 开启KeepAlive功能
netcam_keepalive on
# Output 'normal' pictures when motion is detected (default: on)
# Valid values: on, off, first, best, center
# When set to 'first', only the first picture of an event is saved.
# Picture with most motion of an event is saved when set to 'best'.
# Picture with motion nearest center of picture is saved when set to 'center'.
# Can be used as preview shot for the corresponding movie.
# 禁用自动拍照保存的功能
output_pictures off
# Use ffmpeg to encode movies in realtime (default: off)
# 禁用自动拍摄视频保存的功能
ffmpeg_output_movies off
# The mini-http server listens to this port for requests (default: 0 = disabled)
# 视频监听的端口，默认8081
stream_port 1001
# Quality of the jpeg (in percent) images produced (default: 50)
# 图像质量
stream_quality 50
# Output frames at 1 fps when no motion is detected and increase to the
# rate given by stream_maxrate when motion is detected (default: off)
stream_motion on
# Maximum framerate for stream streams (default: 1)
# 帧数8，需要先把上面的选项改成on
stream_maxrate 8
# Set the authentication method (default: 0)
# 0 = disabled
# 1 = Basic authentication
# 2 = MD5 digest (the safer authentication)
# 改成1，增加授权验证，访问需要输入密码
stream_auth_method 1
# Authentication for the stream. Syntax username:password
# Default: not defined (Disabled)
# 设置用户名username和密码password
stream_authentication username:password
# Restrict stream connections to localhost only (default: on)
# 改成off允许外网访问视频
stream_localhost off
# TCP/IP port for the http server to listen on (default: 0 = disabled)
# WEB控制台监听的端口，默认8080
webcontrol_port 1000
# 改成off允许外网访问web控制台
webcontrol_localhost off

"""