#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy,cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(bag):
	global i
	path = "../img/"
	b = CvBridge()
	img = b.imgmsg_to_cv2(bag, 'bgr8')
	name = str(i) + ".png"
	cv2.imwrite(path + name,img)
	i += 1
	print(path + str(i))

if __name__ == '__main__':
	rospy.init_node('video_to_image')
	i = 0
	rospy.Subscriber('/rgb/image_raw_color', Image, callback, queue_size=1)
	rospy.spin()
