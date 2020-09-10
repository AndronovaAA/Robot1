#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from std_msgs.msg import String
import math

def talker():
    pub1 = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    joint1 = 0
    joint2 = 0
    joint3 = -0.1


    while not rospy.is_shutdown():
        position = JointState()
	position.header = Header()
	position.header.stamp = rospy.Time.now()
	position.name = ['base_to_right_cylinder', 'base_to_left_cylinder', 'base_to_up_box']
	position.position = [joint1, joint2, joint3]
	position.velocity = []
	position.effort = []
	rospy.loginfo(position)
        
	pub1.publish(position)
        rate.sleep()
	if (joint1 >= -0.9 and joint2 <= 0.9 and joint3 <= 0.1):
		joint1 -= 0.01
		joint2 += 0.01
		joint3 += 0.001
	else:
		break


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

