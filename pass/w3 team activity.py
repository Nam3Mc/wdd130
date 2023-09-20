#core program
'''grade = float ( input ( ' Please introduce your grade persentaje to receive your grade: ' ) )
print ( )
if grade >= .90:
    print ( 'Congratulations, Your Grade is: A \nAmazing job! You have passed. ' )
elif grade >= .80:
    print ( 'Verry well, your grade is: B \nWell done! ' )
elif grade >= .70:
    print ( 'Good jod, your grade is: C \nWe know your can do it better, keep pushing! \nYou have passed. ' )
elif grade >= .60:
    print ( 'Your grade is: D \nUnfortunately, your grade does not qualify to pass the course. \nYou have not passed. ' )
else:
    print ( 'Your grade is: F \nUnfortunately, your grade does not qualify to pass the course. \nYou have not passed. ' )
print ( )'''
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Stretch Challenge
grade = float ( input ( ' Please introduce your grade persentaje to receive your grade: ' ) )
print ( )
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
print ()
sing = ''
plus_minus = grade % 10
if plus_minus >= 7:
    sing = '+'
elif plus_minus <= 3:
    sing = '-'
else:
    sing = ''
print ()
if grade >= 93:
    sing = ''
print ()
if letter == 'F':
    sing = ''

print ( f'Your grade is: { letter } { sing }')
