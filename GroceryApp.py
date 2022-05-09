class Grocery_Item:
  def __init__(self, name, cost, quantity):
    self.name = name
    self.cost = cost
    self.quantity = quantity


class Grocery_List:
  def __init__(self, list_name):
    self.list_name = list_name
    self.list_items = []

  def add_item(self, new_item):
    self.list_items.append(new_item)

  def remove_item(self, removed_item):
    if removed_item in self.list_items:
      del self.list_items[self.list_items.index(removed_item)]

def display_list(list, list_item_divider):
  print(list.list_name)
  print(list_item_divider)
  for item in list.list_items:
    print(f" {item.name} - ${item.cost} - {item.quantity}")
    print(list_item_divider)

def edit_list(list, exit_key, edit_keys, item_divider):
  
  finished_editing = False
  while finished_editing == False:
    main_input = input(f"Do you want to add or remove items from the shopping list?\n {edit_keys[0]} - add\n {edit_keys[1]} - remove\n exit - exit \n")
    if main_input == edit_keys[0]:
          new_item_name = input("What is this item's name? ")
          new_item_cost = input("What is this item's cost? ")
          new_item_quantity = input("How much of the item do you want to get? ")
          list.add_item(Grocery_Item(new_item_name, new_item_cost, new_item_quantity))
          display_list(list, item_divider)
    elif main_input == edit_keys[1]:
        display_list(list, item_divider)
        selected_item = input("Which item do you want to delete? ")
        for index in range(0, len(list.list_items)):
          if selected_item.lower() == list.list_items[index].name.lower():
            del list.list_items[index]
    if main_input == "exit":
      finished_editing = True
  
    

def new_list_menu(menu_divider, exit_key, edit_keys, item_divider, list_holder):
  print(menu_divider)
  valid_name = False
  while valid_name == False:
    new_list_name = input("What do you want to name the new list? \n")
    if new_list_name in list_holder:
      print("That shopping list name is already used.")
    else:
      valid_name = True
  
  new_position = len(list_holder)
  list_holder.append(Grocery_List(new_list_name))
  edit_list(list_holder[new_position], exit_key, edit_keys, item_divider)

def display_list_of_lists(lists, divider):
  print(divider)
  for item in lists:
    print(item.list_name)