# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:18:02 2023

@author: luis mercado
"""

from PIL import Image, ImageTk
import threading
import tkinter as tk

# Load the images
image1 = Image.open("picture2.jpg")
image2 = Image.open("picture1.jpg")

# Create the tkinter window
window = tk.Tk()
window.geometry("1200x720")

# Create the tkinter canvas
canvas = tk.Canvas(window, width=1200, height=700)
canvas.pack()

# Create the tkinter image objects
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

# Create the tkinter image objects on the canvas
canvas_image1 = canvas.create_image(0, 500, image=tk_image1)
canvas_image2 = canvas.create_image(500, 0, image=tk_image2)

# Define the function to move image1 right to left
def move_image1():
    x = 0
    y = 300
    while True:
        canvas.move(canvas_image1, 5, 0)
        window.update()
        x += 5
        if x >= 600:
            x = 0
            canvas.coords(canvas_image1, x, y)

# Define the function to move image2 up to down
def move_image2():
    x = 300
    y = 0
    while True:
        canvas.move(canvas_image2, 0, 5)
        window.update()
        y += 5
        if y >= 600:
            y = 0
            canvas.coords(canvas_image2, x, y)

# Create the threads
thread1 = threading.Thread(target=move_image1)
thread2 = threading.Thread(target=move_image2)

# Start the threads
thread1.start()
thread2.start()

# Start the tkinter main loop
window.mainloop()
