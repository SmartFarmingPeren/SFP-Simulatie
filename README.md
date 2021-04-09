# SFP-Simulatie

## Why ROS noetic and Unity



## Requirements

## ROS Setup

## Setup Unity
To setup the unity environment download the git and add the "Boomgaard simulatie" folder in the Unity folder to your Unity projects in [Unity Hub](https://unity3d.com/get-unity/download). Then download the [2020.2.0b9](https://unity3d.com/unity/beta/2020.2.0b9) Unity version. Once you have opened the Unity project open the "ground_test" scene to get the simulation environment.

### Bug fix with packages


## Import Robot
To import robots through a .urdf file the [URDF-Importer](https://github.com/Unity-Technologies/URDF-Importer?path=/com.unity.robotics.urdf-importer#v0.2.0) package has been added to the project. To import the ur10 download the "ur10" and "ur_description/meshes/ur10" folders from the [reveal_packages](https://github.com/PositronicsLab/reveal_packages/tree/master/industrial_arm/scenario/models/urdf) github page, place them in the Unity environment in the "Assets/URDF" folder, right click on the .urdf file and select "Import Robot from Selected URDF file". Then click "Import URDF" and give the new prefab a location.
For later use the ur10_moveit_config or the ur10_e_moveit_config folder from the [universal_robot](https://github.com/ros-industrial/universal_robot) git needs to be placed in the ROS/src folder.

## Connect to ROS
To make a connection to ros the [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector?path=/com.unity.robotics.ros-tcp-connector#v0.2.0) package has been added to the project. Create a new empty for the ROS opperations and add the "ROS Connection" script to it as a new component. Generate the ROS messages by selecting the "Generate ROS Messages..." from the now present Robotics tab in the top bar, then select the ROS folder as the ROS message path and Build the msg and srv from ROS/src/ros_tcp_endpoint and Build the RobotTrajectory.msg from ROS/src/moveit_msgs/msg. Add the "ROS IP Address" in the ROS Connection script of the machine running ros (**Note:** may not work with a virtual machine) and Play to make the connection.

For a more in depth explanation on how to set up a Unity connection with ROS visit the [Pick-and-Place](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/README.md) Tutorial from the [Unity-Robotics-Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub) github page.


## Plans for the future
