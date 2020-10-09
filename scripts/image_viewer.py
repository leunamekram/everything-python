import os
import tkinter as tk
from PIL import Image, ImageTk
from resizeimage import resizeimage

window = tk.Tk()
window.title("Image Viewer")
window.geometry("300x300")

picture = input(r"Drop picture here >> ")

resized = resizeimage.resize_cover(Image.open(picture), [300, 300])
image_render = ImageTk.PhotoImage(resized)
image = tk.Label(window, image = image_render)
image.pack()

window.mainloop()
