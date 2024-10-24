# Copyright 2020 ros2_control Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import xacro

from launch import LaunchDescription
from launch.actions import RegisterEventHandler, EmitEvent
from launch.events import Shutdown
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    pkg_share = get_package_share_directory('pca9685_ros2_control_example')

    xacro_file = os.path.join(pkg_share, 'urdf', 'robot.xacro.urdf')
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)

    robot_description = {"robot_description": doc.toxml()}
    robot_controllers = PathJoinSubstitution([pkg_share,"config","mixed_controller.yaml"])

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers],
        output="both",
        on_exit=EmitEvent(event=Shutdown(reason='ros2_control_node crashed... shutting down'))
    )

    joint_group_velocity_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_group_velocity_controller", "--controller-manager", "/controller_manager"],
    )

    diff_drive_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller", "--controller-manager", "/controller_manager"],
    )

    # joint_state_broadcaster_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    # )


    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description],
    )

    nodes = [
        control_node,
        joint_group_velocity_controller_spawner,
        diff_drive_controller_spawner,
        # joint_state_broadcaster_spawner,
        robot_state_publisher_node
    ]

    return LaunchDescription(nodes)