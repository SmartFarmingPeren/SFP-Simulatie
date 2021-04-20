#!/usr/bin/env python3

import rospy
import MoveJoints as mj
from hello_world.msg import UR10eMoveitJoints, UR10eJoints

TOPIC_NAME = 'JointsSub'
NODE_NAME = 'JointsreadAndSender'


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", data)
    mj.SendJoints(data)

def listener():
    rospy.init_node(NODE_NAME, anonymous=True)
    rospy.Subscriber(TOPIC_NAME, UR10eJoints, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()