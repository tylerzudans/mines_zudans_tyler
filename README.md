# mines_zudans_tyler
ROS package for making the turtlesim node draw the Mines "M"

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
