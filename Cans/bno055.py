import board
import busio
import time
import adafruit_bno055

# Initialize I2C bus and BNO055 sensor
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
sensor = adafruit_bno055.BNO055_I2C(i2c)

last_val = 0xFFFF

def read_sensor_data():
    # Read data
    accel_x, accel_y, accel_z = sensor.acceleration
    gyro_x, gyro_y, gyro_z = sensor.gyro
    euler_x, euler_y, euler_z = sensor.euler
    temp_celsius = sensor.temperature
    mag_x, mag_y, mag_z = sensor.magnetic

    # Return data as array
    return [gyro_x,gyro_y,gyro_z,euler_x,euler_y,euler_z]   #roll pitch yaw
        #"A": {"x": accel_x, "y": accel_y, "z": accel_z},    #acceleration
        #"gyroscope": {"x": gyro_x, "y": gyro_y, "z": gyro_z},   #gyroscope
        #"euler": {"r": euler_x, "p": euler_y, "y": euler_z}, #euler absolute orientation, roll pitch yaw}

def read_and_return_sensor_data():
    try:
        while True:
            sensor_data = read_sensor_data()
            print("CANMOTION:", sensor_data) # For testing
            time.sleep(1)  # Delay before next reading
            return sensor_data # Returns data
    # Exception handling
    except Exception as e:
        print("Error:", e)

# The libraries needed to be installed can be found here: https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/python-circuitpython
