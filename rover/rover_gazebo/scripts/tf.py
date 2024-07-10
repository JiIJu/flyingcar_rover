#!/usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

def tf_broadcaster():
    rospy.init_node('tf_broadcaster')
    broadcaster = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(5.0)
    while not rospy.is_shutdown():
        transform = TransformStamped()
        transform.header.stamp = rospy.Time.now()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_link"
        transform.transform.translation.x = 0.0  # Adjust translation values as needed
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0
        transform.transform.rotation.x = 0.0  # No rotation for simplicity
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0

        broadcaster.sendTransform(transform)
        rate.sleep()

if __name__ == '__main__':
    try:
        tf_broadcaster()
    except rospy.ROSInterruptException:
        pass
