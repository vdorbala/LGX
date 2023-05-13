#!/usr/bin/env python

import rospy

import cv2

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image

import sys, select, termios, tty

import numpy as np

import message_filters

from tf.transformations import euler_from_quaternion

import time

from cv_bridge import CvBridge

class ros_move:
    def __init__(self):
        settings = termios.tcgetattr(sys.stdin)

        self.pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)

        self.rate = rospy.Rate(10) # 10hz
        self.yaw = 0

        self.current_pose = Odometry()

        self.sub = rospy.Subscriber("odom", Odometry, self.odom_callback)

        # self.sub.registerCallback(self.odom_callback)

        self.distance_traveled = 0
        self.turn_speed = 1
        self.linear_speed = 0.2 
        self.rate = rospy.Rate(10)

        time.sleep(0.1)
        # rospy.Subscriber("odom", Odometry, self.odom_callback)    

    def odom_callback(self, data):
        self.current_pose = data

        orientation_q = data.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (_, _, self.yaw) = euler_from_quaternion(orientation_list)


    def rotate_degree(self, degree): # Will not work with more than 360

        move_twist = Twist()
        move_twist.linear.x = 0; move_twist.linear.y = 0; move_twist.linear.z = 0
        move_twist.angular.x = 0; move_twist.angular.y = 0; move_twist.angular.z = self.turn_speed

        initial_yaw = self.yaw
        if initial_yaw == 0:
            self.pub.publish(move_twist)
        print('rotate initial_yaw: ',initial_yaw)   
        goal_yaw = initial_yaw + degree/180.0*np.math.pi
        if goal_yaw > np.math.pi:
            goal_yaw = goal_yaw - 2*np.math.pi
        print('rotate goal_yaw: ',goal_yaw)   

        error = 10
        try:
            while not rospy.is_shutdown():
                # print(self.yaw)
                error = np.abs(self.yaw - goal_yaw)
                if error < 0.1:
                    break
                self.pub.publish(move_twist)
                self.rate.sleep()
        except Exception as e:
            print(e)

        finally:
            twist = Twist()
            twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
            self.pub.publish(twist)

        print('rotate end yaw: ',self.yaw)


    def move_forward(self, distance):
        twist = Twist()

        while not rospy.is_shutdown():
            twist.linear.x = self.linear_speed
            self.pub.publish(twist)
            self.rate.sleep()
            distance_delta = self.current_pose.twist.twist.linear.x * self.rate.sleep_dur.to_sec()
            self.distance_traveled += distance_delta
            if self.distance_traveled >= distance:
                twist.linear.x = 0
                self.pub.publish(twist)
                break


class image_subscribe:
    def __init__(self):

        # depth_sub = message_filters.Subscriber('depth_image', Image)
        # self.rgb_sub = message_filters.Subscriber('rgb/image_rect_color', Image)
        # odom_sub = message_filters.Subscriber('rgb_image', Odometry)

        self.image_pub = rospy.Publisher("glip_bb_img",Image)

        self.image_sub = rospy.Subscriber("/zed2i/zed_node/stereo/image_rect_color", Image, self.image_callback)

        self.bridge = CvBridge()

        self.cv_image =  np.zeros((512,512,3), np.uint8)

        time.sleep(0.1)

    def image_callback(self, data):

        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        # cv2.imshow("Image window", cv_image)
        # cv2.waitKey(3)

        
    def get_img(self):
        return self.cv_image

    def pub_img(self, image):
        try:
          self.image_pub.publish(self.bridge.cv2_to_imgmsg(image, "bgr8"))
        except CvBridgeError as e:
          print(e)
          
        time.sleep(1)


if __name__=="__main__":

    rotate = ros_move()
    imsub = image_subscribe()
    rotate.rotate_degree(353)