#!/usr/bin/env python3

import rospy
from hello_world.msg import UR10eJoints

TOPIC_NAME = 'JointsMover'
NODE_NAME = 'JointsSender'


def SendJoints():
    # UR10eJoints joints = UR10eJoints
    # joints.joint_00 = float 50.0
    # joints.joint_01 = float 0.0
    # joints.joint_02 = float 0.0
    # joints.joint_03 = float 0.0
    # joints.joint_04 = float 0.0
    # joints.joint_05 = float 0.0


    pub = rospy.Publisher(TOPIC_NAME, UR10eJoints, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        Msg = UR10eJoints("100.0")
        pub.publish(Msg)
        rate.sleep()
        break

if __name__ == '__main__':
    SendJoints()
