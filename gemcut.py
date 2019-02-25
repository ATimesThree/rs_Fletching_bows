## Import stuff
import pyautogui, math, time
from random import randint



## Import my own information
from mouse_real import move_mouse_to
from info_formulas import coordinates, rand_coor, rand_sleep

#################################################
#################################################
#################################################


def gemcutter_script():
    '''
    Function for Fletching longbows (u).
    This will go through the whole function of fletching longbows(u) as long as the setup is correct.
    :return: None
    '''


    # Some time to set up...
    amountOfLogs = int(input('How many logs do you have? '))
    print('Starting script.. Make yourself ready...')
    round_counts = 0 #How many times it completes the loop
    script_timer = time.time() # Timer
    all_loop_times = []

    # Some time to set up...
    rand_sleep('long')



    # Move the mouse to the compass and click to reset the screen
    rand_sleep('insane')
    move_mouse_to(rand_coor(coordinates['compass'][0], coordinates['compass'][2]),
             rand_coor(coordinates['compass'][1], coordinates['compass'][3]))
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
    rand_sleep('insane')
    move_mouse_to(rand_coor(coordinates['access_bank'][0], coordinates['access_bank'][2]),
             rand_coor(coordinates['access_bank'][1], coordinates['access_bank'][3]))
    rand_sleep('short')

    # Move to and click first tab
    rand_sleep('insane')
    move_mouse_to(rand_coor(coordinates['bank_second_tab'][0], coordinates['bank_second_tab'][2]),
             rand_coor(coordinates['bank_second_tab'][1], coordinates['bank_second_tab'][3]))
    rand_sleep('short')

    # Move to and Click first item (knife)
    rand_sleep('insane')
    move_mouse_to(rand_coor(coordinates['bank_first_item'][0], coordinates['bank_first_item'][2]),
                  rand_coor(coordinates['bank_first_item'][1], coordinates['bank_first_item'][3]))
    rand_sleep('short')


    # How many logs do you have in your bank?
    # Calculates inventory runs
    for _ in range((math.ceil(amountOfLogs/26.0))):
        while round_counts > 0:
            print(f'Completed rounds: {round_counts}... Script has ran for {round(((time.time()-script_timer)/60),2)} minutes...')
            break

        loop_timer = time.time()


        # Move to and click second item
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_second_item'][0], coordinates['bank_second_item'][2]),
                 rand_coor(coordinates['bank_second_item'][1], coordinates['bank_second_item'][3]))
        rand_sleep('short')

        # Move to and click exit bank button
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_exit'][0], coordinates['bank_exit'][2]),
                 rand_coor(coordinates['bank_exit'][1], coordinates['bank_exit'][3]))
        rand_sleep('short')

        # Move to and click first item in inventory
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['inventory_first_item'][0], coordinates['inventory_first_item'][2]),
                 rand_coor(coordinates['inventory_first_item'][1], coordinates['inventory_first_item'][3]))
        rand_sleep('short')

        # Move to and click second item in inventory
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['inventory_second_item'][0], coordinates['inventory_second_item'][2]),
                 rand_coor(coordinates['inventory_second_item'][1], coordinates['inventory_second_item'][3]))
        rand_sleep('short')

        # Move to and click cut gem option
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['gem_cutting'][0], coordinates['gem_cutting'][2]),
                 rand_coor(coordinates['gem_cutting'][1], coordinates['gem_cutting'][3]))
        rand_sleep('cut_gem')

        # Move back in the bank
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['access_bank'][0], coordinates['access_bank'][2]),
                 rand_coor(coordinates['access_bank'][1], coordinates['access_bank'][3]))
        rand_sleep('short')
        rand_sleep('bank')

        round_counts += 1
        all_loop_times.append((time.time()-loop_timer))
    print(f'The script ran for {round(((time.time() - script_timer)/60),2)} minutes and completed {round_counts} loops...')
    print(f'The average time per loop is: {round((sum(all_loop_times)/len(all_loop_times)),2)} seconds...')
