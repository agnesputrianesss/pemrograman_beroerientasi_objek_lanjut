class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        print("Hero Nana")

class Item:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item", item.name)

    def remove_item(self, item):
        self.items.remove(item)

player = Player("Hero Nana")
sword = Item("Clock of Destiny (CoD")
shield = Item("Immortal")

print("="*40)

player.inventory.add_item(sword)
player.inventory.add_item(shield)
player.inventory.items
print(" ")