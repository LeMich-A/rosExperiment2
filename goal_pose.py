#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



# Callbacks definition

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    # rospy.loginfo("Current location: "+str(feedback))
    pass


def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('goal_pose')



def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    global navclient
    global finished
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()


rospy.loginfo("moving to point 1 \n")
moveToPose(0.0026674522741821916,-4.94854804344073, 0, 0, 0, -0.9995121716790542, 0.031231693284561324)
rospy.loginfo("successfully moved to point 1 \n")

rospy.loginfo("moving to point 2 \n")
moveToPose(-4.816321224016534, -4.384473733083735, 0, 0, 0, 0.8271150623614761, 0.5620326268240764)
rospy.loginfo("successfully moved to point 2 \n")

rospy.loginfo("moving to point 3 \n")
moveToPose(-4.9780169506410274, 0.019622006295543004, 0, 0, 0, 0.6936211082463848, 0.7203400295659383)
rospy.loginfo("successfully moved to point 3 \n")

rospy.loginfo("moving to point  \n")
moveToPose(0.5563874532005274, 0.04176794018581296, 0, 0, 0, 0.13348249881265917, 0.9910511704804795)
rospy.loginfo("successfully moved to point  \n")




if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())