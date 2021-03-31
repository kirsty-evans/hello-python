"""
Sensor.py

Reading out sensor data.
"""


def read_sensor():  # defining a function called read_sensor
    # do something to read the sensor and get data from it
    data = 10.4  # defining data as an example
    result = {
        "source": "voltage sensor",
        "value": data,
    }
    return result
