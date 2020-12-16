#!/usr/bin/env python3.7
# EX1  What temperature (in Fahrenheit) would you like converted to Celsius?

f_temp = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))

c_temp = (f_temp -32) * 5 / 9

print(f_temp, "F is", round(c_temp, 2), "C")