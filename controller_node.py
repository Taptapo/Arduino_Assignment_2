import rclpy
from rclpy.node import Node


from std_msgs.msg import Int32, String



class ControllerNode(Node):


def init(self):
super().__init__('controller_node')


self.command_publisher = self.create_publisher(
String,
'/arduino_command',
10
        )


self.sensor_subscriber = self.create_subscription(
Int32,
'/arduino_sensor',
self.sensor_callback,
10
        )


def sensor_callback(self, message):


command = String()


if message.data (http://message.data/) > 500:
command.data (http://command.data/) = 'ON'
else:
command.data (http://command.data/) = 'OFF'


self.command_publisher.publish(command)


self.get_logger().info(
f'Sensor: {message.data (http://message.data/)} -> {command.data (http://command.data/)}'
        )



def main():
rclpy.init()


node = ControllerNode()


rclpy.spin(node)


node.destroy_node()


rclpy.shutdown()



if name == '__main__':
main()