#!/bin/sh

roslaunch ur_e_gazebo ur10e.launch limited:=true &
sleep 3
roslaunch ur10_e_moveit_config ur10_e_moveit_planning_execution.launch sim:=true limited:=true &
sleep 3
roslaunch ur10_e_moveit_config moveit_rviz.launch config:=true &