# I added 2 discount of 5% and 10% if the stotal amount is higher than 75 and 150

# lists
menu = [ '1. Add item', '2. View cart', '3. Remove item', '4. Compute total', '5. Quit' ]
shoppings = []
prices = []

# variables
new_item = ''
choose = 0
value = 0
total = 0

#loop
while choose != 5:
    print ( 'Please select one of the following: ' )
    for action in menu:
        print ( action )
    choose = int ( input ( 'Please enter an action: ' ) )
    print ( )
    
    if choose == 1:
        new_item = input ( 'What item would you like to add? ' )
        price = float ( input ( f'What is the price of {new_item}? '))
        print ( f'{new_item.capitalize()} has been added to the cart. ' )
        shoppings.append(new_item)
        prices.append(price)
        print ( )
    
    elif choose == 2:
        if len(shoppings) == 0:
            print ( 'Your cart is enty. ' )
        
        elif len(shoppings) > 0:
            print ( 'The contents of the shopping cart are: ' )
            for each in range(len(shoppings) ):
                item = shoppings[each]
                value = prices[each]
                print (f'{each+1}. {item} - ${value:.2f}' )
        print ( )

    elif choose == 3:
        delete = int ( input ( 'Which item would you like to remove? ' ) )
        shoppings.pop(delete-1)
        prices.pop(delete-1)

        print ( 'Item removed. ' )
        print ( )

    elif choose == 4:
        for value in range(0,len(prices)):
            total = total + prices[value]
        if total > 75 and total < 150:
            print ( f'The total price of the items in the shopping cart is: ${total:.2f}' )
            print ( 'Congratulations, you got a discount of 5% ' )
            print ( f'Your new total bill is ${total-(total*0.05):.2f}\nYour saving is ${total*0.05:.2f} ' )
            print ( )
        elif total >= 150:
            print ( f'The total price of the items in the shopping cart is: ${total:.2f}' )
            print ( 'Congratulations, you got a discount of 10% ' )
            print ( f'Your new total bill is ${total-(total*0.10):.2f}\nYour saving is ${total*0.10:.2f} ' )
            print ( )
        else:
            print ( f'The total price of the items in the shopping cart is: ${total:.2f} ' )
            print ()
        # total = 0 # if the total is not reseted the total will increse each time we use the 4 option 

    elif choose == 5:
        print ( 'Thank you. Goodbye. ' )
    