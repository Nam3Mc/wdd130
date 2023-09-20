# Work as a team to write a Python program named discount.py that gets a customer’s 
# subtotal as input and gets the current day of the week from your computer’s 
# operating system. Your program must not ask the user to enter the day of the week. 
# Instead, it must get the day of the week from your computer’s operating system.
# 
# If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
# your program must subtract 10% from the subtotal. Your program must then 
# compute the total amount due by adding sales tax of 6% to the subtotal. 
# Your program must print the discount amount if applicable, the sales tax amount, 
# and the total amount due.
# 
# Stretch Challenges
# 
# Near the beginning of your program replace the code that asks the user for the subtotal 
# with a loop that repeatedly asks the user for a price and a quantity and computes the 
# subtotal. This loop should repeat until the user enters "0" for the price.




from datetime import datetime

current_date = datetime.now()
day = 2
# current_date.weekday()
subtotal = []
price = None

while price != 0:  
    print ( 'Type 0 in price to quick ' )
    price = float ( input ( 'Please intoduce the price: ' ) )

# else:
#     # subtotal = float ( input (' Please enter the subtotal: ' ) )
#     tax = ( subtotal * 0.06 )
#     discount = ( subtotal * 0.10 )

#     # this is the part of the code which will generate ethe dicount 
#     if day in ( 0, 3, 4, 5, 6):
#         print ( f' Sales tax amount: { tax:.2f} ' )
#         print ( f' Total: { subtotal + tax:.2f} ' ) 

#     elif day in ( 1, 2) and subtotal < 50:
#         print ( 'Today we have an amazin promotion ')
#         print ( 'If your purchase is iqual or higher than 50 $ ')
#         print ( 'You will receive a DISCOUNT OF 10% ' )
#         print ( f'Adding { 50 - subtotal } $ you will qualify for this discount ' )
#         print ( f' Sales tax amount: { tax:.2f} ' )
#         print ( f' Total: { subtotal + tax:.2f} ' ) 

#     else:
#         print ( f' Sales tax amount: { tax:.2f} ' )
#         print ( f' Discount amount: { discount:.2f} ' )
#         print ( f' Total { ( subtotal - discount ) + tax :.2f} ' )