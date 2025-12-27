import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# ---------------- ENCRYPT / DECRYPT LOGIC ----------------
def process_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)


# ---------------- GUI FUNCTIONS ----------------
def select_image():
    global image_path
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if image_path:
        file_label.config(text=os.path.basename(image_path))


def encrypt_image():
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return

    try:
        key = int(key_entry.get())
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Key must be between 0 and 255.")
        return

    output_path = "encrypted_image.png"
    process_image(image_path, output_path, key)
    messagebox.showinfo("Success", "Image encrypted successfully!")


def decrypt_image():
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return

    try:
        key = int(key_entry.get())
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Key must be between 0 and 255.")
        return

    output_path = "decrypted_image.png"
    process_image(image_path, output_path, key)
    messagebox.showinfo("Success", "Image decrypted successfully!")


# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("420x300")
root.resizable(False, False)

image_path = ""

title = tk.Label(root, text="Image Encryption Tool", font=("Arial", 16, "bold"))
title.pack(pady=10)

select_btn = tk.Button(root, text="Select Image", command=select_image, width=20)
select_btn.pack(pady=5)

file_label = tk.Label(root, text="No file selected", fg="gray")
file_label.pack()

key_label = tk.Label(root, text="Enter Encryption Key (0-255):")
key_label.pack(pady=5)

key_entry = tk.Entry(root, width=20)
key_entry.pack()

encrypt_btn = tk.Button(root, text="Encrypt Image", command=encrypt_image, bg="#4CAF50", fg="white", width=20)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt Image", command=decrypt_image, bg="#2196F3", fg="white", width=20)
decrypt_btn.pack()

footer = tk.Label(root, text="For Educational Use Only", font=("Arial", 9), fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
