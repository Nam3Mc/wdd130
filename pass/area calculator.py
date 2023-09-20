# Write functions to compute and return the areas of squares, rectangles, and circles. 
# These functions should not display the values directly, but rather should return them, so they could be used in other parts of the program.

def ac_square(value):
    area = value ** 2
    return area

def ac_triangle(value_l, value_w):
    area = value_l * value_w
    return area

def ac_circle(value):
    import math
    area = math.pi * (value ** 2 )
    return area



squared_length2 = float ( input ( 'Intruduce a single length value: ' ) )
print ( f'The are of an square with {squared_length2} lenght will be { ac_square(squared_length2)} ' )
print ( )
print ( f'Using this area we can calculated that a radious of { squared_length2 / 2 :.2f} ' )
radious = squared_length2 / 2 
import math
print ( f'That shows a circle with a circunference of { 2 * math.pi * radious :.2f} ' )
print ( )
print ( f' a cube with { squared_length2 } of lenght produce a cube of { squared_length2 * squared_length2 * squared_length2 :.2f} ' ) 

squared_length = float ( input ( 'Intruduce the length of a squared side: ' ) )
print ( f' Your squared are is : { squared_length ** 2 :.2f}')
print ( )

rectangle_lenght = float ( input ( 'For calculating your rectangle area, please introduce the triangle lenght : ' ) )
reactangle_width = float ( input ( 'Now introduce your triangle width: ' ) )
print ( f' Your triangle area is { rectangle_lenght * reactangle_width :.2f} ' )
print ( )
circle_radius = float ( input ( 'For calculating your circle area, please introduce your circle radius: ' ) )
import math
print ( f'Your circle are is: {math.pi * ( circle_radius ** 2 ) :.2f} ' )
print ( )
lenght = float ( )



print ( )
w_speed = 0 # reset speed to avoid errors in calculating 
w_speed = float ( input ( 'What is the wind speed? ' ) )
temperature = float ( input ( 'What is the temperature? ' ) )
f_or_c = input ( 'Fahrenheit or Celsius (F/C)? ' )
print ( )
if f_or_c.upper() == 'C':
    print ( f'At temperature {temperature}Cº, and speed {w_speed} mph, the windchill is: {wc_calculater( False, w_speed, temperature ):.2f}, Cº' )
elif f_or_c.upper() == 'F':
    print ( f'At temperature {temperature}Cº, and speed {w_speed} mph, the windchill is: {wc_calculater(temperature, w_speed , False ):.2f} Fº ' )

elif exit.upper == 'Y':
    print ( )
    print ( 'Bye ')
    