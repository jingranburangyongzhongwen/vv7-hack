#!/usr/bin/env python

from panda import Panda
from vv7_create_msgs import create_acc1_command, create_acc2_command, create_acc3_command, create_steer_command
import time
import rospy
from std_msgs.msg import Int16

"""

Author: kunfeng li
"""


class AllPublisher(object):
    def __init__(self):
        self.p = Panda()
        self.p.set_safety_mode(self.p.SAFETY_ALLOUTPUT)
        self.acc1_val = 80
        self.steer_val = 0
        self.go_val = 0
        self.sub_acc1 = rospy.Subscriber(
            '/acc1_value', Int16, self.acc1_cb, queue_size=1)
        self.sub_steer = rospy.Subscriber(
            '/steer_value', Int16, self.steer_cb, queue_size=1)
        self.sub_go = rospy.Subscriber(
            '/go_value', Int16, self.go_cb, queue_size=1)

    def go_cb(self, data):
        self.go_val = (self.go_val+data.data)%2
        print("go_val: " + str(self.go_val))
    
    def acc1_cb(self, data):
        print("acc1_cb: " + str(data))
        if data.data > 255:
            self.acc1_val = 255
        elif data.data < 0:
            self.acc1_val = 0
        self.acc1_val = data.data

    def steer_cb(self, data):
        print("steer_cb: " + str(data))
        self.steer_val = data.data
        if data.data > 32767:
            self.steer_val = 32767
        elif data.data < -32768:
            self.steer_val = -32768

    def run(self):
        print("Publishing...")
        idx_counter = 0
        total_cmds_sent = 0
        while not rospy.is_shutdown():

            if(self.go_val==0):
                if(self.acc1_val>80):
                    self.acc1_val = 80

            cmd = create_acc1_command(self.acc1_val, idx_counter)
            print("\n--------------------------------------------")
            print("Sending  acc1 val: " + str(self.acc1_val) + "\n" + str(cmd) +
                  " (#" + str(total_cmds_sent) +
                  ")")
            # addr,dat,bus
            self.p.can_send(cmd[0], cmd[2], 1)

            cmd = create_acc2_command(idx_counter)
            self.p.can_send(cmd[0], cmd[2], 1)

            cmd = create_acc3_command(idx_counter)
            self.p.can_send(cmd[0], cmd[2], 1)

            cmd = create_steer_command(self.steer_val, idx_counter)
            print("--------------------------------------------")
            print("Sending steer val: " + str(self.steer_val) + "\n" + str(cmd) +
                  " (#" + str(total_cmds_sent) +
                  ") ")
            print("--------------------------------------------")
            self.p.can_send(cmd[0], cmd[2], 1)

            idx_counter += 1
            idx_counter %= 15

            total_cmds_sent += 1
            time.sleep(0.01)


if __name__ == '__main__':
    rospy.init_node('all_sender')
    sp = AllPublisher()
    sp.run()
