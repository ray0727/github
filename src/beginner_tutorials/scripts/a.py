   def gettaginfo(self,data):
        for detection in data.detections:
         self.tagid = detection.id
             pose = Pose()
             self.xx = detection.pose.position.x
             self.yy = detection.pose.position.y
             self.zz = detection.pose.position.z
             self.orxx = detection.pose.orientation.x
             self.oryy = detection.pose.orientation.y
             self.orzz = detection.pose.orientation.z
             self.orww = detection.pose.orientation.w 
      
      def apriltag_callback(self):
        rospy.Subscriber("/apriltags/detections", AprilTagDetections, self.gettaginfo)
        rospy.spin#20180802
