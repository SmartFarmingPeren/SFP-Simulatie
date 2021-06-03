## create catkin workspace:

` mkdir -p *projectname*/src`

Install package dependencies not already in your workspace:

`rosdep install -y --from-paths . --ignore-src --rosdistro melodic`

Configure catking workspace:

```sh
cd *projectname*
catkin config --extend /opt/ros/melodic --cmake-args -DCMAKE_BUILD_TYPE=Release
catkin build
```

Source the catkin workspace[2]:

```sh
source *projectname*/devel/setup.bash
```

to launch the project:

```sh
roslaunch *projectname* *launchfile*.launch
```

example: `roslaunch ur10e_moveit_config demo.launch` roslaunch contains autocomplete for loaded catkin workspaces.[5]
Only 1 catkin workspace can be sourced at a time.[7]


## Sources:

1. [ROS melodic Installation](http://wiki.ros.org/melodic/Installation/Ubuntu)
2. [Moveit Installation](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html)
3. [ROS-industrial Installation](http://wiki.ros.org/Industrial/Install)
4. [Universal Robot for ROS-industrial](https://github.com/ros-industrial/universal_robot)
5. [MoveIt setup_assistant tutorial](https://www.youtube.com/watch?v=9aK0UDBKWT8)
6. [Convert xarco file to urdf](https://answers.ros.org/question/10401/how-to-convert-xacro-file-to-urdf-file/)
7. [Several catkin workspaces](https://answers.ros.org/question/175234/several-catkin-workspaces/)



### ROS topics, nodes, publishers and subscribers

A Node is a running program. ROS devides a program into multiple nodes. e.g. for a robot with a path planner there are 3 nodes: A wheel odometer, a path planner and a motor controller. These nodes talk through topics. On these topics messages are published and the subscribed nodes can read those topics.

* Any node can publish a message to any topic
* Any node can subscribe to any topic
* Multiple nodes can publish to the same topic
* Multiple nodes can subscribe to the same topic
* A node can publish to multiple topics
* A node can subscribe to multiple topics

# publish/subscribe tools
Command | Description
--------|-----------
rosnode list | shows all running nodes
rosnode info /some_node | shows detailed info of the node. E.G. the topics it is publishing or subscribed to
rostopic list | shows all topics
rostopic info /some_topic | shows detailed info of a topic. E.G. all the nodes that are publishing or subscribed to that topic
rostopic echo /some_topic | print out the data that is published to that topic
rostopic pub /some_topic msg/MessageType "data:value" | Publish data to a topic, formated in YAML ( use tab completion for pre-formated version )

Topics and messages are of a specific type, E.G. string, numerical etc.

# messages
* A serialization format for structured data
* Allows nodes written in C++ and Python to communicate with each other
* Defined in a .msg file
* Must be compiled into C++ / Python classes before using them

# Ros master
* A server that tracks the network addresses of all other nodes
    * Also tracks other information like parameters
* Informs subscribers about nodes publishing on the same topic
* Publisher and subscriber establish a peer-to-peer connection
* Nodes must know network address of master on startup (ROS_MASTER_URI)
* Can be started with `roscore` or `roslaunch`

Master does not handle any data. Only keeps track of meta-information: What nodes are out there, etc...
Does however manage passing meta-information between nodes.
ROS-master is usually localhost:1234 if running on one PC.

roslaunch will start a roscore if there is not one already running. If this roslaunch is stopped or exists the ros master will also exit. Any other ros nodes depending on that ros master will lose the ros master aswell.

Create a roscore in the terminal to prevent this.

[Source](https://youtu.be/bJB9tv4ThV4)

# Services

ROS's version of a remote procedure call system (RPC).
Exposes a function that is implemented by a server and allows different clients to call that function.
* A node can implement one or more services. ( server )
* Any node can call a service ( Client )
* Calls are synchronous / blocking ( while waiting it can't do anything else )
    * For long running tasks use a ROS-action

## Service messages
* Must define a .srv message that defines a request message and a response message.

Example:
```
string name         # argument
---
float64 distance    # return value
```

## ROS-service command line tools
Command | Description
------- | ---------
rosservice list | lists all the available services
rosservice info /some_service | shows detailed information about the service 
rosservice call /some_service "param1:0.0" | Calls the service directly from the command line. Uses YAML
rossrv show my_msgs/ServiceName | will print the .srv file format. my_msgs is the name of the package the service resides in. 