from tkinter import *
import pyautogui


root = Tk()
root.geomentry("500x500")

def take_a_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save()


button = Button(root,text="Take a Screenshot",bg="yellow")
button.pack()




root.mainloop()
