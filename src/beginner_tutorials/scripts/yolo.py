#!/usr/bin/env python
import rospy
from darknet_ros_msgs.msg import BoundingBoxes
def callback(data):
   #print('1')
   for ans in data.bounding_boxes:
      #print('1')
      if ans.Class == 'person':
         x = (ans.xmin+ans.xmax)/2
         y = (ans.ymin+ans.ymax)/2
         print("123")
         print(x)
         print(y)
def get():
   rospy.init_node('recevier', anonymous=True)
   rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback)
   rospy.spin()

if __name__ == '__main__':
   get()
