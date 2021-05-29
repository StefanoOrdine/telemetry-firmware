#!/usr/bin/env python

import time
import pycom

from pysense import Pysense
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from LIS2HH12 import LIS2HH12
from utils import safely_read_light_sensor, print_sensors

# Fuchsia: Reading sensors
pycom.rgbled(0x330033)
py = Pysense()

mp = MPL3115A2(py, mode=ALTITUDE)
altitude = mp.altitude()
temperature = mp.temperature()
mpp = MPL3115A2(py, mode=PRESSURE)
pressure = mpp.pressure()

si = SI7006A20(py)
si_temperature = si.temperature()
humidity = si.humidity()
dew_point = si.dew_point()
t_ambient = 24.4
humid_ambient = si.humid_ambient(t_ambient)

lt = LTR329ALS01(py)
(lux, light) = safely_read_light_sensor(lt)
(light_blue, light_red) = light

li = LIS2HH12(py)
acceleration = li.acceleration()
[x, y, z] = acceleration
roll = li.roll()
pitch = li.pitch()

battery_voltage = py.read_battery_voltage()

print_sensors(temperature, altitude, pressure, si_temperature, humidity, dew_point, t_ambient, humid_ambient, light, lux, acceleration, roll, pitch, battery_voltage)

# Blue: Networking
pycom.rgbled(0x000022)
pybytes.connect()
tup = ( \
    temperature, \
    altitude, \
    pressure, \
    si_temperature, \
    humidity, \
    light_blue, \
    light_red, \
    lux, \
    roll, \
    pitch, \
    battery_voltage \
)
pybytes.send_signal(1, tup)

# Greenwater: Delay to safely push all data
pycom.rgbled(0x002222)
time.sleep(5)
pybytes.disconnect()

# Green: Execution finished successfully
pycom.rgbled(0x002200)
time.sleep(2)

# Off: Sleep for 1 hour
pycom.rgbled(0x000000)
time_milliseconds = 60 * 60 * 1000
pybytes.deepsleep(time_milliseconds)