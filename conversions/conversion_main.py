# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:21:14 2023

@author: collin
"""

from conversions import convert_temp, convert_length
from conversions import *

def display_main_menu():
    
    # MAIN MENU
    menu_string = "MAIN MENU"
    menu_bar_length = 50
    num_asterisks = (menu_bar_length - len(menu_string)) // 2
    
    print()
    print("*"*num_asterisks, menu_string, "*"*num_asterisks)
    print()
    print("\t\tPlease choose an option")
    print("\t\t1. Convert Temperature")
    print("\t\t2. Convert Length")
    print("\t\t3. Convert Weight")
    print("\t\t4. Convert Area")
    print("\t\t5. Exit")
    
def display_temp_menu():
    
    menu_string = "CONVERT TEMPERATURE"
    menu_bar_length = 50
    num_asterisks = (menu_bar_length - len(menu_string)) // 2
    
    print()
    print("*"*num_asterisks, menu_string, "*"*num_asterisks)
    print()
    print("\t\tPlease choose a starting unit")
    print("\t\t1. Fahrenheit")
    print("\t\t2. Celsius")
    print("\t\t3. Kelvin")
    print("\t\t4. Exit")
    
def display_length_menu():
    
    menu_string = "CONVERT LENGTH"
    menu_bar_length = 50
    num_asterisks = (menu_bar_length - len(menu_string)) // 2
    
    print()
    print("*"*num_asterisks, menu_string, "*"*num_asterisks)
    print()
    print("\t\tPlease choose a starting unit")
    print("\t\t1. Millimeters")
    print("\t\t2. Centimeters")
    print("\t\t3. Inches")
    print("\t\t4. Feet")
    print("\t\t5. Yards")
    print("\t\t6. Meters")
    print("\t\t7. Kilometers")
    print("\t\t8. Miles")
    print("\t\t9. Exit")
    

def menu_valid_selection(choice):
    menu_options = [1, 2, 3, 4, 5]
    try:
        choice = int(choice)
        if choice in menu_options:
            return True
        else:
            return False
    except ValueError:
        return False
    
def temp_valid_selection(choice):
    temp_menu_options = [1, 2, 3, 4]
    try:
        choice = int(choice)
        if choice in temp_menu_options:
            return True
        else:
            return False
    except ValueError:
        return False
    
def length_valid_selection(choice):
    length_menu_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        choice = int(choice)
        if choice in length_menu_options:
            return True
        else:
            return False
    except ValueError:
        return False

    
def print_invalid_message():
    print("\n\t\t\t*****INVALID INPUT*****")
    
        
        

while True:
    
    display_main_menu()
    
    choice = input("\t\tOption: ")
    if not menu_valid_selection(choice):
        print_invalid_message()
        continue
    
    choice = int(choice)
    
    ###################### CONVERT TEMP ##############################
    if choice == 1:
        display_temp_menu()
        unit_choice = input("\t\tOption: ")
        if not temp_valid_selection(unit_choice):
            print_invalid_message()
            continue
        
        # DEGREES FAHRENHEIT
        if int(unit_choice) == 1: 
            num = input("\t\tPlease enter degrees Fahrenheit: ")        
            try:
                num = float(num)
                convert_temp(num, "F")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
        
        # DEGREES CELSIUS
        if int(unit_choice) == 2:
            num = input("\t\tPlease enter degrees Celsius: ")        
            try:
                num = float(num)
                convert_temp(num, "C")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # KELVIN
        if int(unit_choice) == 3:
            num = input("\t\tPlease enter temperature in Kelvin: ")        
            try:
                num = float(num)
                convert_temp(num, "K")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # EXIT        
        if int(unit_choice) == 4:
            print("Terminating program...")
            break
        
    ##################################################################
    
    ###################### CONVERT LENGTH ##############################
    if choice == 2:
        display_length_menu()
        unit_choice = input("\t\tOption: ")
        if not length_valid_selection(unit_choice):
            print_invalid_message()
            continue
        
        # MILLIMETERS
        if int(unit_choice) == 1: 
            num = input("\t\tPlease enter length in millimeters: ")        
            try:
                num = float(num)
                convert_length(num, "mm")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # CENTIMETERS
        if int(unit_choice) == 2: 
            num = input("\t\tPlease enter length in centimeters: ")        
            try:
                num = float(num)
                convert_length(num, "cm")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # INCHES
        if int(unit_choice) == 3: 
            num = input("\t\tPlease enter length in inches: ")        
            try:
                num = float(num)
                convert_length(num, "inches")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # FEET
        if int(unit_choice) == 4: 
            num = input("\t\tPlease enter length in feet: ")        
            try:
                num = float(num)
                convert_length(num, "feet")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # YARDS
        if int(unit_choice) == 5: 
            num = input("\t\tPlease enter length in yards: ")        
            try:
                num = float(num)
                convert_length(num, "yard")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # METERS
        if int(unit_choice) == 6: 
            num = input("\t\tPlease enter length in meters: ")        
            try:
                num = float(num)
                convert_length(num, "m")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # KILOMETERS
        if int(unit_choice) == 7: 
            num = input("\t\tPlease enter length in kilometers: ")        
            try:
                num = float(num)
                convert_length(num, "km")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # MILES
        if int(unit_choice) == 8: 
            num = input("\t\tPlease enter length in miles: ")        
            try:
                num = float(num)
                convert_length(num, "mi")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    print("Terminating program...")
                    break
            except ValueError:
                print_invalid_message()
                
        # EXIT        
        if int(unit_choice) == 9:
            print("Terminating program...")
            break
        
        ##################################################################
        
    print("Terminating program...")
    break


"""
 or int(choice) in menu_options
 
        if int(unit_choice) == 1:
            num = input("\t\tPlease enter degrees Fahrenheit: ")
            try:                
                num = int(num)
                convert_temp(num, "F")
                continue_option = input("\t\tContinue? (y/n): ")
                if continue_option.lower() == "y":
                    continue
                else:
                    break
            except ValueError:
                if not isinstance(num, float):
                    print_invalid_message_temp()

"""