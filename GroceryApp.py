class Grocery_Item:
  def __init__(self, name, cost, quantity):
    self.name = name
    self.cost = cost
    self.quantity = quantity


class Grocery_List:
  def __init__(self, list_name, list_address):
    self.list_name = list_name
    self.list_address = list_address
    self.list_items = []

  def add_item(self, new_item):
    self.list_items.append(new_item)

  def remove_item(self, removed_item):
    try:
      self.list_items[removed_item]
    except:
      print("item not found")
    else:
      del self.list_items[removed_item]
      

def check_item_int(input, error_message = ""):
  output = False
  try:
    float(input)
  except:
    print(error_message)
  else:
    output = True
  return output

def display_list(list, list_item_divider):
  print(list.list_name)
  print(list_item_divider)
  for index in range(0, len(list.list_items)):
    print(f"{index + 1}: {list.list_items[index].name} - costs: ${list.list_items[index].cost} - amount wanted: {list.list_items[index].quantity}")
    print(list_item_divider)

def edit_list(list, edit_keys, item_divider):
  
  finished_editing = False
  while finished_editing == False:
    main_input = input(f"Do you want to add or remove items from the shopping list?\n {edit_keys[0]} - add\n {edit_keys[1]} - remove\n exit - exit \n")
    if main_input == edit_keys[0]:
      new_item_name = input("What is this item's name? ")
      
      while True:
        new_item_cost = input("What is this item's cost? ")
        if check_item_int(new_item_cost, "You must input a number"):
          float(new_item_cost)
          break
      while True:
        new_item_quantity = input("How much of the item do you want to get? ")
        if check_item_int(new_item_quantity, "You must input a number"):
          float(new_item_quantity)
          break
      
      list.add_item(Grocery_Item(new_item_name, new_item_cost, new_item_quantity))
      display_list(list, item_divider)
    elif main_input == edit_keys[1]:
        display_list(list, item_divider)
        while True:
          selected_item = input("Which item do you want to delete? ")
          if check_item_int(selected_item, "Please enter the number of the item you want to delete\n"):
            selected_item = int(selected_item)
            break
        list.remove_item((selected_item - 1))
    if main_input == "exit":
      finished_editing = True
  


def new_list_menu(menu_divider, edit_keys, item_divider, list_holder):
  print(menu_divider)
  valid_name = False
  while valid_name == False:
    new_list_name = input("What do you want to name the new list? \n")
    if new_list_name in list_holder:
      print("That shopping list name is already used.")
    else:
      valid_name = True
  new_list_address = input("What is the store's address? \n")
  
  new_position = len(list_holder)
  list_holder.append(Grocery_List(new_list_name, new_list_address))
  display_list(list_holder[new_position], item_divider)
  edit_list(list_holder[new_position], edit_keys, item_divider)

def delete_list(list_holder, divider, exit_keys):
  wants_to_leave = False
  while wants_to_leave == False:
    
    display_list_of_lists(list_holder, divider)
    selected_list = input("which shopping list do you want to delete?\n")
    for index in range(0, len(list_holder)):
      if selected_list == list_holder[index].list_name:
        del list_holder[index]
    display_list_of_lists(list_holder, divider)
    if len(list_holder) > 0:
      new_input = int(input(f"Do you want to continue deleting shopping lists?\n {exit_keys[0]} to continue \n {exit_keys[1]} to stop deleting"))
      if new_input.lower == exit_keys[0].lower():
        wants_to_leave = True
      elif new_input.lower == exit_keys[1].lower():
        wants_to_leave = False
    else:
      print("There are no more shopping lists to delete")
      wants_to_leave = True
    

def display_list_of_lists(lists, divider):
  print(divider)
  for item in lists:
    print(item.list_name)
  print(divider)