#!/usr/bin/env python3

import rospy
from hello_world.msg import Text

TOPIC_NAME = 'HelloWorld'
NODE_NAME = 'SCREAMER'


def scream():
    pub = rospy.Publisher(TOPIC_NAME, Text, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        Msg = Text("100")
        pub.publish(Msg)
        rate.sleep()
        break


if __name__ == '__main__':
    try:
        scream()
    except rospy.ROSInterruptException:
        pass