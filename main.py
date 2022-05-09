from GroceryApp import *

menu_divider = "***************"
list_item_divider = "---------------"

menu_keys = {"Make new list": "1",
             "Edit list": "2",
             "Add to list": "1",
             "Remove from list": "2",
             "Destroy list": "3",
             "Display list": "3",
             "Close Program": "q"}

main_menu_string = f"GROCERY LIST PROGRAM \n What would you like to do? \n {menu_keys['Make new list']}: Make a new list \n {menu_keys['Edit list']}: Edit an existing list \n {menu_keys['Display list']}: Display a list \n {menu_keys['Close Program']}: Close the program \n"


exit_key = "y"


grocery_lists = []


#Menus



#Execution

while True:
  print(menu_divider)
  start_input = input(main_menu_string)
  if start_input == menu_keys["Make new list"]:
    new_list_menu(menu_divider, exit_key, [menu_keys["Add to list"], menu_keys["Remove from list"]], list_item_divider, grocery_lists)
  elif start_input == menu_keys["Edit list"]:
    display_list_of_lists(grocery_lists, menu_divider)
    wanted_list = input("What shopping list do you want to edit? ")
    for index in range(0, len(grocery_lists)):
      if grocery_lists[index].list_name == wanted_list:
        edit_list(grocery_lists[index], exit_key, [menu_keys["Add to list"], menu_keys["Remove from list"]], list_item_divider)
  elif start_input == menu_keys["Display list"]:
    for list in grocery_lists:
      print(menu_divider)
      display_list(list, list_item_divider)
  elif start_input == menu_keys["Close Program"]:
    break
    