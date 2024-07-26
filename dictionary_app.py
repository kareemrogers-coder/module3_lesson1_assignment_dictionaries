#Question 1


""" Objective:

The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

Add a new category called "Beverages" with at least two items.

Update the price of "Steak" to 17.99.

Remove "Bruschetta" from "Starters".

Problem Statement:
Given the initial menu: """

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def s():
    #to create space in code
    print("="*60)

def a():
    print("Adding a new category called Beverages with at least two items.")

def b():
    print("Updating the price of Steak to 17.99.")

def c():
    print("Removing Bruschetta from Starters.")


#Add a new category called "Beverages" with at least two items.

print(restaurant_menu) # First is to print the existing to examine.

s()
a()
s()

# Because its a nested dictionary you need to create variable to create beverages and its item

add_bev = restaurant_menu["Bevearage"] = { } # this will create an empty Beverage category inside the first level of the dictionary.

print(restaurant_menu) # to verify, I reprint the menu aagin

#then you will add items to add_bev with its values


add_bev["Cranberry Juice"] = 4.58
add_bev["Cherry Coke"] = 2.99

#finally you can reprint the resturant menu with the added menu category and its items.

print(restaurant_menu)

s()
b()
s()

#Update the price of "Steak" to 17.99.

# print the dictionaary to verify its contents:

print(restaurant_menu)

#access the catergory where the steak item resides.

print(restaurant_menu["Main Course"])


#rename/create a variable where the to access the nested dictionary:

update_steak = restaurant_menu["Main Course"]

#Now access the sublist or nested dictionary and update the price

update_steak["Steak"] = 17.99

print(restaurant_menu["Main Course"])

print(restaurant_menu)

s()
c()
s()

# Remove "Bruschetta" from "Starters".

#print menu to verfiy its contents:

print(restaurant_menu)

#exmaine the Starters nest dictionary.

print(restaurant_menu["Starters"])


#create a variable is easilty manage the nested variable

del_bru = restaurant_menu["Starters"]

#print the new varible to verify and confirm.

print(del_bru)

#delete the "Bruschetta" item.

del del_bru["Bruschetta"]


# reprint the nested dictionary.
print(restaurant_menu["Starters"])

#reprint the entire menu:

print(restaurant_menu)
