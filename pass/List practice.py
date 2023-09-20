numbers = []
number = ''
total = 0 

# loop to add numbers 
while number != 0:
    number = int ( input ( 'Please type a number: > ' ) )
    if number != 0:
        numbers.append(number)
print ( )

# this loop will sum all the values in the list
for number in numbers:
    total += number
print ( ) 

print ( f'The total is: {total} ' )
print ( f'The averange is: {total / ( len(numbers)-1 ) :.2f}')
print ( f'The highest number is: {max(numbers)} ' )
print ( )

min_positive = 0 
max_positive = max(numbers)

for number in numbers:
    if number > 0 and number < max_positive:
        min_positive = number
print ( f'The smallest positive number is: {min_positive}' )


numbers.sort()

print ( 'The sorted list is: ' )
for number in numbers:
    print ( number )
