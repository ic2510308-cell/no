Sensor Data Logger
A sensor data collection and logging utility for drone and Arduino projects.
Overview
This Python utility enables real-time recording and analysis of data from various sensors such as MPU6050 and VL53L0X. It's designed for drone flight testing, sensor calibration, and data analysis purposes.
Features

Real-time Data Logging: Records sensor data with timestamps
CSV Format Export: Easy integration with Excel and other analysis tools
Statistical Analysis: Provides basic statistics (average, min, max)
Extensible Architecture: Easy to add new sensors

Usage
Basic Usage
pythonfrom sensor_data_logger import SensorDataLogger

# Create logger instance
logger = SensorDataLogger("my_sensor_data.csv")

# Add sensor data
logger.add_data("MPU6050_GyroX", 1.25, "deg/s")
logger.add_data("VL53L0X_Distance", 142, "mm")

# Save to file
logger.save_to_file()
Statistical Information
python# Get statistics for a specific sensor
stats = logger.get_statistics("VL53L0X_Distance")
print(f"Average: {stats['average']:.2f}mm")
print(f"Min: {stats['min']}mm")
print(f"Max: {stats['max']}mm")
Supported Sensors
Currently tested with the following sensors:

MPU6050: Gyroscope and Accelerometer
VL53L0X: Laser Distance Sensor
Ultrasonic Sensors: HC-SR04, etc.
Other analog/digital sensors can be easily added

Example Execution
bashpython sensor_data_logger.py
This will record 10 sample data points and save them to drone_sensors.csv.
Output Format
CSV file is saved in the following format:
2024-11-20 14:30:25.123,MPU6050_GyroX,1.25,deg/s
2024-11-20 14:30:25.223,VL53L0X_Distance,142,mm
Requirements

Python 3.6 or higher
Standard library only (no additional installations required)

Future Development

 Add graph visualization features
 Real-time sensor integration (serial communication)
 Data filtering functionality
 Web dashboard interface

License
MIT License
Author
Rain
High School Student (10th Grade) - Mechanical Engineering & Robotics Projects
Contact
If you have any questions or suggestions about this project, please open an issue!
