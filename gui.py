from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


def create_window():
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    image = None
    upload_button = ttk.Button(root, text="Upload Image", command=lambda:upload_image(image, upload_button))
    upload_button.place(x=50,y=50)
    root.mainloop()
    if image:
        upload_button.destroy()
        print("image uploaded")
    return

def upload_image(image, upload_button):
    img_exists = False
    image = filedialog.askopenfile(mode='r')
    if image:
        img_exists = verify_upload(image.name)
    print(img_exists, "after verification")
    if img_exists:
        upload_button.destroy()
    else:
        messagebox.showerror(title="Error Uploading Image", message="The file you selected is not supported, please choose a file with an extension of .png, .jpg, or .jpeg")
        image = None


def grab_image_with_PIL():
    image = Image.open()

def verify_upload(path):
    extension = path[len(path)-4 : len(path)]
    return extension == ".png" or extension == '.jpg' or extension == "jpeg"