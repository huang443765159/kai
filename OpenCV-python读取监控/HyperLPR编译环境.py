"""
1.去官网下载HyperLPR包
2.安装python依赖的各个库
Keras >2.0.0
Theano >0.9
Numpy >1.1
Scipy 0.19.1
OpenCV-python >3.0
Scikit-image 0.13.0
PIL
安装OPENCV库，去Opencv官网下载3.4.3版本的包
然后编译环境并且安装相关关联库
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
1.cd opencv-3.4.4
2.mkdir build
3.cd build
4. cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON ..
5.make -j4
6.sudo make install
7.sudo /bin/bash -c 'echo "usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
8.sudo ldconfig
测试
cd ../samples/
sudo cmake .
sudo make -j $(nproc)
cd cpp/
./cpp-example-facedetect 图片路径
显示图像 成功
完成

MAC版本OpenCV编译
去OpenCV官网下载3.4.3版本source code zip包
然后解压
1.cd opencv-3.4.4
2.mkdir build
3.cd build
4. cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON ..
5.make -j4
6.sudo make install

hyperlpr编译--官网教程
1.cd hyperlpr/Pri-Linux
2.mkdir build
3.cd mkdir
4.cmake ../
5.sudo make -j4
注：如果opencv-python安装的最新版本会和hyperlpr库不兼容，导致无法使用，需要降低版本
pip3 install opencv-python=3.4.6.27
降低opencv-python的版本就可以用了

hyperlpr使用 pip版本 需编译完之后使用
1.安装hyperlpr
pip3 install hyperlpr
2.降低opencv版本
回退到4以前的版本，因为最新版本opencv和hyperlpr不兼容
pip3 install opencv-python==3.4.6.27
3.安装opencv-python的运行环境
sudo apt install libqt4-test
如果执行还错误执行编译
sudo apt install libatlas-base-dev
sudo apt install libjasper-dev
sudo apt install libqtgui4
sudo apt install libhdf5-dev
sudo apt install libhdf5-serial-dev

4.安装最新的opencv会报错，原因有一个函数更改了
module 'cv2' has no attribute 'estimateRigidTransform' #222
estimateRigidTransform 替换为了 estimateAffinePartial2D 直接跳转到错误一行，然后把函数更改为以下
就成功了
mat_ = cv2.estimateAffinePartial2D(org_pts, target_pts, True)[0]
"""