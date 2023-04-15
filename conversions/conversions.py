# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:17:03 2023

@author: collin
"""

def convert_temp(num, unit):
    if not isinstance(num, (int, float)):
        print("Please enter a valid number")
        return
    
    print("*"*50)
    if unit.upper() == "F":
        # F to C:   C = (F - 32) * (5/9)
        celsius = (num - 32) * (5/9)
        # F to K:   K = (F - 32) * (5/9) + 273.15
        kelvin = celsius + 273.15
        # results rounded with round() function
        print(num, "degree(s) Fahrenheit is ", round(celsius,2), "degrees Celsius")
        print(num, "degree(s) Fahrenheit is ", round(kelvin,2) , "Kelvin")
        print("*"*50)
    elif unit.upper() == "C":
        # C to F:   F = (9/5) * C + 32 or F = (1.8 * C) + 32
        fahrenheit = (1.8 * num) + 32
        # C to K:   K = C + 273.15
        kelvin = num + 273.15
        # results rounded with 'f' format specifier
        print(f"{num} degree(s) Celsius is {fahrenheit:.2f} degrees Fahrenheit")
        print(f"{num} degree(s) Celsius is {kelvin:.2f} Kelvin")
        print("*"*50)
    elif unit.upper() == "K":
        # K to C:   C = K - 273.15
        celsius = num - 273.15
        # K to F:   F = (K - 273.15) * (9/5) + 32 or F = 1.8 * (K - 273.15) + 32
        fahrenheit = 1.8 * (num - 273.15) + 32
        print(f"{num} Kelvin is {celsius:.2f} degrees Celsius")
        print(f"{num} Kelvin is {fahrenheit:.2f} degrees Fahrenheit")
        print("*"*50)
    # will need to add else statement to check for exception
    else:
        print("Please add a valid number/unit")
        
def convert_length(num, unit):
    if not isinstance(num, (int, float)):
        print("Please enter a valid number")
        return
    
    print("*"*50)
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
        print("*"*50) 
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
        print("*"*50)
    elif unit.lower() == "inches":
        # inches to mm:    in * 25.4
        mm = num * 25.4
    	# inches to cm:    in * 2.54
        cm = num * 2.54        
        # inches to ft:    in / 12
        feet = num / 12        
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
        print("*"*50)        
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
        print("*"*50)     
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
        print("*"*50)   
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
        print("*"*50)
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
        print("*"*50)
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
        print("*"*50)
    else:
        print("Please enter a valid unit")

def convert_weight(num, unit):
    if not isinstance(num, (int, float)):
        print("Please enter a valid number")
        return
    
    print("*"*50)
    if unit.lower() == "mg":
        # mg to g: g = mg / 1000
        g = num / 1000
        # mg to oz: oz = mg / 28350
        oz = num / 28350
        # mg to lbs: lbs = mg / 453600
        lbs = num / 453600
        # mg to kg: kg = mg / 1e+6 or mg / 1,000,000
        kg = num / 1000000
        # mg to stone: stone = mg / 6,350,000
        stone = num / 6350000
        # mg to ton: ton = mg / 907,200,000
        ton = num / 907200000
        print(f"{num} milligram(s) is {g:.6f} grams")
        print(f"{num} milligram(s) is {oz:.9f} ounces")
        print(f"{num} milligram(s) is {lbs:.9f} pounds")
        print(f"{num} milligram(s) is {kg:.9f} kilograms")
        print(f"{num} milligram(s) is {stone:.9f} stone")
        print(f"{num} milligram(s) is {ton:.12f} tons")
        print("*"*50)
    elif unit.lower() == "g":
        # g to mg: mg = g * 1000
        mg = num * 1000
        # g to oz: oz = g / 28.35
        oz = num / 28.35
        # g to lbs: lbs = g / 453.592
        lbs = num / 453.592
        # g to kg: kg = g / 1000
        kg = num / 1000
        # g to stone: stone = g / 6350.293
        stone = num / 6350.293
        # g to ton: ton = g / 907200
        ton = num / 907200
        print(f"{num} gram(s) is {mg:.2f} milligrams")
        print(f"{num} gram(s) is {oz:.6f} ounces")
        print(f"{num} gram(s) is {lbs:.6f} pounds")
        print(f"{num} gram(s) is {kg:.6f} kilograms")
        print(f"{num} gram(s) is {stone:.6f} stone")
        print(f"{num} gram(s) is {ton:.9f} tons")
        print("*"*50)     
    elif unit.lower() == "oz":
        # oz to mg: mg = oz * 28349.523
        mg = num * 28349.523
        # oz to g: g = oz * 28.35
        g = num * 28.35
        # oz to lbs: lbs = oz / 16
        lbs = num / 16
        # oz to kg: kg = oz / 35.274
        kg = num / 35.274
        # oz to stone: stone = oz / 224
        stone = num / 224
        # oz to ton: ton = oz / 32000
        ton = num / 32000
        print(f"{num} ounce(s) is {mg:.2f} milligrams")
        print(f"{num} ounce(s) is {g:.2f} grams")
        print(f"{num} ounce(s) is {lbs:.6f} pounds")
        print(f"{num} ounce(s) is {kg:.6f} kilograms")
        print(f"{num} ounce(s) is {stone:.6f} stone")
        print(f"{num} ounce(s) is {ton:.9f} tons")
        print("*"*50)  
    elif unit.lower() == "lbs":
        # lbs to mg: mg = lbs * 453592
        mg = num * 453592
        # lbs to g: g = lbs * 453.592
        g = num * 453.592
        # lbs to oz: oz = lbs * 16
        oz = num * 16
        # lbs to kg: kg = lbs / 2.205
        kg = num / 2.205
        # lbs to stone: stone = lbs / 14
        stone = num / 14
        # lbs to ton: ton = lbs / 2000
        ton = num / 2000
        print(f"{num} pound(s) is {mg:.2f} milligrams")
        print(f"{num} pound(s) is {g:.2f} grams")
        print(f"{num} pound(s) is {oz:.2f} ounces")
        print(f"{num} pound(s) is {kg:.6f} kilograms")
        print(f"{num} pound(s) is {stone:.6f} stone")
        print(f"{num} pound(s) is {ton:.9f} tons")
        print("*"*50)
    elif unit.lower() == "kg":
        # kg to mg: mg = kg * 1e+6 or kg * 1,000,000
        mg = num * 1000000
        # kg to g: g = kg * 1000
        g = num * 1000
        # kg to oz: oz = kg * 35.274
        oz = num * 35.274
        # kg to lbs: lbs = kg * 2.205
        lbs = num * 2.205
        # kg to stone: stone = kg * 0.157
        stone = num * 0.157
        # kg to ton: ton = kg / 902.7
        ton = num / 907.2
        print(f"{num} kilogram(s) is {mg:.2f} milligrams")
        print(f"{num} kilogram(s) is {g:.2f} grams")
        print(f"{num} kilogram(s) is {oz:.2f} ounces")
        print(f"{num} kilogram(s) is {lbs:.6f} pounds")
        print(f"{num} kilogram(s) is {stone:.6f} stone")
        print(f"{num} kilogram(s) is {ton:.9f} tons")
        print("*"*50) 
    elif unit.lower() == "stone":
        # stone to mg: mg = stone * 6,350,290
        mg = num * 6350290
        # stone to g: g = stone * 6350.29
        g = num * 6350.29
        # stone to oz: oz = stone * 224
        oz = num * 224
        # stone to lbs: lbs = stone * 14
        lbs = num * 14
        # stone to kg: kg = stone * 6.35029
        kg = num * 6.35029
        # stone to ton: ton = stone / 142.9
        ton = num / 142.9
        print(f"{num} stone(s) is {mg:.2f} milligrams")
        print(f"{num} stone(s) is {g:.2f} grams")
        print(f"{num} stone(s) is {oz:.2f} ounces")
        print(f"{num} stone(s) is {lbs:.5f} pounds")
        print(f"{num} stone(s) is {kg:.5f} kilograms")
        print(f"{num} stone(s) is {ton:.5f} tons")
        print("*"*50) 
    elif unit.lower() == "ton":
        # ton to mg: mg = ton * 907200000
        mg = num * 907200000
        # ton to g: g = ton * 907185
        g = num * 907185
        # ton to oz: oz = ton * 32000
        oz = num * 32000
        # ton to lbs: lbs = ton * 2000
        lbs = num * 2000
        # ton to kg: kg = ton * 907.185
        kg = num * 907.185
        # ton to stone: stone = ton * 142.857
        stone = num * 142.857
        print(f"{num} ton(s) is {mg:.2f} milligrams")
        print(f"{num} ton(s) is {g:.2f} grams")
        print(f"{num} ton(s) is {oz:.2f} ounces")
        print(f"{num} ton(s) is {lbs:.2f} pounds")
        print(f"{num} ton(s) is {kg:.2f} kilograms")
        print(f"{num} ton(s) is {stone:.2f} stones")
        print("*"*50)
    else:
        print("Please enter a valid unit")

def convert_area(num, unit):
    if not isinstance(num, (int, float)):
        print("Please enter a valid number")
        return
    
    print("*"*50)
    if unit.lower() == "sq ft":
        # sq ft to sq m: sq m = sq ft / 10.764
        sq_m = num / 10.764
        # sq ft to acre: acre = sq ft / 43560
        acre = num / 43560
        # sq ft to hectare: hectare = sq ft / 107639
        hectare = num / 107639
        # sq ft to sq km: sq km = sq ft / 1.076e+7 or sq ft / 10,763,910
        sq_km = num / 10763910
        # sq ft to sq mile: sq mile = sq ft / 2.788e+7 or sq ft / 27,878,400
        sq_mile = num / 27878400
        print(f"{num} square foot/feet is {sq_m:.6f} square meters")
        print(f"{num} square foot/feet is {acre:.9f} acres")
        print(f"{num} square foot/feet is {hectare:.12f} hectares")
        print(f"{num} square foot/feet is {sq_km:.12f} square kilometers")
        print(f"{num} square foot/feet is {sq_mile:.12f} square miles")
        print("*"*50)
    elif unit.lower() == "sq m":
        # sq m to sq ft: sq ft = sq m * 10.764
        sq_ft = num * 10.764
        # sq m to acre: acre = sq m / 4047
        acre = num / 4047
        # sq m to hectare: hectare = sq m / 10000
        hectare = num / 10000
        # sq m to sq km: sq km = sq m / 1e+6 or sq m / 1,000,000
        sq_km = num / 1000000
        # sq m to sq mile: sq mile = sq m / 2.59e+6 or sq m / 2,589,988
        sq_mile = num / 2589988
        print(f"{num} square meter(s) is {sq_ft:.6f} square feet")
        print(f"{num} square meter(s) is {acre:.8f} acres")
        print(f"{num} square meter(s) is {hectare:.8f} hectares")
        print(f"{num} square meter(s) is {sq_km:.12f} square kilometers")
        print(f"{num} square meter(s) is {sq_mile:.12f} square miles")
        print("*"*50)   
    elif unit.lower() == "acre":
        # acre to sq ft: sq ft = acre * 43,560
        sq_ft = num * 43560
        # acre to sq m: sq m = acre * 4047
        sq_m = num * 4047
        # acre to hectare: hectare = acre / 2.471
        hectare = num / 2.471
        # acre to sq km: sq km = acre / 247.105
        sq_km = num / 247.105
        # acre to sq mile: sq mile = acre / 640
        sq_mile = num / 640
        print(f"{num} acre(s) is {sq_ft:.4f} square feet")
        print(f"{num} acre(s) is {sq_m:.4f} square meters")
        print(f"{num} acre(s) is {hectare:.4f} hectares")
        print(f"{num} acre(s) is {sq_km:.8f} square kilometers")
        print(f"{num} acre(s) is {sq_mile:.8f} square miles")
        print("*"*50)
    elif unit.lower() == "hectare":
        # hectare to sq ft: sq ft = hectare * 107639.105
        sq_ft = num * 107639.105
        # hectare to sq m: sq m = hectare * 10000
        sq_m = num * 10000
        # hectare to acre: acre = hectare * 2.471
        acre = num * 2.471
        # hectare to sq km: sq km = hectare / 100
        sq_km = num / 100
        # hectare to sq mile: sq mile = hectare / 259
        sq_mile = num / 259
        print(f"{num} hectare(s) is {sq_m:.4f} square meters")
        print(f"{num} hectare(s) is {sq_ft:.4f} square feet")
        print(f"{num} hectare(s) is {acre:.4f} acres")
        print(f"{num} hectare(s) is {sq_km:.4f} square kilometers")
        print(f"{num} hectare(s) is {sq_mile:.8f} square miles")
        print("*"*50)
    elif unit.lower() == "sq km":
        # sq km to sq ft: sq ft = sq km * 10763910.41671
        sq_ft = num * 10763910.41671
        # sq km to sq m: sq m = sq km * 1e+6 or sq km * 1,000,000
        sq_m = num * 1000000
        # sq km to acre: acre = sq km * 247.1053814672
        acre = num * 247.1053814672
        # sq km to hectare: hectare = sq km * 100
        hectare = num * 100        
        # sq km to sq mile: sq mile = sq km / 2.59
        sq_mile = num / 2.59
        print(f"{num} square kilometer(s) is {sq_ft:.4f} square feet")
        print(f"{num} square kilometer(s) is {sq_m:.4f} square meters")
        print(f"{num} square kilometer(s) is {acre:.4f} acres")
        print(f"{num} square kilometer(s) is {hectare:.4f} hectares")
        print(f"{num} square kilometer(s) is {sq_mile:.4f} square miles")
        print("*"*50)
    elif unit.lower() == "sq mile":
        # sq mile to sq ft: sq ft = sq mile * 2.788e+7 or sq mile * 27,878,400
        sq_ft = num * 27878400
        # sq mile to sq m: sq m = sq mile * 2.59e+6 or sq mile * 2,589,988
        sq_m = num * 2589988
        # sq mile to acre: acre = sq mile * 640
        acre = num * 640
        # sq mile to hectare: hectare = sq mile * 258.999
        hectare = num * 258.999
        # sq mile to sq km: sq km = sq mile * 2.59
        sq_km = num * 2.59
        print(f"{num} square mile(s) is {sq_ft:.4f} square feet")
        print(f"{num} square mile(s) is {acre:.4f} acres")
        print(f"{num} square mile(s) is {hectare:.4f} hectares")
        print(f"{num} square mile(s) is {sq_km:.4f} square kilometers")
        print(f"{num} square mile(s) is {sq_m:.4f} square meters")
        print("*"*50)
    else:
        print("Please enter a valid unit")
        
def convert_currency(num, unit):
    if not isinstance(num, (int, float)):
        print("Please enter a valid number")
        return

    print("*"*50)
    
    # currency conversion rates as of 4/15/2023
    if unit.lower() == "usd":
        euro = num * 0.83
        yen = num * 110.32
        pound = num * 0.72
        aud = num * 1.25
        cad = num * 1.25
        franc = num * 0.91
        renminbi = num * 6.38
        baht = num * 31.35
        mxn = num * 19.95
        inr = num * 75.21
        
        print(f"{num} US dollar(s) is {euro:.2f} Euros")
        print(f"{num} US dollar(s) is {yen:.2f} Japanese yen")
        print(f"{num} US dollar(s) is {pound:.2f} British pounds")
        print(f"{num} US dollar(s) is {aud:.2f} Australian dollars")
        print(f"{num} US dollar(s) is {cad:.2f} Canadian dollars")
        print(f"{num} US dollar(s) is {franc:.2f} Swiss francs")
        print(f"{num} US dollar(s) is {renminbi:.2f} Chinese renminbis")
        print(f"{num} US dollar(s) is {baht:.2f} Thai baht")
        print(f"{num} US dollar(s) is {mxn:.2f} Mexican pesos")
        print(f"{num} US dollar(s) is {inr:.2f} Indian rupees")
        
    elif unit.lower() == "euro":
        usd = num * 1.21
        yen = num * 128.26
        pound = num * 0.84
        aud = num * 1.45
        cad = num * 1.45
        franc = num * 1.06
        renminbi = num * 7.41
        baht = num * 36.45
        mxn = num * 23.20
        inr = num * 87.28
    
        print(f"{num} Euro(s) is {usd:.2f} US dollars")
        print(f"{num} Euro(s) is {yen:.2f} Japanese yen")
        print(f"{num} Euro(s) is {pound:.2f} British pounds")
        print(f"{num} Euro(s) is {aud:.2f} Australian dollars")
        print(f"{num} Euro(s) is {cad:.2f} Canadian dollars")
        print(f"{num} Euro(s) is {franc:.2f} Swiss francs")
        print(f"{num} Euro(s) is {renminbi:.2f} Chinese renminbis")
        print(f"{num} Euro(s) is {baht:.2f} Thai baht")
        print(f"{num} Euro(s) is {mxn:.2f} Mexican pesos")
        print(f"{num} Euro(s) is {inr:.2f} Indian rupees")
        
    elif unit.lower() == "yen":
        euro = num / 132.68
        usd = num / 110.32
        pound = num / 153.76
        aud = num / 88.26
        cad = num / 87.45
        franc = num / 120.7
        renminbi = num / 17.28
        baht = num / 3.58
        mxn = num / 5.53
        inr = num / 1.49
    
        print(f"{num} Japanese yen(s) is {euro:.2f} Euros")
        print(f"{num} Japanese yen(s) is {usd:.2f} US dollars")
        print(f"{num} Japanese yen(s) is {pound:.2f} British pounds")
        print(f"{num} Japanese yen(s) is {aud:.2f} Australian dollars")
        print(f"{num} Japanese yen(s) is {cad:.2f} Canadian dollars")
        print(f"{num} Japanese yen(s) is {franc:.2f} Swiss francs")
        print(f"{num} Japanese yen(s) is {renminbi:.2f} Chinese renminbis")
        print(f"{num} Japanese yen(s) is {baht:.2f} Thai baht")
        print(f"{num} Japanese yen(s) is {mxn:.2f} Mexican pesos")
        print(f"{num} Japanese yen(s) is {inr:.2f} Indian rupees")

        
    



    # Add more conversion rates for other currencies here

    else:
        print("Currency not supported")

    print("*"*50)


convert_currency(1, "usd")
convert_currency(1, "euro")
convert_currency(1, "yen")


"""

def convert_capacity:
    
def convert_currency:
    
def convert_storage:
    
def convert_time:
    
    
    

# test data

convert_temp(0, "F")
convert_temp(0, "C")
convert_temp(273.15, "K")

convert_temp(1, "test")
convert_temp("test", "F")
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


convert_weight(1, "mg")
convert_weight(1, "g")
convert_weight(1, "oz")
convert_weight(1, "lbs")
convert_weight(1, "kg")
convert_weight(1, "stone")
convert_weight(1, "ton")

convert_weight(1, "test")
convert_weight("test", "mg")
convert_weight("test", "test")

convert_area(1, "sq ft")
convert_area(1, "sq m")
convert_area(1, "acre")
convert_area(1, "hectare")
convert_area(1, "sq km")
convert_area(1, "sq mile")

convert_area(1, "test")
convert_area("test", "sq mile")
convert_area("test", "test")


"""
















