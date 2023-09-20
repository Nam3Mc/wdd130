word = "book"

number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")


shoppings = ['a','b','c']
prices = [1,2,3]

for each in range(len(shoppings) ):# right
    item = shoppings[each]
    value = prices[each]
    each += 1
    print (f'{each}. {item} - ${value}' )
print ( )


# Please enter an action: 3
# Which item would you like to remove? 2
# Item removed.
# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 2
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Butter - $4.00

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 4
# The total price of the items in the shopping cart is $7.49

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 5
# Thank you. Goodbye.