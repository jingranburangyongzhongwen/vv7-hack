# Vv7 CAN Hack - related code & packages

通过Xbox one实现对vv7加速、转向的控制

## Screenshots

[![1](gifs/vv7_1.gif)]

![2](gifs/vv7_2.gif)


## Features
* Uses an XBox controller as an input device
* LT加速，RT减速，Xbox按键实现加速允许，刚开始以-3m/s2反向加速度停在原地，按下一次xbox启用加速，再按一次取消，并以-3m/s2减速，再按启动，再按取消，以此类推。减速时无法加速。左摇杆实现左右转向
* Full braking authority at any speed

## Things to konw
* 清楚msg格式，一行一个字节，DLC代表多少行
* struct.pack打包msg，部分数据需要移位拼接为整数个字节
* bus为1
* 看清无符号还是有符号
* 由于涉及车辆协议，创建msg的文件未上传

## Try it yourself
### Hardware requirements
* [Panda](https://shop.comma.ai/products/panda-obd-ii-dongle) + USB cable
* Either a [Girafe](https://shop.comma.ai/products/giraffe-honda) or a good old soldering iron/crimper + an OBD-II connector.
* WEY VV7 2018
* Decent laptop + Xbox Controller
* [Bosch ScanTool](https://www.alltiresupply.com/products/north-american-comprehensive-diagnostic-scan-tool?variant=16349255301) to reset those errors.

### Software Dependencies
 * Python 2.7
 * ROS Kinetic
 * Ubuntu 16.04
 * [cantools library](https://github.com/eerimoq/cantools) :`pip install cantools`
 * [pandacan library](https://shop.comma.ai/products/panda-obd-ii-dongle) :`pip install pandacan`
 * [can_msgs](http://wiki.ros.org/can_msgs) : `sudo apt-get install ros-kinetic-can-msgs`

### Tips
 * Run vv7_control.py with root permission!
 * Add `source /home/username/.bashrc` to the end of /root/.bashrc, then run `source /root/.bashrc` with root permission

## Credits
Thanks to [civic-hack](https://github.com/pixmoving-moveit/civic-hack), [comma.ai](https://comma.ai/) for its incredible [software](https://github.com/commaai/openpilot) and [hardware](https://shop.comma.ai/products/panda-obd-ii-dongle). Without them above, the hacking process would have been a lot more tedious.


