#!/usr/bin/env python3

import rospy
from hello_world.msg import UR10eMoveitJoints, UR10eJoints

TOPIC_NAME = 'JointsMover'
NODE_NAME = 'JointsSender'


def SendJoints(jointsIn): #jointsIn
    joints = UR10eJoints()
    # joints.joint_00 = 70
    # joints.joint_01 = -20
    # joints.joint_02 = 30
    # joints.joint_03 = -40
    # joints.joint_04 = 70
    # joints.joint_05 = -70
    
    if jointsIn.joint_00 < 10:
        joints.joint_00 = 50.0
        joints.joint_01 = -20
        joints.joint_02 = 40
        joints.joint_03 = -50
        joints.joint_04 = 70
        joints.joint_05 = -70
    elif jointsIn.joint_00 < 60:
        joints.joint_00 = 100.0
        joints.joint_01 = -40
        joints.joint_02 = 60
        joints.joint_03 = -70
        joints.joint_04 = 90
        joints.joint_05 = -90
    elif jointsIn.joint_00 < 110:
        joints.joint_00 = 150.0
        joints.joint_01 = -60
        joints.joint_02 = 90
        joints.joint_03 = -100
        joints.joint_04 = 110
        joints.joint_05 = -110
    elif jointsIn.joint_00 < 160:
        joints.joint_00 = 200.0
        joints.joint_01 = -80
        joints.joint_02 = 120
        joints.joint_03 = -130
        joints.joint_04 = 130
        joints.joint_05 = -130
    else:
        joints.joint_00 = 0.0
        joints.joint_01 = 0.0
        joints.joint_02 = 0.0
        joints.joint_03 = 0.0
        joints.joint_04 = 0.0
        joints.joint_05 = 0.0


    pub = rospy.Publisher(TOPIC_NAME, UR10eJoints, queue_size=10)
    # rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        print("I send:\n",joints)
        pub.publish(joints)
        rate.sleep()
        break

# if __name__ == '__main__':
#     SendJoints()
