# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:18:02 2023

@author: luis mercado
"""

from PIL import Image, ImageTk
import threading
import tkinter as tk

# carga las imagenes
image1 = Image.open("picture2.jpg")
image2 = Image.open("picture1.jpg")

# Crea una ventana
window = tk.Tk()
window.geometry("1800x1220")

# Crea el tamaño de la ventana
canvas = tk.Canvas(window, width=1270, height=720)
canvas.pack()

# Crea el objeto imagen
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

canvas_image1 = canvas.create_image(100, 500, image=tk_image1)
canvas_image2 = canvas.create_image(500, 100, image=tk_image2)

# Define la funcion del movimiento de la imagen 1 izq a der
def move_image1():
    x = 0
    y = 200
    while True:
        canvas.move(canvas_image1, 5, 0)
        window.update()
        x += 5
        if x >= 800:
            x = 0
            canvas.coords(canvas_image1, x, y)

# Define la funcion de la imagen 2 arriba a abajo
def move_image2():
    x = 200
    y = 0
    while True:
        canvas.move(canvas_image2, 0, 5)
        window.update()
        y += 5
        if y >= 800:
            y = 0
            canvas.coords(canvas_image2, x, y)

# Crea un hilo
thread1 = threading.Thread(target=move_image1)
thread2 = threading.Thread(target=move_image2)

# inicia un hilo
thread1.start()
thread2.start()

# inicia el loop de tkinter
window.mainloop()
