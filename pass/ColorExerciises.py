word = 'beautifull'

guess = input ( 'Guess the wword in \n <' + '_ '* len(word) + '>\n')

for char in word:

    if char.lower() == guess.lower():
        print ('_', end='')

    else:
        print ( char.lower()  )
print ( )