import board
import busio
import time
import adafruit_bno055

# Initialize I2C bus and BNO055 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

last_val = 0xFFFF

def read_sensor_data():
    # Read data
    accel_x, accel_y, accel_z = sensor.acceleration
    gyro_x, gyro_y, gyro_z = sensor.gyro
    euler_x, euler_y, euler_z = sensor.euler
    temp_celsius = sensor.temperature
    mag_x, mag_y, mag_z = sensor.magnetic

    # Return data as dict
    return {
        "acceleration": {"x": accel_x, "y": accel_y, "z": accel_z},
        "gyroscope": {"x": gyro_x, "y": gyro_y, "z": gyro_z},
        "euler": {"roll": euler_x, "pitch": euler_y, "yaw": euler_z},
        "temperature": temp_celsius,
        "magnetic": {"x": mag_x, "y": mag_y, "z": mag_z}
    }

def read_and_return_sensor_data():
    try:
        while True:
            sensor_data = read_sensor_data()
            print("Sensor Data:", sensor_data) # For testing
            time.sleep(1)  # Delay before next reading
            return sensor_data # Returns data
    # Exception handling
    except Exception as e:
        print("Error:", e)

# The libraries needed to be installed can be found here: https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/python-circuitpython
