## DESCRIPTION ##
# 1. Using OOPS concept.
# 2. Creating a Program for a car dealership.
# 3. DISPLAY COLLECTION, LEND, ADD and RETURN CARS.
# 4. Created a button to quit or continue the program.

print('***** Welcome to RAWAT CARz *****\n')
class Rawat_carz:
    '''Lend, add, return, display'''
    def __init__(self, carlist, name): # 1st cosntructor class
        self.carlist = carlist
        self.name = name # business name
        self.lendDict = {} # items that are lend to customers will be stored

    def display_cars(self):
        print(f"We have the following cars in {self.name}'s showroom")
        for cars in self.carlist:
            print(cars)

    def lend_cars(self, user, cars): # user will be lender
        if cars in self.carlist and cars not in self.lendDict.keys():
            self.lendDict.update({cars:user})
            print('Database has been updated, you may collect car keys from the reception.\n ')

        elif cars not in self.carlist:
            print('***** This car is not available *****')

        elif cars in self.lendDict.keys():
            print(f'This car has already been lend to {self.lendDict[cars]}, please try to get another car.\n')

        else:
            pass

    def add_cars(self, cars):
        if cars not in self.carlist:
            self.carlist.append(cars)
        else:
            print('This car already exists please try next time\n')

    def return_cars(self, cars):
        self.lendDict.pop(cars)
        print('Thank you for returning the car\n')

if __name__ == '__main__':
    my_cars = Rawat_carz(['Sonnet', 'XUVOO', 'KUVOO', 'WagnR', 'C-class', 'S-class', 'Esteem', 'Duster', 'Polo', 'Pinto', 'Beetle', 'Santro', 'Alto', 'Alto 800'], 'RAWAT CARZ')

    while (True):
        print(f'\nWeclome to the {my_cars.name}, Enter your choice to continue\n')
        user_choice = input("1 - Display collection\n2 - Lend a Car\n3 - add a car to the collection\n4 - Return a car\nEnter your choice:- ")
        if user_choice not in ['1','2','3','4']:
            print('***** Please enter a valid number *****')
            continue

        ## To display collection ##
        elif user_choice == '1':
           '''To display collection'''
           my_cars.display_cars()

        ## To lend cars ##
        elif user_choice == '2':
            '''To lend cars'''
            cars = input('Emter the name of the car you want to lend: ')
            user = input('Enter the name of the customer: ')
            my_cars.lend_cars(user, cars)

        ## To add a car to the collection ##
        elif user_choice == '3':
            '''To add a car to the collection'''
            cars = input('Enter the Car name you want to add: ')
            my_cars.add_cars(cars)

        ## Return a car ##
        elif user_choice == '4':
            '''Return a car'''
            cars = input('Enter the name of the car you want to return: ')
            my_cars.return_cars(cars)

        print("\nPress 'q' to quit and c to continue")
        user_choice2 = ""
        # user_choice2 = input('Input choice:- ')
        while (user_choice2 != 'q' and user_choice2 != 'c'):
            user_choice2 = input('Input choice:- ')
            if user_choice2 == 'q':
                quit()
            elif user_choice2 == 'c':
                continue