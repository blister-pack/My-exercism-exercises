"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}

    for item in items:
        if item not in inventory:
            no_item = items.count(item)
            inventory[item] = no_item

    return inventory

print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for index, item in enumerate(items):
        if item in items and item not in inventory:
            inventory[item] = items.count(item)
        elif item in items and item in inventory:
            if item in items[:index]:
                continue
            else:
                inventory[item] = inventory[item] + items.count(item)

    return inventory
print(add_items({}, ["iron", "iron", "diamond"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for index, item in enumerate(items):
        if item in items and item not in inventory:
            continue  #  assuming there will be no requests to deduct from an item that never was in the inventory
        elif item in items and item in inventory:
            if item in items[:index]:
                continue
            else:
                inventory[item] = inventory[item] - items.count(item)
                if inventory[item] < 0:
                    inventory[item] = 0

    return inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)

    return inventory

print(remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"))


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    the_tuples = []
    for item in inventory:
        if inventory[item] > 0:
            the_tuples.append((item, inventory[item]))

    return the_tuples

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))