input ('Would you like to know, how old you will be on your next birthday? ')
age = int(input ('How old are you? ' ))
print (f'On your next birthday, you will be {1+ age}' )


Egg= int(input('How many egg cartons do you have? '))
print (f'If you have {Egg} cartons, then you have {Egg * 12}')


cookies = int(input('How many cookies do you have for your party? '))
people= int(input('How many of your friends are coming? '))
# Cookies_x_person = int(cookies / people)
# print (f'If { people} are coming, the you should give {Cookies_x_person} to each of then.')
print (f'If { people} are coming, the you should give {int(cookies / people) } to each of then.')
