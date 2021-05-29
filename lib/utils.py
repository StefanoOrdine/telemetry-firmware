#!/usr/bin/env python
import time

__version__ = '0.0.1'

def safely_read_light_sensor(lt):
    for index in range(10):
        lux = lt.lux()
        light = lt.light()
        if (lux != 0):
            break
        time.sleep_ms(500)
    return (lux, light)

def print_sensors(temperature, altitude, pressure, si_temperature, humidity, dew_point, t_ambient, humid_ambient, light, lux, acceleration, roll, pitch, battery_voltage):
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
