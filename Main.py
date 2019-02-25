from stringing import stringing_script
from fletching import makeBows_script
from enchant import enchant_script
from gemcut import gemcutter_script


def main_script():
    '''
    Runs the beginning of the script.

    This will ask if you want to string bows or if you want to make them (u).
    It will execute the thing you choose and if not the given commands are given
    it just resets and run's again.

    :return: stringing script, fletching script or reset.
    '''

    print('Do you want to string bows, fletch bows, cut gems or enchant rings?')
    user_input = input("write 'fletch', 'string', 'gem' or 'enchant': " )

    # Create longbows (u)
    if user_input.lower() == 'fletch':
        makeBows_script()

    # String bows
    elif user_input.lower() == 'string':
        stringing_script()

    # Enchant rings
    elif user_input.lower() == 'enchant':
        enchant_script()

    # Cut gems
    elif user_input.lower() == 'gem':
        gemcutter_script()

    # Not a valid input --> Reset
    else:
        print(f'"{user_input}" is not an valid input. Try again....')
        main_script()

main_script()

