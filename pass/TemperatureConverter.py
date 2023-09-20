# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

fahrenheit = int ( input ( 'Introduce the temperature in Farhenheit degrees, to convert it to Celsius ' ) )
print ( )
celsius = ( fahrenheit - 32 ) * 5/9
print ( )
print ( f" The temperature is { celsius :.1f} Celsius degrees. " )


# Verify that your program works correctly by following each step in this testing procedure:

# Try the values in the examples on this page and ensure that your program generates the same results.

# Verify that you are displaying the result to 1 decimal point of precision as shown.

# Try converting 32 degrees Fahrenheit (freezing, which should be 0 degrees Celsius) and 212 degrees (boiling, which should be 100 degrees Celsius)

# Try converting 0 and a negative number and make sure they come out as you would expect.

# Verify that you have used good style, by checking the variable names you have used as well as the use of blank lines and whitespace around your operators.