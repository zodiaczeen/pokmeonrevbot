import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab


def screen_frozen(threshold=500):
    # Capture the first screenshot
    img1 = np.array(ImageGrab.grab(bbox=(1224, 623, 1451, 801)))
    time.sleep(0.5)  # Delay before capturing the second image

    # Load the reference image (encounter.PNG)
    img2 = cv2.imread("encounter.PNG")  # Load the image using OpenCV
    if img2 is None:
        print("Error: encounter.PNG not foadadund.")
        return False

    # Resize img2 to match the dimensions of img1 if necessary
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Calculate the absolute difference between the two images
    diff = np.sum(np.abs(img1.astype("float") - img2.astype("float")))

    # Print the difference for debugging
    print("done till screen frezze")
    

    # Return True if the difference is below the threshold
    return diff < threshold


def move_left_right():
    while True:
        pyautogui.keyDown('a')  # Press and hold 'a'
        time.sleep(2)  # Hold for 2 seconds
        pyautogui.keyUp('a')  # Release 'a'

        pyautogui.keyDown('d')  # Press and hold 'd'
        time.sleep(2)  # Hold for 2 seconds
        pyautogui.keyUp('d')  # Release 'd'

        if screen_frozen():
            
            print("Battle detected!")
            handle_battle()


def is_pokemon(target_image="pic.png", threshold=500000):
    print("Checking for Pokémon...")
    imgw = (983, 443, 1121, 516)
    screenshot = np.array(ImageGrab.grab(bbox=imgw))  # Capture the region
    img2 = cv2.imread(target_image)  # Load the target Pokémon image

    if img2 is None:
        print(f"Error: {target_image} not found.")
        return False

    # Resize img2 to match the dimensions of the screenshot
    # img2 = cv2.resize(img2, (screenshot.shape[1], screenshot.shape[0]))

    # Calculate the absolute difference between the two images
    diff = np.sum(np.abs(screenshot.astype("float") - img2.astype("float")))
    print(f"Screen difference: {diff}")

    # Return True if the difference is below the thresholdadad
    if diff < threshold:
        print("Pokémon matched!")
        return True
    else:
        print("No match found.")
        return False


def handle_battle():
    time.sleep(1)
    if is_pokemon("pic.png"):
        print("Charmander found! Come catch it!")
        pyautogui.alert("Charmander found! Come catch it!", title="Pokémon Alert") 
        
        
        # Uncomment the line below if you want to play a sound
        # playsound('shiny_alert.mp3')
        while True:
            time.sleep(10)  # Wait indefinitely
    else:
        run_away()


def run_away():
    time.sleep(1)
    print("Running away from the encounter...")
      # Move to the "Run" button
    pyautogui.click()
    pyautogui.moveTo(1400, 767)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(500, 767)
    time.sleep(0.5)
     # Click the "Run" button
    time.sleep(0.5)  # Wait for the action to complete


if __name__ == "__main__":
    time.sleep(5) 
    
     # Initial delay before starting
    move_left_right()
