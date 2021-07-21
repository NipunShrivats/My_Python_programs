# HEALTH MANAGEMENT SYSTEM

# 3 clients - Harry, Rohan, Hammad.
# Total 6 files - 0 for exercise 1 for diet.
# write a function when executed takes as input client name.

def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):

    # For HARRY
    if k == 1:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))
        if c == 1:
            value = input('Please enter the name of the exercise: ')
            print('\n')

            with open ('Harry_ex.txt', 'a') as he:
                he.write(str(getdate()) + ": " + value + "\n")
            print('submitted successfully!')

        elif c == 2:
            value = input('Please enter the name of the food item: ')
            print('\n')

            with open ('Harry_diet.txt', 'a') as hd:
                hd.write(str(getdate()) + ": " + value + "\n")
            print('submitted successfully!')

        else:
            print('Please enter valid input (Exercises: 1 & Diet: 2)')

    # FOR ROHAN
    elif k == 2:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))
        if c == 1:
            value = input('Please enter the name of the exercise: ')
            print('\n')

            with open ('Rohan_ex.txt', 'a') as re:
                re.write(str(getdate()) + ': ' + value + '\n')
            print('submitted successfully!')

        elif c == 2:
            value = input('Please enter the name of the food item: ')
            print('\n')

            with open ('Rohan_diet.txt', 'a') as rd:
                rd.write(str(getdate()) + ': ' + value + '\n')
            print('submitted successfully!')

        else:
            print('Please enter valid input (Exercises: 1 & Diet: 2)')

    # FOR HAMMAD
    elif k == 3:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))
        if c == 1:
            value = input('Please enter the name of the exercise: ')
            print('\n')

            with open('Hammad_ex.txt', 'a') as he:
                he.write(str(getdate()) + ': ' + value + '\n')
            print('submitted successfully!')

        elif c == 2:
            value = input('Please enter the name of the food item: ')
            print('\n')

            with open('Hammad_diet.txt', 'a') as hd:
                hd.write(str(getdate()) + ': ' + value + '\n')
            print('submitted successfully!')

        else:
            print('Please enter valid input (Exercises: 1 & Diet: 2)')

    else:
        print('Please enter valid input (Harry : 1, Rohan: 2, Hammad: 3)')

##### RETRIEVE #####

def retrieve(k):

    # For HARRY
    if k == 1:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))

        try:
            if c == 1:
                with open('Harry_ex.txt') as he:
                    for text in he:
                        print(text)
            elif c == 2:
                with open('Harry_diet.txt') as he:
                    for text in he:
                        print(text)

            else:
                print('Please enter valid input (Exercises: 1 & Diet: 2)')

        except Exception as e:
            print('Sorry, No information entered yet.')

    # FOR ROHAN
    elif k == 2:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))

        try:
            if c == 1:
                with open('Rohan_ex.txt') as re:
                    for text in re:
                        print(text)

            elif c == 2:
                with open('Rohan_diet.txt') as rd:
                    for text in rd:
                        print(text)

            else:
                print('Please enter valid input (Exercises: 1 & Diet: 2)')

        except Exception as e:
            print('Sorry, No information entered yet.')

    # FOR HAMMAD
    elif k == 3:
        c = int(input("Enter 1 for exercises and 2 for Diet: "))

        try:
            if c == 1:
                with open('Hammad_ex.txt') as re:
                    for text in re:
                        print(text)

            elif c == 2:
                with open('Hammad_diet.txt') as rd:
                    for text in rd:
                        print(text)

            else:
                print('Please enter valid input (Exercises: 1 & Diet: 2)')

        except Exception as e:
            print('Sorry, No information entered yet')

    else:
        print('Please enter valid input (Harry : 1, Rohan: 2, Hammad: 3)')



##### CODE RUNNER #####
print('***** Health Management System *****\n')
value = int(input('Enter 1 to Submit and 2 to retrieve information: '))

if value == 1:
     value_1 = int(input('Enter 1 for Harry, 2 for Rohan and 3 for Hammad: '))
     take(value_1)
elif value == 2:
     value_1 = int(input('Enter 1 for Harry, 2 for Rohan and 3 for Hammad: '))
     retrieve(value_1)
else:
    print('Please enter valid input (Submit: 1 & retrieve information: 2)')
