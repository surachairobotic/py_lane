import os
import launch
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    node = Node(
        package='py_lane',
        executable='lane_guidance_node',
        output='screen',
    )
    return launch.LaunchDescription([node])
