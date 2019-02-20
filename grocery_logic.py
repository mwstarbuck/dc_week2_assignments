class GroceryLogic:
    def __init__(self):
        self.name = "Logicon"

    def add_unique_item(self, shopping_list, name):
        items = shopping_list.items
        name = "bread"
        if len(items) > 0:
            for i in range(0, len(items)):
                while name == items[i].name:
                    return False

                return True

    def calculate_cost(self, stores):
        total = 0.00
        for i in range(0, len(stores)):
            store_total = 0.00
            store = stores[i]
            items = store.items
            for j in range(0, len(items)):
                item = items[j]
                store_total += (item.price * item.quantity)
                store_total = round(store_total, 2)
            total += store_total
        total = round(total, 2)
        return store_total, total
