
from shopping_list import ShoppingList
from grocery_item import GroceryItem
# formatting


def print_lines():
    print("------------------ \n")


def show_menu():
    # show_menu
    print_lines()
    print("CREATE new shopping list, enter 1: ")
    print("ADD a new item to an existing list, enter 2: ")
    print("To VIEW COMPLETE list, enter 3: ")
    print("To QUIT the app, enter 'q': ")
    print_lines()

# function that runs a function based on user input


def chooser(user_input):
    if user_input == "1":
        create_list()
    elif user_input == "2":
        append_to_list()
    elif user_input == "3":
        view_complete_lists()

# adds item to a list


def add_item(shopping_list):
    items = shopping_list.items
    name = input("Enter product name: ")
    while name == "":
        print("*** You did not enter a product name.***")
        name = input("Enter product name: ")
    if len(items) > 0:
        for i in range(0, len(items)):
            while name == items[i].name:
                # if name == items[i].name:
                print("***Item is already on list. Please enter another item.***")
                name = input("Enter product name: ")
    while True:
        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
        # create grocery_item object
            item = GroceryItem(name, price, quantity)
            shopping_list.items.append(item)
            break
        except ValueError:
            print("***Please re-enter a valid price and quantity***")


# creates a list and then adds to the main (stores list)


def create_list():
    name = input("Enter the store name: ")
    # Create object list
    while name == "":
        print("*** You did not enter a store name.***")
        name = input("Enter the store name: ")
    shopping_list = ShoppingList(name)
    answer = ""
    while answer != "n":
        answer = input("Add Item to list? (y/n): ")
        if answer == "y":
            add_item(shopping_list)
        elif answer == "n":
            input(
                f"{shopping_list.name} is being added to main shopping list... Hit return to continue.")
        else:
            print("Invalid choice.  Please enter again")
    stores.append(shopping_list)
    # print(stores[0].name)

# shows a list of stores for choosing which store to add an item to


def view_stores():
    for i in range(0, len(stores)):
        store = stores[i]
        print(f"{i + 1} - {store.name}")

# shows user a complete lits of stores and items for each store


def view_complete_lists():
    print("")
    print("Printing complete shopping list")
    total = 0.00
    for i in range(0, len(stores)):
        store_total = 0.00
        store = stores[i]
        print(f"{i + 1} - {store.name}")
        print("\t_Items_")
        items = store.items
        for j in range(0, len(items)):
            item = items[j]
            store_total += (item.price * item.quantity)
            print(
                f"\t{j + 1} - {item.name} - ${item.price} - qty = {item.quantity}")
        store_total = round(store_total, 2)
        print(f"{store.name} total = ${store_total}")
        print("------------------")
        total += store_total
    total = round(total, 2)
    print_lines()
    print(f"Grand total: ${total}")

# function that will allow user to append to existing list


def append_to_list():
    print("")
    print("Current stores in master list")
    view_stores()
    to_add_to = int(
        input("Enter the the store number to add to that list: ")) - 1
    for i in range(0, len(stores)):
        if i == to_add_to:
            add_item(stores[i])


# stores is the list of shopping_lists()
stores = []


user_input = ""
while user_input != "q":
    show_menu()
    user_input = input("Please enter a choice from the menu: ")
    chooser(user_input)
