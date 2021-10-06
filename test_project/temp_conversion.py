#!/usr/bin/env python3

"""
Python program that handles both Fahrenheit (F) to Celsius (C)
and Celsius (C) to Fahrenheit (F) temperature conversions.
"""

# Begin convert temperature function
def convert_temp(scale=None, source_temp=None):
    # Handles both upper and lower case scale inputs along with the appropriate temperature conversions
    if (scale == "F") or (scale == "f"):
        return "C", (source_temp - 32.0) * (5.0/9.0)
    elif (scale == "C") or (scale == "c"):
        return "F", (source_temp * (9.0/5.0)) + 32.0
    else:
        raise TypeError("Only F or C are allowed!")

print("-------- Temperature Conversion Program --------")
scale = input("Enter (F) or (C): " )
source_temp = float(input("Enter temperature: " ))
# Calls the function and prints the output
a = convert_temp(scale, source_temp)
print(str(round(source_temp,1)) + " degrees " + scale.upper() + " is " + str(round(a[1],1)) + " degrees " + a[0])
print("------------------------------------------------")
