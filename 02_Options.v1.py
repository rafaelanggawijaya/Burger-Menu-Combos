"""Menu Maker -Options- V1
Gives options for the user to pick to do things in menu maker"""

import easygui


# welcome statement
easygui.msgbox("Welcome To Menu Maker")
options = easygui.buttonbox("Would you like to", choices=["Add combo",
                                                          "Find combo",
                                                          "Delete combo",
                                                          "Output all",
                                                          "Exit"])
if options == "Add combo":
    print("Add combo")
elif options == "Find combo":
    print("find combo")
elif options == "Delete combo":
    print("Delete combo")
elif options == "Output all":
    print("Output all")
elif options == "Exit":
    print("Goodbye")
