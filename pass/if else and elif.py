# Comparing Numbers
# Write a program that asks the user for two integers.
# Then, write three separate if/else statements as follows:
# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".
# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".
# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

print ( 'What number of two digits, betwen 30 and 40 I`m thinking in? ' )
number = input ( 'Try to guess, thel me the number: ' )
if number == '36':
    print ( 'That is correct, you`re amazing! ' )
elif number < '36':
    print ( 'Good shot, but the nuber is higher. Try again.' )
    number2 = input ( 'What is the number? ' )
    if number2 == '36':
        print ( 'That is correct, you`re amazing! ' )
elif number > '36':
    print ( ' Nice atemp, but the nuber is lower. Try againg. ' ) 
    number3 = input ( 'What is the number? ' )
    if number3 == '36':
        print ( 'That is correct, you`re amazing! ' )
print ( )
print ( ' to comparate 2 number please, ' ) 
number4 = int ( input ( 'Introduce the first number: ' ) )
number5 = int ( input ( 'Introduce the second number: ' ) )
if number4 == number5:
    print ( ' The numbers are iqual. ' )
elif int ( number4 ) > int ( number5 ):
    print ( 'The first number is greater than second. ' )
else:
    print ( str ( number5 ) + ' is greater than ' + str ( number4 ) ) 
print ( )
print ( )
favorite_animal =  input ( 'What is your favorite animal? ' )
if favorite_animal.lower() == 'lion':
# if favorite_animal in ( 'Tiger', \
#                        'Lion', 'Cat', 'Dog' ):
    print ( 'Awesome, I mine too! ' )
else:
    print ( 'It isn`t mine, but it`s a good one! ' )