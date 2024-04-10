"""Menu Maker -Add_Combo- V1
Allows user to add combos to the current menu
"""

import easygui

# default list
menu = {"Value": {"Beef Burger": {5.69}, "Fries": {1.00}, "Fizzy "
                                                          "drink": {1.00}},
        "Cheezy": {"Cheeseburger": {6.69},
                   "Fries": {1.00}, "Fizzy Drink": {1.00}}, "Super": {
        "Cheeseburger": {6.69}, "Larger fries": {2.00}, "Smoothie":
            {2.00}}}
# simplified options
options = easygui.buttonbox("Would you like to", choices=["Add combo",
                                                          "Find combo",
                                                          "Delete combo",
                                                          "Output all",
                                                          "Exit"])
if options == "Add combo":
    # makes dictionary for tha combo
    combo = easygui.enterbox("Enter the name of the combo you would like to "
                             "add")
    menu[combo] = {}
    # adds food
    food = easygui.enterbox("Please enter a food for this combo")
    menu[combo] = food
    # adds price
    price = easygui.enterbox("Please enter a price for this food")
    menu[combo][food] = price
    # asks if use wants to add another food
    while True:
        end_add = easygui.buttonbox("Would you like to add another food?",
                                    choices=["Yes", "No"])
        if end_add == "Yes":
            # adds food
            food = easygui.enterbox("Please enter a food for this combo")
            menu[combo] = food
            # adds price of food
            price = easygui.enterbox("Please enter a price for this food")
            menu[combo][food] = price
        elif end_add == "No":
            break
elif options == "Find combo":
    print("find combo")
elif options == "Delete combo":
    print("Delete combo")
elif options == "Output all":
    print("Output all")
elif options == "Exit":
    print("Goodbye")
