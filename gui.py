from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from image import convert_image_to_grayscale


def create_window():
    root = Tk()
    frame = ttk.Frame(root,width=700, height=700)
    image = None
    frame.grid()

    ui_left = ttk.Frame(frame, width=250, height=250, padding=5)
    ui_left.grid(row=0, column=0)
    placeholder = ttk.Label(ui_left)
    placeholder.place(x=50, y=5)

    upload_button = ttk.Button(ui_left, text="Upload Image", command=lambda:upload_file(image, upload_button, placeholder))
    upload_button.place(x=50,y=50)
    reset_button = ttk.Button(ui_left, text="RESET", command=lambda:reset_file(image))
    reset_button.place(x=50, y=90)

    ui_right = ttk.Frame(frame, width=250, height=250, padding=5)
    ui_right.grid(row=0, column=1)
    result_box = Text(ui_right, width=30, height=30)
    result_box.pack()
    result = "testing"
    result_box.insert(1.0, result)

    root.mainloop()
    return

def upload_file(image, upload_button, placeholder):
    img_exists = False
    image = filedialog.askopenfile(mode='r').name
    if image:
        img_exists = verify_upload(image)
    print(img_exists, "after verification")
    if img_exists:
        image = Image.open(image)
        placeholder_image = ImageTk.PhotoImage(image)
        placeholder.config(image=placeholder_image)
        placeholder.image = placeholder_image
    else:
        messagebox.showerror(title="Error Uploading Image", message="The file you selected is not supported, please choose a file with an extension of .png, .jpg, or .jpeg")
        image = None

def verify_upload(path):
    extension = path[len(path)-4 : len(path)]
    return extension == ".png" or extension == '.jpg' or extension == "jpeg"


def reset_file(image):
    image = None