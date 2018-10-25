"""
Steven Tucker
14 October 2018
CSC 231-003, Fall 2018
Lab 2: Foot Measure Project
"""

import FootMeasure_class as fm

def main():
    print('Instructions:\n'
          '1. Type a number for the number of feet.\n'
          '2. Type a number for the number of inches (can be more than 12).\n'
          '3. Type the number of the action you want to do.\n')

    measure1 = get_input()
    new_menu(measure1)


def get_input():
    has_valid_input = False
    while has_valid_input == False:
        get_feet = input('Please type a number of feet: ')
        get_inches = input('Please type a number of inches: ')

        try:
            feet = int(get_feet)
            inches = int(get_inches)
            has_valid_input = True                                  # Only exits the loop if they're valid numbers
        except ValueError:
            print('\nPlease type a valid integer for feet and inches values.\n')

    measure = fm.FootMeasure(feet = feet, inches = inches)          # Creates the object
    print('Your Measurement: ' + str(measure) + '\n')
    return measure


def new_menu(m1):
    """Menu for selecting what to do next: add, convert to inches, optional keyword args, relational operators,
    or quit."""
    while True:
        selection = input('Type the number of what you would like to do:\n'
                          '1. Add to ' + str(m1) + '\n'
                          '2. Output Optional Keyword Arguments\n'
                          '3. Output Relational Operators\n'
                          '4. Quit\n')

        if selection == '1':
            new_add(m1)
        elif selection == '2':
            optional_args()
        elif selection == '3':
            relation_ops()
        elif selection == '4':
            my_quit()
        else:
            print('Please select a valid input.\n')


def new_add(m1):
    """Prompts for a new measurement to add. Adds it to Your Measurement, then prints the total """
    new_measure = get_input()
    result = m1 + new_measure
    print('Sum of Your Measurement and New Measurement:', result, '\n')


def optional_args():
    """Create a FootMeasure object in various ways by use of optional keyword arguments."""
    # Measurements - Creates 4 new instances
    meas1 = fm.FootMeasure()
    meas2 = fm.FootMeasure(feet=5)
    meas3 = fm.FootMeasure(feet=5, inches=8)
    meas4 = fm.FootMeasure(inches=68)

    # Prints the display of the 4 new instances
    print('\nHere are 4 differently generated instances of FootMeasure:')
    print(meas1)
    print(meas2)
    print(meas3)
    print(str(meas4) + '\n')


def relation_ops():
    """Showcases the different relational operators (==, !=, <, <=, >, >=)."""
    # Measurements - Creates 3 new instances
    meas1 = fm.FootMeasure(feet = 2, inches = 6)
    meas2 = fm.FootMeasure(feet = 2, inches = 10)
    meas3 = fm.FootMeasure(feet = 1, inches = 1)

    # Relational Operators sentences
    print('Is ' + str(meas1) + ' == ' + str(meas3) + '? ' + str(meas1 == meas3))
    print('Is ' + str(meas1) + ' != ' + str(meas2) + '? ' + str(meas1 != meas2))
    print('Is ' + str(meas1) + ' < ' + str(meas2) + '? ' + str(meas1 < meas2))
    print('Is ' + str(meas1) + ' <= ' + str(meas3) + '? ' + str(meas1 <= meas3))
    print('Is ' + str(meas2) + ' > ' + str(meas1) + '? ' + str(meas2 > meas1))
    print('Is ' + str(meas3) + ' >= ' + str(meas1) + '? ' + str(meas3 >= meas1) + '\n')


def my_quit():
    """Prompts user to deliberately exit."""
    input('Press Enter to quit. ')
    exit(1)


main()