


## Import stuff
from pyclick import HumanClicker
import random, time, pyautogui
from random import randint


## Import my own information
from info_formulas import coordinates, rand_coor, rand_sleep

#################################################
#################################################
#################################################


def main_script(amountOfLogs):

    # initialize HumanClicker object
    hc = HumanClicker()

    # Some time to set up...
    rand_sleep('long')

    # Move the mouse to the compass and click to reset the screen
    hc.move((rand_coor(coordinates['compass'][0], coordinates['compass'][2]),
             rand_coor(coordinates['compass'][1], coordinates['compass'][3])))
    rand_sleep('short') # Sleep, click, sleep

    ## Move the screen down
    # Press the down arrow between 1-5 seconds (random)
    for _ in range(randint(1,5)):
        pyautogui.keyDown('down')
    rand_sleep('quick')

    #Release the down arrow.
    pyautogui.keyUp('down')
    rand_sleep('quick')

    # Move to and click bank window
    hc.move((rand_coor(coordinates['access_bank'][0], coordinates['access_bank'][2]),
             rand_coor(coordinates['access_bank'][1], coordinates['access_bank'][3])))
    rand_sleep('short')

    # Move to and click first tab
    hc.move((rand_coor(coordinates['bank_second_tab'][0], coordinates['bank_second_tab'][2]),
             rand_coor(coordinates['bank_second_tab'][1], coordinates['bank_second_tab'][3])))
    rand_sleep('short')


    # How many logs do you have in your bank?
    # Calculates inventory runs
    for _ in range((round(amountOfLogs/27))):
        # Move to and Click first item (knife)
        hc.move((rand_coor(coordinates['bank_first_item'][0], coordinates['bank_first_item'][2]),
                 rand_coor(coordinates['bank_first_item'][1], coordinates['bank_first_item'][3])))
        rand_sleep('short')

        # Move to and click second item
        hc.move((rand_coor(coordinates['bank_second_item'][0], coordinates['bank_second_item'][2]),
                 rand_coor(coordinates['bank_second_item'][1], coordinates['bank_second_item'][3])))
        rand_sleep('short')

        # Move to and click exit bank button
        hc.move((rand_coor(coordinates['bank_exit'][0], coordinates['bank_exit'][2]),
                 rand_coor(coordinates['bank_exit'][1], coordinates['bank_exit'][3])))
        rand_sleep('short')

        # Move to and click first item in inventory
        hc.move((rand_coor(coordinates['inventory_first_item'][0], coordinates['inventory_first_item'][2]),
                 rand_coor(coordinates['inventory_first_item'][1], coordinates['inventory_first_item'][3])))
        rand_sleep('short')

        # Move to and click second item in inventory
        hc.move((rand_coor(coordinates['inventory_second_item'][0], coordinates['inventory_second_item'][2]),
                 rand_coor(coordinates['inventory_second_item'][1], coordinates['inventory_second_item'][3])))
        rand_sleep('short')

        # Move to and click fletching option
        hc.move((rand_coor(coordinates['make_shortbow'][0], coordinates['make_shortbow'][2]),
                 rand_coor(coordinates['make_shortbow'][1], coordinates['make_shortbow'][3])))
        rand_sleep('make_bow')

        # Move back in the bank
        hc.move((rand_coor(coordinates['access_bank'][0], coordinates['access_bank'][2]),
                 rand_coor(coordinates['access_bank'][1], coordinates['access_bank'][3])))
        rand_sleep('short')
        rand_sleep('bank')

        # Deposit all
        hc.move((rand_coor(coordinates['bank_deposit_all'][0], coordinates['bank_deposit_all'][2]),
                 rand_coor(coordinates['bank_deposit_all'][1], coordinates['bank_deposit_all'][3])))
        rand_sleep('short')

# Input amout of logs in the bank
main_script(7800)
