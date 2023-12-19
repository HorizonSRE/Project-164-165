from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


root = Tk()
root.configure(bg="lightgray")  

image_label = Label(root, bg="white", highlightthickness=1, highlightcolor="white")
image_label.place(relx=0.5, rely=0.2, anchor=CENTER)


img_path = ""


def open_file():
    global img_path, img

    img_path = askopenfilename(title="Open Image File",
                             filetypes=[("Image files", "*.jpg *.gif *.png *.jpeg")])

    if img_path:
        
        img = ImageTk.PhotoImage(Image.open(img_path))

        
        image_label.configure(image=img)

        
        if image_label.image:
            image_label.image.close()


open_button = Button(root, text="Open Image",
                    font=("Arial", 12, "bold"),
                    bg="skyblue", fg="white", relief="solid",
                    padx=10, pady=5,
                    command=open_file)
open_button.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()