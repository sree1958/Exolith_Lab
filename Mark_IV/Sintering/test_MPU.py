import RPi.GPIO as GPIO
import time
from datetime import date, datetime
import arrow
from Logging import logger
from sensorGroup import sensor_group
import os
from dotenv import load_dotenv
from elevationTracking import elevation_tracker

load_dotenv()
logger = logger()
elevation_tracker = elevation_tracker()


def sensorGroupCheck():
    sg = sensor_group()
    light_sensor_status = False
    orientation_sensor_status = False

    try:
        light_sensor_status = sg.light_sensor_health()
        orientation_sensor_status = sg.orientation_sensor_health()

    except Exception as e:
        logger.logInfo("Sensor Group Failure: {}".format(e))

    if light_sensor_status and orientation_sensor_status:
        logger.logInfo("Sensor Group Healthy")
        return True

    else:
        logger.logInfo(
            "Sensor Group Failure: light_sensor_status: {} \norientation_sensor_status: {}".format(
                light_sensor_status, orientation_sensor_status
            )
        )
        return False


def main():
    sensorStatus = sensorGroupCheck()
    elevation_tracker.tiltAngle()

if __name__ == "__main__":
    main()
