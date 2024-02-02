#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist



class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        
        self.rate = rospy.Rate(10)

   

    def circle(self):
       
        vel_msg = Twist()
       
        
        speed=1
        ang_speed=1
        while True:

            
            t1 = float(rospy.Time.now().to_sec())
            # Linear velocity in the x-axis.
            vel_msg.linear.x =speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = ang_speed=1
            self.velocity_publisher.publish(vel_msg)


       
        
  


if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.circle()
    except rospy.ROSInterruptException:
        pass
