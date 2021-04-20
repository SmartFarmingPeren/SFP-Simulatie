#!/usr/bin/env python3

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from hello_world.msg import Text, UR10eMoveitJoints, UR10eJoints


def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)
    
    tcp_server.start({
        'String': RosSubscriber('HelloWorld', Text, tcp_server),
        'SubJoints': RosPublisher('JointsSub', UR10eJoints),
        'MoveJoints': RosSubscriber('JointsMover', UR10eJoints, tcp_server)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
