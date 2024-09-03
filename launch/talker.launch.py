from launch import LaunchDescription
from lauch_ros.actions import Node

def generate_launch_description():
 return LaunchDescription([
        Node(
             package='demo_nodes_cpp',
             executable='talker'
             )
 ])            
