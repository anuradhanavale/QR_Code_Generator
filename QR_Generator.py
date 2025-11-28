import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_qr():
    text = data_var.get().strip()
    filename = filename_var.get().strip()

    if not filename:
        messagebox.showerror("Error", "Please enter a file name.")
        return

    if not text:
        messagebox.showerror("Error", "QR content cannot be empty.")
        return

    folder = filedialog.askdirectory()
    if not folder:
        return  # user canceled

    try:
        qr_img = qrcode.make(text)
        save_path = f"{folder}/{filename}.png"
        qr_img.save(save_path)
        messagebox.showinfo("Success", f"QR code saved at:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# --- UI Setup ---
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("380x200")
root.resizable(False, False)

data_var = tk.StringVar()
filename_var = tk.StringVar()

tk.Label(root, text="Save As (filename)").grid(row=0, column=0, padx=20, pady=10, sticky="w")
tk.Entry(root, textvariable=filename_var, width=30).grid(row=1, column=0, padx=20)

tk.Label(root, text="QR Content (text inside QR)").grid(row=2, column=0, padx=20, pady=10, sticky="w")
tk.Entry(root, textvariable=data_var, width=30).grid(row=3, column=0, padx=20)

tk.Button(root, text="Generate QR Code", command=generate_qr, width=30, bg="gray").grid(
    row=4, column=0, pady=20
)

root.mainloop()
