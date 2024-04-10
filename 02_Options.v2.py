"""Menu Maker -Options- V2
Gives options for the user to pick to do things in menu maker
Update: Turned it into a function"""

import easygui


def option():
    easygui.msgbox("Welcome To Menu Maker")
    options = easygui.buttonbox("Would you like to", choices=["Add combo",
                                                              "Find combo",
                                                              "Delete combo",
                                                              "Output all",
                                                              "Exit"])
    if options == "Add combo":
        return "Add combo"
    elif options == "Find combo":
        return "Find combo"
    elif options == "Delete combo":
        return "Delete combo"
    elif options == "Output all":
        return "Output all"
    elif options == "Exit":
        return "Exit"


# main routine

answer = option()
if answer == "Add combo":
    print("Add combo")
elif answer == "Find combo":
    print("find combo")
elif answer == "Delete combo":
    print("Delete combo")
elif answer == "Output all":
    print("Output all")
elif answer == "Exit":
    print("Goodbye")
