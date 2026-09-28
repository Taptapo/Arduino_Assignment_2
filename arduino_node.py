import rclpy
from rclpy.node import Node


import serial


from std_msgs.msg import Int32, String



class ArduinoNode(Node):


def init(self):
super().__init__('arduino_node')


self.serial_port = serial.Serial(
'/dev/ttyACM0',
9600,
timeout=1
        )


self.sensor_publisher = self.create_publisher(
Int32,
'/arduino_sensor',
10
        )


self.command_subscriber = self.create_subscription(
String,
'/arduino_command',
self.send_command,
10
        )


self.timer = self.create_timer(
0.1,
self.read (http://self.read/)_serial
        )


def read_serial(self):


if self.serial_port.in (http://port.in/)_waiting > 0:


data = self.serial_port.readline().decode().strip()


try:
value = int(data)


message = Int32()
message.data (http://message.data/) = value


self.sensor_publisher.publish(message)


self.get_logger().info(f'Sensor: {value}')


except ValueError:
pass


def send_command(self, message):


command = message.data (http://message.data/) + '\n'


self.serial_port.write(command.encode())


self.get_logger().info(f'Sent: {message.data (http://message.data/)}')



def main():


rclpy.init()


node = ArduinoNode()


rclpy.spin(node)


node.destroy_node()


rclpy.shutdown()



if name == '__main__':
main()