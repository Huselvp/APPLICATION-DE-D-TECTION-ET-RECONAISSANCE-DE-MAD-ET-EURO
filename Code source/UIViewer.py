import tkinter as tk
from tkinter import filedialog

import PIL.Image as pil
from PIL import ImageTk

# function to be called when button is clicked
# that will open an image in main window
# from a file browser
import Extractor


def openImage():
    global total_label
    global img

    # get filename
    filename = filedialog.askopenfilename()

    # open image
    total_label.grid_forget()
    total_label = tk.Label(root, text="En traitment...")
    total_label.grid(row=0, column=1)
    img_n = pil.open(filename)
    img_n = ImageTk.PhotoImage(img_n)
    img.grid_forget()
    img = tk.Label(root, image=img_n)
    img.image = img_n
    img.grid(row=1, column=0, columnspan=3)

    # load image
    new_image, mad_val, euro_val = Extractor.extract(filename)
    new_image = pil.fromarray(new_image)

    # resize image
    new_image = new_image.resize((root.winfo_width() - 5, new_image.height * (root.winfo_width() - 5) // new_image.width))
    root.geometry(str(new_image.width + 5) + "x" + str(new_image.height + 55))

    # convert image to tkinter image
    new_image = ImageTk.PhotoImage(new_image)

    # set the image to the label
    total_label.grid_forget()
    total_label = tk.Label(root, text="Total: " + str(euro_val) + " Euro | " + str(mad_val) + " Mad")
    total_label.grid(row=0, column=1)
    img.grid_forget()
    img = tk.Label(root, image=new_image)
    img.image = new_image
    img.grid(row=1, column=0, columnspan=3)


root = tk.Tk()
root.geometry("600x600")
root.title('Euro Mad Predictor')

total_label = tk.Label(root, text="Total: 0 Euro | 0 Mad")
total_label.grid(row=0, column=1)
img = tk.Label(text="Select an image")
img.grid(row=1, column=0, columnspan=3)

button_load_img = tk.Button(root, text="Load Image", command=lambda: openImage())
button_exit = tk.Button(root, text="Exit Program", command=root.quit)

button_load_img.grid(row=2, column=1)
button_load_img.config(width=10, height=1)
root.mainloop()
