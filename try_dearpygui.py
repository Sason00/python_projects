from dearpygui.dearpygui import *

show_debug()
add_button("Add Buttons", callback="addButtons")
add_button("Delete Buttons", callback="deleteButtons")
add_window("Secondary Window")
end_window()

def addButtons(sender, data):
    add_button("New Button")
    add_button("New Button 2", parent="Secondary Window")


def deleteButtons(sender, data):
    delete_item("New Button")
    delete_item("New Button 2")


start_dearpygui() 