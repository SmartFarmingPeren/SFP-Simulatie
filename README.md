# SFP-Simulatie

## Why ROS noetic and Unity
We use Unity because its able to be used for 3D simulations, a robot can be imported with an .urdf file and its able to make a connection with ROS. We use ROS to move the imported robot, the usage of ROS has been suggested by the Action group.


## Requirements
To setup everything there are some requirements to make the simulation usable.
* Virtual box with the SFP-Simulation .vbox 			[Code branch](https://github.com/SmartFarmingPeren/SFP-Simulatie/tree/ROS-Sim)
* Unity 2020.2.0b9 installed.							[Code branch](https://github.com/SmartFarmingPeren/SFP-Simulatie/tree/Unity-Sim)

The virtual machine network should be set up as a bridged adapter.
Unity 2020.2.0b9 is used for compatibility with imported packages for a ROS connection and to import the robot.

## ROS Setup
On the SFP-Simulation .vbox ROS-noetic is already installed.
If you wish to use a different machine for ROS development follow the below tutorials

To install and setup ROS two tutorials are used.
* To install ROS http://wiki.ros.org/Installation/Ubuntu
* For the further setup of ROS https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/0_ros_setup.md

Install dependencies.
```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update
```

## ROS usage

to compile the ROS workspace you can use the following command
> catkin_make
afterwhich you can use the following command to run a ROS script
> source devel/setup.bash
> roslaunch hello_world *launchfile*
The current launchfiles are used for:
launchfile | usage | script 
-----------|-------|-------
*hello.launch* | test script to send "100" to the unity machine **depricated** | Publisher.py
*read_joints.launch* |test script to read Unity messages | Subscriber.py
*send_joints.launch* | Used to read incoming joint data and send outgoing joint data | MoveJointsSub.py, MoveJoints.py

server_endpoint.py is the TCP server script. In this file you need to add the ROS topic and the server settings.
If the topic is meant for outbound traffic, that is to say towards the unity machine. It needs to be a RosSubscriber('TopicName', *ROSmsgType*, tcp_server)
If the topic is meant for inbound traffic, that is to say from the unity machine. It needs to be a RosPublisher('TopicName, *ROSmsgType*, queue_size=10)

The function names stem from the way they interact with the ROS topic system, **not** how the TCP system works. To send data over the TCP connection, the TCP script subscribes to the given ROS topic on which the TCP data is send. Afterwhich it will automatically send it to the other side of the TCP connection.
The same goes for the other direction. The TCP script publishes incomming TCP data to the given ROS topic.

Make sure the TopicNames match in the server_endpoint.py script.

### ROS message, service and action compiling
When making new messages they need to be added to the CMakeLists.txt file of the corresponding package. This needs to be done in the add_message_files() area.
The same goes for services and actions, which need to be added in the add_service_files() and add_action_files() area's

### ROS packages
When new packages are added to the ROS project they also need to be listed in the CMakeLists.txt file, this needs to be done in the find_package() area. It also needs to be added in the package.xml

For more information about the CMakeLists.txt it is recommended to watch or read a tutorial on CMake with ROS

### IP in params.yaml
You need to make a params.yaml file in the config folder of the hello_world project. In this file you can copy the contents of the _params.yaml and replace the *YOUR IP HERE* with the ROS machine's IP

## plans for the future
