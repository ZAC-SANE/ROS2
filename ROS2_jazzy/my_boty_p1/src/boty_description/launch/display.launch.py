import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():

    # 1. Path to your package and Xacro model
    pkg_share = get_package_share_directory('boty_description')
    xacro_file = os.path.join(pkg_share, 'urdf', 'my_boty.urdf.xacro')

    # 2. Process Xacro dynamically using Command substitution
    robot_description_config = Command(['xacro ', xacro_file])
    
    # 3. Define the nodes to launch
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config}]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # 4. Return the complete package configuration
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])

