import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

from .dynamixel_controller import Dynamixel


class GoatController(Node):
    def __init__(self):
        super().__init__('goat_controller')

        self.joystick_topic = self.declare_parameter('joystick_topic', '/joy').get_parameter_value().string_value

        self.linear_scale = self.declare_parameter('linear_scale', 0.5).get_parameter_value().double_value
        self.angular_scale = self.declare_parameter('angular_scale', 0.5).get_parameter_value().double_value

        self.joystick_subscription = self.create_subscription(Joy, self.joystick_topic, self.joystick_callback, 10)

        self.get_logger().info(f"Subscribed to {self.joystick_topic}")

        self.servo = Dynamixel(ID=[11, 12, 13, 14], descriptive_device_name="DYNAMIXEL_GOAT", series_name=["xw", "xw", "xw", "xw"], baudrate=1000000, port_name="/dev/ttyUSB0")
        self.servo.begin_communication()
        self.servo.set_operating_mode("velocity", ID="all")

        self.ID_FRONT_LEFT = 11
        self.ID_BACK_LEFT = 12
        self.ID_FRONT_RIGHT = 14 
        self.ID_BACK_RIGHT = 13

        self.DIR_FRONT_LEFT = -1
        self.DIR_BACK_LEFT = -1
        self.DIR_FRONT_RIGHT = 1
        self.DIR_BACK_RIGHT = 1


    def joystick_callback(self, msg: Joy):

        linear_velocity = 0.0
        angular_velocity = 0.0

        if abs(msg.axes[1]) > 0.1 or abs(msg.axes[0]) > 0.1:
            linear_velocity = self.linear_scale * msg.axes[1]
            angular_velocity = self.angular_scale * msg.axes[0]

        left_wheel_velocity = linear_velocity - angular_velocity
        right_wheel_velocity = linear_velocity + angular_velocity

        left_wheel_dynamixel_velocity = int(left_wheel_velocity * 310)
        right_wheel_dynamixel_velocity = int(right_wheel_velocity * 310)

        self.servo.write_velocity(self.DIR_FRONT_LEFT * left_wheel_dynamixel_velocity, self.ID_FRONT_LEFT)
        self.servo.write_velocity(self.DIR_FRONT_RIGHT * right_wheel_dynamixel_velocity, self.ID_FRONT_RIGHT)
        self.servo.write_velocity(self.DIR_BACK_LEFT * left_wheel_dynamixel_velocity, self.ID_BACK_LEFT)
        self.servo.write_velocity(self.DIR_BACK_RIGHT * right_wheel_dynamixel_velocity, self.ID_BACK_RIGHT)


def main(args=None):
    rclpy.init(args=args)
    goat_controller_node = GoatController()
    rclpy.spin(goat_controller_node)
    goat_controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
