# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:17:03 2023

@author: collin
"""

def convert_temp(num, metric):
    
    if metric.upper() == "F":
        # F to C:   C = (F - 32) * (5/9)
        celsius = (num - 32) * (5/9)
        
        # F to K:   K = (F - 32) * (5/9) + 273.15
        kelvin = celsius + 273.15
        
        # results rounded with round() function
        print(num, "degrees F is ", round(celsius,2), "degrees C")
        print(num, "degrees F is ", round(kelvin,2) , "K")
        print("******************************")
        
    elif metric.upper() == "C":
        # C to F:   F = (9/5) * C + 32 or F = (1.8 * C) + 32
        fahrenheit = (1.8 * num) + 32
        
        # C to K:   K = C + 273.15
        kelvin = num + 273.15
        
        # results rounded with 'f' format specifier
        print(f"{num} degrees C is {fahrenheit:.2f} degrees F")
        print(f"{num} degrees C is {kelvin:.2f} K")
        print("******************************")
        
    elif metric.upper() == "K":
        # K to C:   C = K - 273.15
        celsius = num - 273.15
        
        # K to F:   F = (K - 273.15) * (9/5) + 32 or F = 1.8 * (K - 273.15) + 32
        fahrenheit = 1.8 * (num - 273.15) + 32
        
        print(f"{num} K is {celsius:.2f} degrees C")
        print(f"{num} K is {fahrenheit:.2f} degrees F")
        print("******************************")
        
    # will need to add else statement to check for exception
    else:
        print("Please add a valid number/metric")
        

convert_temp(32, "F")
convert_temp(0, "F")
convert_temp(80, "F")

convert_temp(-34, "C")
convert_temp(0, "C")
convert_temp(100, "C")

convert_temp(0, "K")
convert_temp(100, "K")
convert_temp(273.15, "K")

convert_temp(0, " ")
convert_temp(" ", " ")
convert_temp("test", "test")