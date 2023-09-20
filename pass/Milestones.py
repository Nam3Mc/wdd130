# I added an option for tips, because i wanted to know how to do it, and it works verry well!

child_meal = float ( input ( 'Child meal Price $: ' ) )
adult_meal = float ( input ( 'Adult meal Price $: ' ) )
child_number = int ( input ( 'How many children meal:  ' ) ) 
adult_number = int ( input ( 'How many adults meal: ' ) )
tax_rate = float ( input ( ' How much is the sales tax rate % ' ) )
print ( )

print ( f'Children meal total price: ${ child_meal * child_number :.2f}' )
children_total = child_meal * child_number
print ( f'Adults meal total price: ${ adult_meal * adult_number :.2f} ' )
adults_total = adult_meal * adult_number
subtotal = adults_total + children_total
print ( )
print ( f'Subtotal: ${ children_total + adults_total :.2f} ' )
print ( f'Sales Tax ${ (subtotal * tax_rate) / 100 :.2f} ')
total = (subtotal * tax_rate) / 100 +subtotal 
print ( )
print  ( f'Total: ${ total:.2f}' )
print ( )
paid_with = float ( input ( 'What is the payment amount: $ ' ) )
change = paid_with - total 
print ( )
print ( f'Change: $ { change :.2f} ')
print ( )
tip = input ( 'Would you like to add a tip? (Y/N): ')
if tip.lower() == 'y':
    tip_amoun = float ( input ( 'How much would you like to tip : $'))
    print ( 'Thank ypur for yout tip!')
    print ( )
    print ( f' Your new Change is: {change - tip_amoun :.2f}')
else:
    print ( )
    print ('Thank you for your purchace, come back soon! ' )


