# mines_zudans_tyler
ROS package for making the turtlesim node draw the Mines "M". This was written for Project 1: "Learning Robot Operating System" of Colorado School of Mines CSCI473 [http://inside.mines.edu/~hzhang/Courses/CSCI473-573/index.html] in February of 2020. The code is A ROS package that contains:

1. A python script (mines_zudans_tyler/scripts/turtle_M_maker.py) that spawns a node that sends a set of Twist messages to the cmd_vel topic to make the turle move in the shape of an "M".
1. Two launch files to run depending upon whether turtle_sim is already running

**Installation**:

1. install ROS Melodic - http://wiki.ros.org/melodic/Installation/Ubuntu
1. install turtlesim - http://wiki.ros.org/turtlesim
1. in your catkin_ws/src clone this directory
   1. $ `cd ~/catkin_ws/src`
   1. $ `git clone https://github.com/tylerzudans/mines_zudans_tyler.git`

**Compile and Run**:
(From within catkin_ws)

1. $ `catkin_make`
2. $ `source devel/setup.bash`
3. $ `roslaunch mines_zudans_tyler draw_m.launch` (*if turlesim is already running*)
4. $ `roslaunch mines_zudans_tyler turtlesim_and_draw_m.launch` (*if no turtlesim is running*)
