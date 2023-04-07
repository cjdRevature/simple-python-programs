# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:17:03 2023

@author: collin
"""

def convert_temp(num, unit):
    if not type(num) == int or type(num) == float:
        print("Please enter a valid number")
        return
    
    print("******************************")
    if unit.upper() == "F":
        # F to C:   C = (F - 32) * (5/9)
        celsius = (num - 32) * (5/9)
        # F to K:   K = (F - 32) * (5/9) + 273.15
        kelvin = celsius + 273.15
        # results rounded with round() function
        print(num, "degrees F is ", round(celsius,2), "degrees C")
        print(num, "degrees F is ", round(kelvin,2) , "K")
        print("******************************")
    elif unit.upper() == "C":
        # C to F:   F = (9/5) * C + 32 or F = (1.8 * C) + 32
        fahrenheit = (1.8 * num) + 32
        # C to K:   K = C + 273.15
        kelvin = num + 273.15
        # results rounded with 'f' format specifier
        print(f"{num} degrees C is {fahrenheit:.2f} degrees F")
        print(f"{num} degrees C is {kelvin:.2f} K")
        print("******************************")
    elif unit.upper() == "K":
        # K to C:   C = K - 273.15
        celsius = num - 273.15
        # K to F:   F = (K - 273.15) * (9/5) + 32 or F = 1.8 * (K - 273.15) + 32
        fahrenheit = 1.8 * (num - 273.15) + 32
        print(f"{num} K is {celsius:.2f} degrees C")
        print(f"{num} K is {fahrenheit:.2f} degrees F")
        print("******************************")
    # will need to add else statement to check for exception
    else:
        print("Please add a valid number/unit")
        
def convert_length(num, unit):
    if not type(num) == int or type(num) == float:
        print("Please enter a valid number")
        return
    
    print("******************************")
    if unit.lower() == "mm":
        # mm to cm:    cm = mm / 10
        cm = num / 10
    	# mm to inches:    in = mm / 25.4
        inches = num / 25.4
        # mm to feet:    ft = mm / 304.8
        feet = num / 304.8
        # mm to m:     m = mm / 1000
        m = num / 1000
        # mm to yards:  yards = mm * 0.0010936133
        yards = num * 0.0010936133
        # mm to km:    km = mm / 1,000,000
        km = num / 1000000
        # mm to mile:	 mi = mm / 1,609,344
        mi = num / 1609344
        print(f"{num} millimeter(s) is {cm:.2f} centimeters")
        print(f"{num} millimeter(s) is {inches:.2f} inches")
        print(f"{num} millimeter(s) is {feet:.4f} feet")
        print(f"{num} millimeter(s) is {m:.4f} meters")
        print(f"{num} millimeter(s) is {yards:.4f} yards")
        print(f"{num} millimeter(s) is {km:.8f} kilometers")
        print(f"{num} millimeter(s) is {mi:.8f} miles")
        print("******************************")  
    elif unit.lower() == "cm":
        # cm to mm:    mm = cm * 10
        mm = num * 10
    	# cm to inches:  cm / 2.54  
        inches = num / 2.54
        # cm to ft:   cm * 0.0328 
        feet = num * 0.0328
        # cm to m:     cm / 100
        m = num / 1000
        # cm to yards:  cm * 0.010936133
        yards = num * 0.010936133
        # cm to km:    cm / 100,000
        km = num / 100000
        # cm to mile:	cm * 0.0000062137 
        mi = num * 0.0000062137
        print(f"{num} centimeter(s) is {mm:.2f} millimeters")
        print(f"{num} centimeter(s) is {inches:.2f} inches")
        print(f"{num} centimeter(s) is {feet:.4f} feet")
        print(f"{num} centimeter(s) is {m:.4f} meters")
        print(f"{num} centimeter(s) is {yards:.4f} yards")
        print(f"{num} centimeter(s) is {km:.8f} kilometers")
        print(f"{num} centimeter(s) is {mi:.8f} miles")
        print("******************************")
    elif unit.lower() == "inches":
        # inches to mm:    in * 25.4
        mm = num * 25.4
    	# inches to cm:    in * 2.54
        cm = num * 2.54        
        # inches to ft:    in / 12
        feet = num / 3        
        # inches to m:     in / 39.37
        m = num / 39.37        
        # inches to yards:  in / 36
        yards = num / 36        
        # inches to km:    in / 39,370
        km = num / 39370        
        # inches to mile:	in / 63,360
        mi = num / 63360        
        print(f"{num} inch(es) is {mm:.2f} millimeters")
        print(f"{num} inch(es) is {cm:.2f} centimeters")
        print(f"{num} inch(es) is {feet:.4f} feet")
        print(f"{num} inch(es) is {m:.4f} meters")
        print(f"{num} inch(es) is {yards:.4f} yards")
        print(f"{num} inch(es) is {km:.8f} kilometers")
        print(f"{num} inch(es) is {mi:.8f} miles")
        print("******************************")        
    elif unit.lower() == "feet":
        # feet to mm: mm = ft * 304.8
        mm = num * 304.8        
        # feet to cm: cm = ft * 30.48
        cm = num * 30.48        
        # feet to inches: inches = ft * 12
        inches = num * 12        
        # feet to yards: yards = ft / 3
        yards = num / 3        
        # feet to m: m = ft / 3.281
        m = num / 3.281        
        # feet to km: km = ft / 3281
        km = num / 3281        
        # feet to mi: mi = ft / 5280
        mi = num / 5280        
        print(f"{num} foot/feet is {mm:.2f} millimeters")
        print(f"{num} foot/feet is {cm:.2f} centimeters")
        print(f"{num} foot/feet is {inches:.2f} inches")
        print(f"{num} foot/feet is {m:.4f} meters")
        print(f"{num} foot/feet is {yards:.4f} yards")
        print(f"{num} foot/feet is {km:.8f} kilometers")
        print(f"{num} foot/feet is {mi:.8f} miles")
        print("******************************")     
    elif unit.lower() == "yard":
        # yards to mm: mm = yards * 914.4
        mm = num * 914.4        
        # yards to cm: cm = yards * 91.44
        cm = num * 91.44        
        # yards to inches: inches = yards * 36
        inches = num * 36        
        # yards to feet: feet = yards * 3
        feet = num * 3        
        # yards to m: m = yards / 1.094
        m = num / 1.094        
        # yards to km: km = yards / 1094
        km = num / 1094        
        # yards to mi: mi = yards / 1760
        mi = num /1760        
        print(f"{num} yard(s) is {mm:.2f} millimeters")
        print(f"{num} yard(s) is {cm:.2f} centimeters")
        print(f"{num} yard(s) is {inches:.2f} inches")
        print(f"{num} yard(s) is {feet:.4f} feet")
        print(f"{num} yard(s) is {m:.4f} meters")
        print(f"{num} yard(s) is {km:.8f} kilometers")
        print(f"{num} yard(s) is {mi:.8f} miles")
        print("******************************")   
    elif unit.lower() == "m":
        # m to mm: mm = m * 1000
        mm = num * 1000
        # m to cm: cm = m * 100
        cm = num * 100
        # m to inches: inches = m * 39.37
        inches = num * 39.37
        # m to feet: feet = m * 3.281
        feet = num * 3.281
        # m to yards: yards = m * 1.094
        yards = num * 1.094
        # m to km: km = m / 1000
        km = num / 1000
        # m to mi: mi = m / 1609
        mi = num / 1609
        print(f"{num} meter(s) is {mm:.2f} millimeters")
        print(f"{num} meter(s) is {cm:.2f} centimeters")
        print(f"{num} meter(s) is {inches:.2f} inches")
        print(f"{num} meter(s) is {feet:.4f} feet")
        print(f"{num} meter(s) is {yards:.4f} yards")
        print(f"{num} meter(s) is {km:.8f} kilometers")
        print(f"{num} meter(s) is {mi:.8f} miles")
        print("******************************")
    elif unit.lower() == "km":
        # km to mm: mm = km * 1,000,000
        mm = num * 1000000        
        # km to cm: cm = km * 100,000
        cm = num * 100000        
        # km to inches: inches = km * 39,370.1
        inches = num * 39370.1        
        # km to feet: feet = km * 3280.84
        feet = num * 3280.84        
        # km to m: m = km * 1000
        m = num * 1000        
        # km to yards: yards = km * 1093.61
        yards = num * 1093.61        
        # km to mi: mi = km / 1.609
        mi = num / 1.609        
        print(f"{num} kilometer(s) is {mm:.2f} millimeters")
        print(f"{num} kilometer(s) is {cm:.2f} centimeters")
        print(f"{num} kilometer(s) is {inches:.2f} inches")
        print(f"{num} kilometer(s) is {feet:.4f} feet")
        print(f"{num} kilometer(s) is {m:.4f} meters")
        print(f"{num} kilometer(s) is {yards:.4f} yards")
        print(f"{num} kilometer(s) is {mi:.6f} miles")
        print("******************************")
    elif unit.lower() == "mi":
        # miles to mm: mm = mi * 1,609,344
        mm = num * 1609344        
        # miles to cm: cm = mi * 160934.4
        cm = num * 160934.4        
        # miles to inches: inches = mi * 63,360
        inches = num * 63360        
        # miles to feet: feet = mi * 5280
        feet = num * 5280        
        # miles to m: m = mi * 1609.344
        m = num * 1609.344        
        # miles to yards: yards = mi * 1760
        yards = num * 1760        
        # miles to km: km = mi * 1.609
        km = num * 1.609        
        print(f"{num} mile(s) is {mm:.2f} millimeters")
        print(f"{num} mile(s) is {cm:.2f} centimeters")
        print(f"{num} mile(s) is {inches:.2f} inches")
        print(f"{num} mile(s) is {feet:.4f} feet")
        print(f"{num} mile(s) is {m:.4f} meters")
        print(f"{num} mile(s) is {yards:.4f} yards")
        print(f"{num} mile(s) is {km:.6f} kilometers")
        print("******************************")
    else:
        print("Please enter a valid unit")



"""
# test data

convert_temp(0, "F")
convert_temp(0, "C")
convert_temp(273.15, "K")

convert_temp("test", "test")


convert_length(1, "mm")
convert_length(1, "cm")
convert_length(1, "inches")
convert_length(1, "feet")
convert_length(1, "yard")
convert_length(1, "m")
convert_length(1, "km")
convert_length(1, "mi")

convert_length(1, "test")
convert_length("test", "mm")
convert_length("test", "test")



"""
















