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

   

    def move(self):
       
        vel_msg = Twist()
        t0 = float(rospy.Time.now().to_sec())
        t1 = float(rospy.Time.now().to_sec())
        squre_length=2
        speed=0.2
        while t1-t0 <(squre_length/speed):

            
            t1 = float(rospy.Time.now().to_sec())
            # Linear velocity in the x-axis.
            vel_msg.linear.x =speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)


        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        
        self.velocity_publisher.publish(vel_msg)
    def rotate(self):
       
        vel_msg = Twist()
        t0 = float(rospy.Time.now().to_sec())
        t1 = float(rospy.Time.now().to_sec())
        req_rotation=1.57
        ang_speed=0.2
        while t1-t0 <(req_rotation/ang_speed):

            t1 = float(rospy.Time.now().to_sec())
           
            vel_msg.linear.x =0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = ang_speed
            self.velocity_publisher.publish(vel_msg)

            
     
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        # If we press control + C, the node will stop.
        #rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move()       
        x.rotate()
        x.move()
        x.rotate()
        x.move()
        x.rotate()
        x.move()
    except rospy.ROSInterruptException:
        pass
