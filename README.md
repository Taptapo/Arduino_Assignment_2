# Arduino_Assignment_2
# Arduino and ROS 2 Sensor Control System

## 1. Project Description

This project demonstrates communication between an Arduino and ROS 2.

The Arduino reads data from a water sensor connected to analog pin A0.
The sensor value is sent to the computer through a USB serial connection.

ROS 2 receives the sensor data and decides whether to turn the Arduino LED ON or OFF.

If the sensor value is higher than 500, the LED turns ON.
If the sensor value is 500 or lower, the LED turns OFF.

## 2. Components

- Arduino board
- Water sensor
- USB cable
- Computer
- ROS 2
- Python 3

## 3. Software

The project uses:

- Python
- ROS 2
- rclpy
- pyserial
- Arduino IDE

## 4. Project Files

### arduino_controller.ino

Arduino code.

It:
- reads the water sensor from A0;
- sends the sensor value through Serial;
- receives ON/OFF commands;
- controls the built-in LED.

### arduino_node.py

ROS 2 node for communication between Arduino and ROS 2.

It:
- reads sensor data from Arduino;
- publishes the data to `/arduino_sensor`;
- receives commands from `/arduino_command`;
- sends commands to Arduino.

### controller_node.py

ROS 2 controller node.

It receives the sensor value from `/arduino_sensor`.

The control logic is:

- Sensor value > 500 → ON
- Sensor value <= 500 → OFF

The command is published to `/arduino_command`.

## 5. ROS 2 Topics

### /arduino_sensor

Message type: `Int32`

This topic sends the sensor value from Arduino to the controller node.

### /arduino_command

Message type: `String`

This topic sends `ON` or `OFF` commands to the Arduino node.

## 6. System Diagram

Water Sensor
↓
Arduino
↓
USB Serial
↓
arduino_node.py
↓
/arduino_sensor
↓
controller_node.py
↓
/arduino_command
↓
arduino_node.py
↓
Arduino LED

## 7. How to Run

### Step 1 – Upload Arduino Code

Open `arduino_controller.ino` in Arduino IDE and upload it to the Arduino board.

The serial communication speed must be:

9600 baud

### Step 2 – Connect Arduino

Connect the Arduino to the computer using a USB cable.

The Python node uses:

`/dev/ttyACM0`

as the serial port.

### Step 3 – Run ROS 2

Open a terminal and run the Arduino node:

`ros2 run <package_name> arduino_node`

Open another terminal and run the controller node:

`ros2 run <package_name> controller_node`

## 8. Expected Result

The Arduino continuously reads the water sensor.

For example:

Sensor value: 650 → LED ON

Sensor value: 350 → LED OFF

The ROS 2 nodes communicate using the `/arduino_sensor` and `/arduino_command` topics.

## 9. Author

Student: Artem, Galym, Azizkhan, Yerkinbek.

Course: Actuators, Sensors and Signals

Assignment #02
