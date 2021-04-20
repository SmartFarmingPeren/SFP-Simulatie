#!/usr/bin/env python3

import rospy
from hello_world.msg import UR10eMoveitJoints, UR10eJoints

TOPIC_NAME = 'JointsMover'
NODE_NAME = 'JointsSender'


def SendJoints(jointsIn):
    joints = UR10eJoints()
    if jointsIn.joint_00 < 10:
        joints.joint_00 = 50.0
    elif jointsIn.joint_00 < 60:
        joints.joint_00 = 100.0
    elif jointsIn.joint_00 < 110:
        joints.joint_00 = 150.0
    elif jointsIn.joint_00 < 160:
        joints.joint_00 = 200.0
    else:
        joints.joint_00 = 0.0


    pub = rospy.Publisher(TOPIC_NAME, UR10eJoints, queue_size=10)
    # rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        pub.publish(joints)
        rate.sleep()
        break

# if __name__ == '__main__':
#     SendJoints()
