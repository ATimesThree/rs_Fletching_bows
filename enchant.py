## Import stuff
import pyautogui, math, time
from random import randint



## Import my own information
from mouse_real import move_mouse_to
from info_formulas import coordinates, rand_coor, rand_sleep

#################################################
#################################################
#################################################




def enchant_script():
    '''
    Function for enchanting rings.
    This will go through the whole function of enchanting rings as long as the setup is correct.
    :return: None
    '''


    # Some time to set up...
    amountOfLogs = int(input('How many rings do you have? '))
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

    # Move and click spellbook
    rand_sleep('insane')
    move_mouse_to(rand_coor(coordinates['tab_spellbook'][0], coordinates['tab_spellbook'][2]),
             rand_coor(coordinates['tab_spellbook'][1], coordinates['tab_spellbook'][3]))
    rand_sleep('short')

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


    # How many logs do you have in your bank?
    # Calculates inventory runs
    for _ in range((math.ceil(amountOfLogs/27.0))):
        while round_counts > 0:
            print(f'Completed rounds: {round_counts}... Script has ran for {round(((time.time()-script_timer)/60),2)} minutes...')
            break

        loop_timer = time.time()


        # Move to and click cosmic rune
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_cosmic_rune'][0], coordinates['bank_cosmic_rune'][2]),
                 rand_coor(coordinates['bank_cosmic_rune'][1], coordinates['bank_cosmic_rune'][3]))
        rand_sleep('short')

        # Move to and click emerald ring
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_emerald_ring'][0], coordinates['bank_emerald_ring'][2]),
                 rand_coor(coordinates['bank_emerald_ring'][1], coordinates['bank_emerald_ring'][3]))
        rand_sleep('short')

        # Move to and click exit bank button
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_exit'][0], coordinates['bank_exit'][2]),
                 rand_coor(coordinates['bank_exit'][1], coordinates['bank_exit'][3]))
        rand_sleep('short')

        # Move to and click the enchant spell
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['spell_enchant'][0], coordinates['spell_enchant'][2]),
                 rand_coor(coordinates['spell_enchant'][1], coordinates['spell_enchant'][3]))
        rand_sleep('short')

        # Move to and click second item in inventory
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['inventory_second_item'][0], coordinates['inventory_second_item'][2]),
                 rand_coor(coordinates['inventory_second_item'][1], coordinates['inventory_second_item'][3]))
        rand_sleep('enchant_ring')

        # Move back in the bank
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['access_bank'][0], coordinates['access_bank'][2]),
                 rand_coor(coordinates['access_bank'][1], coordinates['access_bank'][3]))
        rand_sleep('short')
        rand_sleep('bank')

        # Deposit all
        rand_sleep('insane')
        move_mouse_to(rand_coor(coordinates['bank_deposit_all'][0], coordinates['bank_deposit_all'][2]),
                 rand_coor(coordinates['bank_deposit_all'][1], coordinates['bank_deposit_all'][3]))
        rand_sleep('short')
        round_counts += 1
        all_loop_times.append((time.time()-loop_timer))
    print(f'The script ran for {round(((time.time() - script_timer)/60),2)} minutes and completed {round_counts} loops...')
    print(f'The average time per loop is: {round((sum(all_loop_times)/len(all_loop_times)),2)} seconds...')
