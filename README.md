# SFP-Simulatie

## Why ROS noetic and Unity
We use Unity because its able to be used for 3D simulations, a robot can be imported with an .urdf file and its able to make a connection with ROS. We use ROS to move the imported robot, the usage of ROS has been suggested by the Action group.


## Requirements
To setup everything there are some requirements to make the simulation usable.
* A machine with Ubuntu 20.04 installed for ROS.
* A machine with Unity 2020.2.0b9 installed.

Both machines need to be able to connect to each other via the internet to create the ROS connection.
Unity 2020.2.0b9 is used for compatibility with imported packages for a ROS connection and to import the robot.

## ROS Setup
To install and setup ROS two tutorials are used.
* To install ROS http://wiki.ros.org/Installation/Ubuntu
* For the further setup of ROS https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/0_ros_setup.md

### Base install ROS
Open the terminal in the Ubuntu machine.
Set up the sources
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
Set the keys.
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```
Install ROS.
```
sudo apt update

sudo apt install ros-noetic-desktop-full
```
To set up the environment there are two options.
If you're going to use this once or twice (needs to be done every time you want to use ROS) use:
```
source /opt/ros/noetic/setup.bash
```
If you want the environment to be automaticcally set up use:
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
Install dependencies.
```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update
```
### Download and set up Unity-Robotics-Hub git
At the moment Unity-Robotics-Hub is being used to connect to Unity.
Clone the git with:
```
git clone --recurse-submodules https://github.com/Unity-Technologies/Unity-Robotics-Hub.git
```
Then navigate to ```/PATH/TO/Unity-Robotics-Hub/tutorials/pick_and_place/ROS``` or put the ROS folder into your own work environment.
Install the required dependecies with:
```
sudo apt-get install python3-pip ros-noetic-robot-state-publisher ros-noetic-moveit ros-noetic-rosbridge-suite ros-noetic-joy ros-noetic-ros-control ros-noetic-ros-controllers
sudo -H pip3 install rospkg jsonpickle
```
After the dependecies are installed create the workplace with ```catkin_make``` and source the workplace with ```source devel/setup.bash```. The source needs to be done everytime you want to use the workspace.
Make the machine discoverable to a ROS connection with.
```
echo "ROS_IP: $(hostname -I)" > src/niryo_moveit/config/params.yaml
```


## Setup Unity
To setup the unity environment download the git and add the "Boomgaard simulatie" folder in the Unity folder to your Unity projects in [Unity Hub](https://unity3d.com/get-unity/download). Then download the [2020.2.0b9](https://unity3d.com/unity/beta/2020.2.0b9) Unity version. Once you have opened the Unity project open the "ground_test" scene to get the simulation environment.
![afbeelding](https://user-images.githubusercontent.com/62204721/114179190-f86f5500-993e-11eb-9c6c-58e3a2ac3b10.png)


### Bug fix with packages
If the Unity project does not open and you get the following error message there are some actions that need to be done to safely open the Unity project.

![unityGitError](https://user-images.githubusercontent.com/62204721/114179478-54d27480-993f-11eb-87cf-2733367ce5d5.png)

First navigate to ```PATH_TO\SFP-Simulatie\Unity\Boomgaard simulatie\Packages``` and open the manifest.json file with an editor, locate
* com.unity.robotics.ros-tcp-connector
* com.unity.robotics.urdf-importer

and cut them out of the file, for safety paste them in a notepad.
Then open the Unity project in safe mode and open the package manager window.
![package manager unity](https://user-images.githubusercontent.com/62204721/114180783-f6a69100-9940-11eb-8128-0652eb695e6e.png)

In this window import the packages by selecting the "add package from git url..." option.
![giturl](https://user-images.githubusercontent.com/62204721/114181177-77658d00-9941-11eb-99d7-12991b8a13be.png)
and paste the folowing urls in the add bar.
* https://github.com/Unity-Technologies/ROS-TCP-Connector.git?path=/com.unity.robotics.ros-tcp-connector#v0.2.0
* https://github.com/Unity-Technologies/URDF-Importer.git?path=/com.unity.robotics.urdf-importer#v0.2.0

![afbeelding](https://user-images.githubusercontent.com/62204721/114181535-ea6f0380-9941-11eb-8988-365fd54a0441.png)

This should make you exit safe mode and you can open you Unity project.


## Import Robot
To import robots through a .urdf file the [URDF-Importer](https://github.com/Unity-Technologies/URDF-Importer?path=/com.unity.robotics.urdf-importer#v0.2.0) package has been added to the project. To import the ur10 download the "ur10" and "ur_description/meshes/ur10" folders from the [reveal_packages](https://github.com/PositronicsLab/reveal_packages/tree/master/industrial_arm/scenario/models/urdf) github page, place them in the Unity environment in the "Assets/URDF" folder, right click on the .urdf file and select "Import Robot from Selected URDF file". Then click "Import URDF" and give the new prefab a location.
![import](https://user-images.githubusercontent.com/62204721/114182214-a8928d00-9942-11eb-8ee5-01b38b7fcc50.png)

![afbeelding](https://user-images.githubusercontent.com/62204721/114182153-99abda80-9942-11eb-8756-130165926e30.png)

For later use the ur10_moveit_config or the ur10_e_moveit_config folder from the [universal_robot](https://github.com/ros-industrial/universal_robot) git needs to be placed in the ROS/src folder.

## Connect to ROS
To make a connection to ros the [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector?path=/com.unity.robotics.ros-tcp-connector#v0.2.0) package has been added to the project. Create a new empty for the ROS opperations and add the "ROS Connection" script to it as a new component.
![afbeelding](https://user-images.githubusercontent.com/62204721/114182543-0626d980-9943-11eb-8a6a-897de02f8b65.png)

Generate the ROS messages by selecting the "Generate ROS Messages..." from the now present Robotics tab in the top bar,
![rosmessage](https://user-images.githubusercontent.com/62204721/114182767-4c7c3880-9943-11eb-9a8c-261db21eae25.png)

then select the ROS folder as the ROS message path and Build the msg and srv from ROS/src/ros_tcp_endpoint and Build the RobotTrajectory.msg from ROS/src/moveit_msgs/msg.

![afbeelding](https://user-images.githubusercontent.com/62204721/114183048-9d8c2c80-9943-11eb-92ca-5f085d393861.png)

![afbeelding](https://user-images.githubusercontent.com/62204721/114183232-beed1880-9943-11eb-9e33-c5259561da32.png)

Add the "ROS IP Address" in the ROS Connection script of the machine running ros (**Note:** may not work with a virtual machine) and Play to make the connection.

![afbeelding](https://user-images.githubusercontent.com/62204721/114183356-e3e18b80-9943-11eb-939c-fd2e4ad26350.png)


## Plans for the future
