# list of frineds
shoppings = []
item = ''

print ( )
print ( 'QUIT to leave ' )
print ( )

while item != 'quit':
    item = input ( 'Type your shopping item: > ' )
    if item != "quit":
        shoppings.append(item.capitalize())
print ( )

print ( 'Your shopping list : ' )
for element in shoppings:
    print (element)
print ( )

print ( 'The shopping list with indexes is: ' )
for i in range( len(shoppings) ):
    element = shoppings[i]
    print(f'{i}. {element} ' )
print ( )

delete = int ( input ( 'Which item would you like to change? \n > ' ) )
shoppings.pop(delete)
item = input ( 'Type your new item: \n > ' ) 
shoppings.append( item.capitalize() )
print ( )

print ( f'The shopping list with indexes is: ' )
for i in range(len(shoppings)):
    element = shoppings[i]
    print(f"{i}. {element}")
print ( )