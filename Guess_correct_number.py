# Guess the number
# MY CODE...
print('Guess the correct number!')
n = 18
no_of_guesses = 1
print('ATTENTION : Your number of guesses is limited to 5 times only.\n')

while(no_of_guesses < 6 ):
    input_1 = float(input('Please guess your number: '))
    if input_1 == n:
        print('CONGRATULATIONS, you have chosen the correct number!\n')
        print(5-no_of_guesses, 'number of guesses are left.')
        print(no_of_guesses, 'number of guesses you took to finish.')
        no_of_guesses += 1
        break

    elif input_1 > n:
        print("The number you have entered is 'GREATER' than original number!\n")
        print(5-no_of_guesses, 'number of guesses are left.')
        no_of_guesses += 1
        continue

    else:
        print("The number you have entered is 'SMALLER' than the original number!\n")
        print(5-no_of_guesses, 'number of guesses are left.')
        no_of_guesses += 1
        continue

print("**********GAME OVER**********")

#####################################################################################

'''n = 69
no_of_guesses = 1

while(no_of_guesses < 6):
    input_1 = float(input('Please input a number : '))

    if input_1 > n:
        print('The number you have entered is Greater than the original number.')
    elif input_1 < n:
        print('The number you have entered is Smaller than the original number.')
    else:
        print('Congratulations, you have entered the correct number.')
        print(no_of_guesses, 'no. of guesses you took to finish!')
        break
    print(5 - no_of_guesses, 'no of guesses left')
    no_of_guesses += 1
print('****Game over****')'''