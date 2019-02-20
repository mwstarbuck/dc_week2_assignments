import unittest
from shopping_list import ShoppingList
from grocery_item import GroceryItem
from grocery_logic import GroceryLogic


class GroceryAppTests(unittest.TestCase):

    def setUp(self):
        self.grocery_logic = GroceryLogic()
        self.shopping_list = ShoppingList("HEB")
        #self.shopping_list2 = ShoppingList("Kroger")
        self.item1 = GroceryItem("bread", 1.85, 2)
        self.item2 = GroceryItem("eggs", 1.85, 1)
        #self.item3 = GroceryItem("chips", 2.10, 2)
        self.shopping_list.items.append(self.item1)
        self.shopping_list.items.append(self.item2)
        # self.shopping_list2.items.append(self.item3)
        self.stores = [self.shopping_list]

    def test_add_only_unique_items(self):
        result = self.grocery_logic.add_unique_item(
            self.shopping_list, "bread")
        self.assertEqual(False, result)

    def test_calculate_cost(self):
        result = self.grocery_logic.calculate_cost(self.stores)
        self.assertEqual(5.55, 5.55, result)

    def tearDown(self):
        print("tearing down")


unittest.main()
