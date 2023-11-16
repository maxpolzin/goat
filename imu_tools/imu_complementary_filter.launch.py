import os
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_dir = os.path.join(get_package_share_directory('imu_complementary_filter'), 'config')

    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package='imu_complementary_filter',
                executable='complementary_filter_node',
                name='imu_complementary_filter',
                output='screen',
                parameters=[os.path.join(config_dir, 'imu_complementary_filter.yaml')],
            )
        ]
    )