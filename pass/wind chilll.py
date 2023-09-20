# wind chill cacculater funtion
def wc_calculater( temp_f , velocity , temp_c ):
    if temp_c:
        temp_f = ( temp_c * 1.8 ) + 32 # coverting celcius to Fahrenheit 
        wct = 35.74 + 0.6215 * temp_f - 35.75 * (velocity ** 0.16) + 0.4275 * temp_f * ( velocity ** 0.16)
    else:
        wct = 35.74 + 0.6215 * temp_f - 35.75 * (velocity ** 0.16) + 0.4275 * temp_f * ( velocity ** 0.16)
    return wct

temperature = float ( input ( 'What is the temperature? ' ) )
f_or_c = input ( 'Fahrenheit or Celsius (F/C)? ' )
print ( )

w_speed = 5

for i in range (5, 61, 5 ):
    if f_or_c.upper() == 'C':
            print ( f'At temperature {temperature}Fº, and speed {w_speed} mph, the windchill is: {wc_calculater( False, w_speed, temperature ):.2f} Cº ' ) 
            w_speed += 5

    elif f_or_c.upper() == 'F':
            print ( f'At temperature {temperature}Cº, and speed {w_speed} mph, the windchill is: {wc_calculater(temperature, w_speed , False ):.2f} Fº ' )
            w_speed += 5