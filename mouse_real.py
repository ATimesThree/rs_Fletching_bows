import pyautogui
import random



def move_mouse_to(x, y):
    """Function to simulate realistic mouse movements in python. The objective of this
     will be to take in coordinates x,y and move them in a realistic manner. We
     will be passing in an x,y,  that is already 'random' so this function will
     move to the exact x,y"""
    # takes current mouse location and stores it
    curr_x, curr_y = pyautogui.position()

            # calculates the distance from current position to target position
    distance = int(((x - curr_x) ** 2 + (y - curr_y) ** 2) ** 0.5)
            # calculates a random time to make the move take based on the distance
    duration_of_move = (distance * random.uniform(0.1,3) / 2000) + 0.5
            # move the mouse to our position and takes the time of our duration just
            # calculated
    pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)



if __name__ == "__main__":
    pass
