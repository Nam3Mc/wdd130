# i just added a limit of guess attempts to stop the game when you reach 15 attemts
# My code just shows hints in the right order of letters, i could not figure out how to add the _ to the hint

word = 'beautifull'
guess_count = 0
large = len
guess_count = guess_count +1
space = ''

print ( 'Guessing game' )
guess = input ( f'Here is your hint.' + ' _'* len (word) + '\nType your guest: > ' )


while guess != word and guess_count <15:

    if len(guess) == len(word):
        for letter in guess:
            if letter.lower() in word.lower():
                print ( letter.lower() , end='')
            elif letter.lower() == word.lower():
                print ( letter.upper() , end='' )
            else:
                print ( '_', end= '' )
        guess = input ('\nType your guest: <> ' )

        guess_count = guess_count +1        

    elif len(guess) > len(word):

        print ( f'The word is just {len(word)} letters long.' )
        guess = input ('Type your guest: > ' )
        guess_count = guess_count +1
    
    elif len(guess) < len(word):

        print ( f'The word must be {len(word)} letters long.' )
        guess = input ('Type your guest: > ' )
        guess_count = guess_count +1

    else:
        guess = input ('\nType your guest: >> ' )
        guess_count = guess_count +1

if guess_count >= 15:
    print ( f'The word was {word}, you could not guess it!' )
    print ( 'better luck next time! ' )
else:
    print ( 'this is the word! ' )
    print ( f'It took you {guess_count} attempts to guess it! ' )
