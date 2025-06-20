
"""
from tkinter import *
window =Tk()
window.geometry("600x600")
window.configure(bg="red")
window.title("BIG WORld")
window.mainloop()
"""
"""
from PIL import Image
from IPython.display import display

image = Image.open("brothers.jpg")          
display(image)                         

"""
"""
ow = tk.Tk()
window.title("scale Example")
window.geometry('200x200')

scale = tk.Scale(window,from_=0,to=160,orient=tk.HORIZONTAL)
scale.pack()
window.mainloop()import tkinter as tk

wind

"""
"""
import tkinter as tk
window = tk.Tk()
window.title("Scale EX")
window.geometry("200x200")
radio_var=tk.StringVar()
radiobutton1=tk.Radiobutton(window,text="Male",variable=radio_var,value="male")
radiobutton2=tk.Radiobutton(window,text="Female",variable=radio_var,value="female")
radiobutton1.pack()
radiobutton2.pack()
window.mainloop()

"""

from tkinter import *

# Create main window
root = Tk()
root.title("4x4 Grid of Frames")
root.geometry("400x400")

# Define number of rows and columns
rows = 4
columns = 4

# Loop to create 4x4 frames
for i in range(rows):
    for j in range(columns):
        frame = Frame(root, width=100, height=100, bg="lightblue", highlightbackground="black", highlightthickness=1)
        frame.grid(row=i, column=j, padx=2, pady=2)

        # Add label inside each frame
        label = Label(frame, text=f"({i},{j})", bg="lightblue")
        label.place(relx=0.5, rely=0.5, anchor="center")

# Start the GUI loop
root.mainloop()


































