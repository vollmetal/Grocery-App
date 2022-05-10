import unittest
import GroceryAppMain
import GroceryApp

class TestApp(unittest.TestCase):

  def setUp(self):
    self.grocery_list = GroceryApp.Grocery_List("WalMart", "38679 1st Strt")
    self.grocery_item = GroceryApp.Grocery_Item("Bread", 5, 1)
    
  def test_display_list(self):
    self.grocery_list.add_item(GroceryApp.Grocery_Item("Shoes", 20, 1))
    self.grocery_list.add_item(GroceryApp.Grocery_Item("Shoes", "blard", 1))
    self.grocery_list.add_item(GroceryApp.Grocery_Item("Shoes", 20, 1))
    self.grocery_list.add_item(GroceryApp.Grocery_Item("Shoes", 20, 1))
    self.grocery_list.add_item(GroceryApp.Grocery_Item("Shoes", 20, 1))
    GroceryApp.display_list(self.grocery_list, "********")

    self.grocery_list.remove_item(3)
    GroceryApp.display_list(self.grocery_list, "********")
    
  def test_input_restriction(self):
      output = GroceryApp.check_item_int("1")
      print(output)
GroceryAppMain.GroceryApp()