## Snake Water Gun ##
# snake > water
# water > gun
# gun > snake

import random

chances = 10
no_of_chances = 0 # total 10
comp_points = 0
your_points = 0

game_data = ['s', 'w', 'g'] # use small characters only

while (no_of_chances < chances): # will only run 10 times.
    player_input = input("'S' for Snake\n'W' for Water\n'G' for Gun\n\nPlease Enter your character : ")
    computer_input = random.choice(game_data)

    # DRAW
    if player_input == computer_input:
        '''if draw both players get points'''
        comp_points += 1
        your_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('DRAW !\nboth gets +1 point\n')

    # WINNING
    elif player_input == 's' and computer_input == 'w':
        your_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('YOU WIN !\nyou get +1 point\n')

    elif player_input == 'w' and computer_input == 'g':
        your_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('YOU WIN !\nyou get +1 point\n')

    elif player_input == 'g' and computer_input == 's':
        your_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('YOU WIN !\nyou get +1 point\n')

    #LOOSING
    elif player_input == 'w' and computer_input == 's':
        comp_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('OOOOPS, YOU LOOSE\ncomputer get +1 point\n')

    elif player_input == 'g' and computer_input == 'w':
        comp_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('OOOOPS, YOU LOOSE\ncomputer get +1 point\n')

    elif player_input == 's' and computer_input == 'g':
        comp_points += 1
        no_of_chances += 1
        print(f"Your input: {player_input}\nComputer input : {computer_input}")
        print('OOOOPS, YOU LOOSE\ncomputer get +1 point\n')

    else:
        print('***** INVALID INPUT *****\n')

    print(f'{chances - no_of_chances} chances are left out of {chances}\n')

if comp_points > your_points:
    print(comp_points)
    print(your_points)
    diff = comp_points - your_points
    print(f"Computer win the game by {diff} points.")

if comp_points < your_points:
    print(comp_points)
    print(your_points)
    diff = your_points - comp_points
    print(f"You win the game by {diff}")
print('********************************************* GAME OVER *********************************************')
