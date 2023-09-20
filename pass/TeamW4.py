# This is my original code ! 

# import random
# 
# number = random.randint(1, 100)
# 
# guess = int ( input ( 'I`m thinking in a magic number \nTry to guess it, type a number. \nWhat is your number: > ' ) )
# print ( )
# 
# while guess < number:
    # print ( 'No. The number is higher! ' )
    # print ( )
    # guess = int ( input ( 'What is your number: > ' ) )
    # print ( )
# 
# if guess > number:
    # print ( 'Close. The number is lower ' )
    # print ( )
    # guess = int ( input ( 'What is your number: > ' ) )
# 
# print ( )
# print ( 'Awesome. This is the number ' )
# print ( )

# I needed help to finish the stretch i needed to use the example! 

import random

start_again = 'yes'

while start_again.lower() == 'yes':
    number = random.randint(1, 100)
    guess_atemt = 0
    guess = 0

    while not guess == number:

        guess_atemt = 1
        
        while guess != number:
            guess_atemt = guess_atemt +1
            guess = int ( input ( 'Guess the number ! \n > ' ) )
        
            if guess > number:
                print ( 'Close. The number is lower ' )
                print ( ) 
            elif guess < number:
                print ( 'Close. The number is higher ' )
                print ( )
            else:
                print ( 'Awesome. This is the number ' )
                print ( f'Guess took you {guess_atemt} atempts! ' )
                print ( )

        start_again = input ( ' Would you like to play again (yes/no)? ' )
    print ( 'Thanks for playing ' )





    # import random

# keep_playing = "yes"

# # As long as they say "yes" we will keep playing
# while keep_playing == "yes":
    # magic_number = random.randint(1, 100)

    # # this variable will keep track of how many guesses it took
    # guess_count = 0

    # guess = -1

    # # Keep going as long as the guess doesn't match the magic number
    # while guess != magic_number:
        # guess = int(input("What is your guess? "))
        # guess_count = guess_count + 1

        # if guess < magic_number:
            # print("Higher")
        # elif guess > magic_number:
            # print("Lower")
        # else:
            # print("You guessed it!")

    # # At this point, they have guessed it correctly
    # print(f"It took you {guess_count} guesses")

    # keep_playing = input("Would you like to play again (yes/no)? ")

# print("Thank you for playing. Goodbye.")