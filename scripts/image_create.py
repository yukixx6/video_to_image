#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy,cv2,sys
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class IMG:
    def __init__(self):
	self.img = 0
	self.i = 0
	self.flag = False
#        self.name = "50_"
	self.name = raw_input("file name >> ")
	self.name += "_" 
	self.time = input("cycle [s] >> ") # 100mm is 0.2, 50mm is 0.15

    def callback(self,bag):
#	path = "../img/"
	b = CvBridge()
	self.img = b.imgmsg_to_cv2(bag, 'bgr8')
#	name = str(self.i) + ".png"
#	cv2.imwrite(path + name,img)
#	i += 1
#	print(path + str(self.i))
	self.flag = True

    def create_img(self,date):
	if self.flag == True:
            path = "/home/ubuntu/catkin_ws/src/video_to_image/img/"
            name = self.name + str(self.i) + ".png"
            cv2.imwrite(path + name,self.img)
            self.i += 1
            print(name)
	    self.flag = False

if __name__ == '__main__':
    rospy.init_node('video_to_image')
    d = IMG()
    rospy.Subscriber('/rgb/image_raw_color', Image, d.callback, queue_size=1)
    rospy.Timer(rospy.Duration(d.time), d.create_img)
    rospy.spin()
