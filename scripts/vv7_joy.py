#!/usr/bin/env python

from sensor_msgs.msg import Joy
import rospy
from std_msgs.msg import Int16

"""

Author: kunfeng li
"""


class JoyToAll(object):
    def __init__(self):
        self.pub_steer = rospy.Publisher('/steer_value', Int16, queue_size=1)

        self.pub_acc1 = rospy.Publisher('/acc1_value', Int16, queue_size=1)

        self.pub_go = rospy.Publisher('/go_value', Int16, queue_size=1)

        self.sub = rospy.Subscriber('/joy', Joy, self.joy_cb, queue_size=1)

    def joy_cb(self, data):
        up = (1-data.axes[2])/2.0  # 0~1
        left_right = data.axes[0] * 1.0
        down = (data.axes[5]-1)/2.0  # 0~-1
        
        go=data.buttons[8]
        self.pub_go.publish(go)

        acc = up

        if down < -0.06:
            acc = down

        amount_acc1 = int(acc * 115+140)  # 25~255,<140 brake
        if amount_acc1 < 0:
            amount_acc1 = 0
        if amount_acc1 > 255:
            amount_acc1 = 255
        self.pub_acc1.publish(amount_acc1)

        amount_steer = int(left_right * 32767)
        self.pub_steer.publish(amount_steer)

        print("amount_steer: " + str(amount_steer))
        print("amount_gas: " + str(amount_acc1))
        print("go: " + str(go))


if __name__ == '__main__':
    rospy.init_node('from_joy_to_all')
    jts = JoyToAll()
    rospy.spin()
