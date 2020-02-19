#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

#speed constants
turnSpeed = 2
linearSpeed = 5
rosHZ = 500

#Letter size
m_scale = 2;

#constant messages for sending
turnTwist = Twist()
turnTwist.angular.z = turnSpeed

linearTwist = Twist()
linearTwist.linear.x= linearSpeed

#both instructions arrays for controlling robots
instruction_index = 0
#set of human readable instructions

#m_instructions =[("turn",90),("go", 3)]#letter M
square = [("turn",90),("go", 1),("turn",90),("go", 1),("turn",90),("go", 1),("turn",90),("go", 1)]#letter M
the_m =[("turn",(90+45)),("go", 1.0),("turn",(45)),("go", 0.5),("turn",90),("go", 0.2),("turn",90),("go", 0.1),("turn",270),("go", 1.4),("turn",270),("go", 0.1),("turn",90),("go", 0.2),("turn",90),("go", 0.5),("turn",90),("go", 0.2),("turn",90),("go", 0.1),("turn",270),("go", 1.2),("turn",225),("go", 1.14),("turn",90),("go", 1.14),("turn",225),("go", 1.2),("turn",270),("go", 0.1),("turn",90),("go", 0.2),("turn",90),("go", 0.5),("turn",90),("go", 0.2),("turn",90),("go", 0.1),("turn",270),("go", 1.4),("turn",270),("go", 0.1),("turn",90),("go", 0.2),("turn",90),("go", 0.5),("turn",45),("go", 1.0),("turn",270)]
m_instructions = the_m
t_instructions =[]# twist set of machine readable twists


def initialize_m_instructions():
    for instruction in m_instructions: # for each human readable instruction
        if(instruction[0] == "turn"):#if its a turn
            t_count = int(rotate_seconds(instruction[1])*rosHZ) # number of turn m_instructions
            print(t_count)
            for i in range(0,t_count):
                t_instructions.append(turnTwist)
        else:#TODO add for linear
            t_count = int(forward_seconds(instruction[1])*rosHZ*m_scale)#distance increased for larger M
            print(t_count)
            for i in range(0,t_count):
                t_instructions.append(linearTwist)



#def get_next_twist()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def rotate_seconds(degrees):
    return ((degrees*2*math.pi/360)/turnSpeed)
    #return (degrees/turnSpeed)

def forward_seconds(distance):
    return (distance/linearSpeed)

def move():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    directions = Twist()
    directions.linear.x = 0.0
    directions.angular.z= 2
    loopRate = rospy.Rate(rosHZ)

    while True :
        pub.publish(directions)
        loopRate.sleep()

def move_m():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    directions = Twist()
    #directions.linear.x = 0.0
    #directions.angular.z= 2
    loopRate = rospy.Rate(rosHZ)
    time.sleep(2)
    for i in range(len(t_instructions)):#for each machine instruction
        pub.publish(t_instructions[i]) #publish machine instruction
        loopRate.sleep()
    pub.publish(Twist())#stop
if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_draw_m', anonymous=True)
        initialize_m_instructions()#create twist list for turtle to use
        move_m()

    except rospy.ROSInterruptException:
        pass
