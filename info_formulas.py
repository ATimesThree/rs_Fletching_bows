from random import randint
from pyclick import HumanClicker
import time, random

##############################################################################
#########################                       ##############################
######################### INFORMATION GOES HERE ##############################
#########################                       ##############################
##############################################################################

##  All coordinates goes in here. Format: x1,y1,x2,y2  ##
coordinates = {'bank_second_tab' : [445, 119, 470, 137], # Second sloth in the bank
               'bank_first_item' : [422, 165, 430, 178], # First item in the bank (top left)
               'bank_second_item' : [462, 162, 479, 177], # Second item in the bank (right side of the first item)
               'bank_deposit_all' : [769, 375, 790, 391], # 'Deposit all' button in the bank
               'access_bank' : [592,159, 637, 172], # Area clicked to access the bank in just one click
               'inventory_first_item' : [905, 293, 926, 306], # First item in the inventory (top left)
               'inventory_second_item' : [953, 293, 970, 307], # Second item in the inventory (right side of the first item)
               'compass' : [887,82,908,97], # Click the compass to reset the screen
               'bank_exit':[818,92,826,97], # Exit button in the bank
               'make_longbow': [659,469,736,520], # The box to make longbow
               'make_shortbow': [569,469,637,520], # The box to make shortbow
               }


##############################################################################
#########################                       ##############################
#########################  FORMULAS GOES HERE   ##############################
#########################                       ##############################
##############################################################################

def rand_coor(coor1, coor2):
    '''
    Takes in two coordinates (x1,x2) and output a random point bewteen these values.
    :param x1: 1    Example --> access_bank[0]
    :param y1: 7    Example --> access_bank[2]
    :return: 3
    '''
    new_coor = randint(coor1,coor2)
    return new_coor


## DIfferent pause times - some followed by a click
def rand_sleep(text):
    hc = HumanClicker()

    if text == 'short':
        time.sleep(random.uniform(0.2,1))
        hc.click()
        time.sleep(random.uniform(0.2, 1))
    elif text == 'medium':
        time.sleep(randint(1,5))
    elif text == 'long':
        time.sleep(random.uniform(4,8.5))
    elif text == 'bank':
        time.sleep(random.uniform(1,3))
    elif text == 'quick':
        time.sleep(random.uniform(0.2,1.2))
    elif text == 'sleep_shortbow':
        time.sleep(random.uniform(30,35))
    elif text == 'make_bow':
        time.sleep(random.uniform(0.2, 1))
        hc.click()
        time.sleep(random.uniform(49,51))
    else:
        return False


