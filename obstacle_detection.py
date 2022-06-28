#!usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

k = 1000

def laser_readings(msg):
    #print('s1 [0]')
    #print (msg.ranges[0])
    #print('s1 [90]')
    #print (msg.ranges[90])
    #print('s1 [180]')
    #print (msg.ranges[180])
    global k
    k = msg.ranges[0]

def motion():
    rospy.init_node('obstacle_detection')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    rospy.Subscriber('/scan', LaserScan, laser_readings)
    move = Twist()
    global k
    #print (k)
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        if(k>0.6):
            print(k)
            move.linear.x = 0.2
            pub.publish(move)
        else:
            print(k)
            move.linear.x = 0
            pub.publish(move)
            rospy.signal_shutdown
            rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        motion()
    except rospy.ROSInterruptException:
        pass
