#!/usr/bin/env python

import time
import pycom

from pysense import Pysense
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from LIS2HH12 import LIS2HH12

# White: Main execution started
pycom.rgbled(0x070707)

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
light = lt.light()
[light_blue, light_red] = light
lux = lt.lux()

li = LIS2HH12(py)
acceleration = li.acceleration()
[x, y, z] = acceleration
roll = li.roll()
pitch = li.pitch()

battery_voltage = py.read_battery_voltage()

print("\nMPL3115A2")
print("Temperature: " + str(temperature))
print("Altitude: " + str(altitude))
print("Pressure: " + str(pressure))
print("\nSI7006A20")
print("Temperature: " + str(si_temperature)+ " deg C and Relative Humidity: " + str(humidity) + " %RH")
print("Dew point: "+ str(dew_point) + " deg C")
print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(humid_ambient) + "%RH")
print("\nLTR329ALS01")
print("Light (channel Blue lux, channel Red lux): " + str(light))
print("Lux: " + str(lux))
print("\nLIS2HH12")
print("Acceleration: " + str(acceleration))
print("Roll: " + str(roll))
print("Pitch: " + str(pitch))
print("\nFiPy")
print("Battery voltage: " + str(battery_voltage))

# Fuchsia: Networking
pybytes.connect()
pycom.rgbled(0x330033)
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

# Greenwater: Wait the signals to be all pushed
pycom.rgbled(0x003333)
time.sleep(15)
pybytes.disconnect()

# Green: Execution finished
pycom.rgbled(0x003300)
time.sleep(2)

# Off: Sleep for 5 minutes
pycom.rgbled(0x000000)
time_milliseconds = 5 * 60 * 1000
pybytes.deepsleep(time_milliseconds)