#-*- coding: utf-8 -*-

import random

secret_number = random.randrange(0,10)
print secret_number, type(secret_number)

number_of_guesses = 1

while number_of_guesses <= 4:
    guessed_number = int(raw_input("Guess  my secret number. My secret number is between 0 and 10."))
    print guessed_number, type(guessed_number)

    if secret_number == guessed_number:
        print "Wow you ž guessed my secret number. You needed", number_of_guesses, "guesses."
        break
    elif secret_number < guessed_number:
        print "Your number is too high."
    elif secret_number > guessed_number:
        print "Your number is too low."
    else:
        print "Did you entered valid number?"
    number_of_guesses += 1

if number_of_guesses > 4:
    print "Sorry. You lost all your chances."

