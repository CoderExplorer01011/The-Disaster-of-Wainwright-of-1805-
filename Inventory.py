# David Ramirez 
# 11/23/2024

#Inventory module
#The inventory will add items based off chapters
#Items will show up in inventory

#Show inventory/list
inventory = []

#Add a function that adds a item when picked up from chapter
def add_item(item):
    if item not in inventory:#if statement
        inventory.append(item)#gives player item
        print(f"{item} has been added to your inventory!")
    else:
        print(f"You already have a {item}.")

#The invenotry should put "-" behind the items as it's easy to identify when the text shows
#The inventory should say "Your inventory is empty" if there's no items obtained
#Include a print that says "Your inventory contains:"
def show_inventory():
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty")

#Clear the inventory list if player loses
def reset_inventory():
    global inventory
    inventory = []
    print("Your inventory has been reset.")