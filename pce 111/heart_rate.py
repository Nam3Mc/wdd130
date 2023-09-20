
age = int ( input ( 'Please enter your age: ' ) )
minute_rate = ( 220 - age )
faster_rate = ( ( minute_rate * 85 ) / 100 )
slowest_rate = ( ( minute_rate * 65 ) / 100 )

print ( f'When you exercise to strengthen your heart, you should keep your heart rate between { slowest_rate:.0f} and { faster_rate:.0f} beats per minute. ' )

