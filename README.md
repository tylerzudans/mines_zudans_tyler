# mines_zudans_tyler
ROS package for making the turtlesim node draw the Mines "M"

**Installation**:

-install ROS Melodic
-install turtlesim
-in your catkin_ws/scr clone this directory

**Compile and Run**:
From catkin_ws

-catkin_make
-source devel/setup.bash
-roslaunch mines_zudans_tyler draw_m.launch *if turlesim is already running*
-roslaunch mines_zudans_tyler turtlesim_and_draw_m.launch *if no turtlesim is running*
