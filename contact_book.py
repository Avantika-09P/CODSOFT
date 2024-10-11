import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Contact dictionary to store contact details
contacts = {}

# Functions for contact management
def add_contact():
    name = name_entry.get().strip().lower()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if not name or not phone or not email or not address:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if name in contacts:
        messagebox.showerror("Error", "A contact with this name already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()

def view_contacts():
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_listbox.insert(tk.END, f"Name: {name.capitalize()}, Phone: {details['phone']}")

def search_contact():
    search_term = search_entry.get().strip().lower()
    found = False
    for name, details in contacts.items():
        if search_term == name or search_term == details['phone']:
            messagebox.showinfo("Contact Found", f"Name: {name.capitalize()}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            found = True
            break
    if not found:
        messagebox.showwarning("Not Found", "No contact found with the given name or phone number.")

def update_contact():
    name = name_entry.get().strip().lower()
    
    if name in contacts:
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        address = address_entry.get().strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    name = name_entry.get().strip().lower()
    
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x600")

# Load background image with error handling
try:
    bg_image = PhotoImage(file="background.png")  # Ensure the file path is correct
    background_label = tk.Label(root, image=bg_image)
    background_label.place(relwidth=1, relheight=1)
except tk.TclError:
    print("Background image not found. Proceeding without it.")
    root.configure(bg="#F0F8FF")  # Default background color if image is missing

# Style settings
label_font = ("Arial", 12, "bold")
entry_bg = "#F0F8FF"
button_bg = "#4682B4"
button_fg = "#FFFFFF"

# Labels and Entries for adding/updating contacts
tk.Label(root, text="Name:", bg=entry_bg, font=label_font).pack(pady=5)
name_entry = tk.Entry(root, bg=entry_bg)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:", bg=entry_bg, font=label_font).pack(pady=5)
phone_entry = tk.Entry(root, bg=entry_bg)
phone_entry.pack(pady=5)

tk.Label(root, text="Email:", bg=entry_bg, font=label_font).pack(pady=5)
email_entry = tk.Entry(root, bg=entry_bg)
email_entry.pack(pady=5)

tk.Label(root, text="Address:", bg=entry_bg, font=label_font).pack(pady=5)
address_entry = tk.Entry(root, bg=entry_bg)
address_entry.pack(pady=5)

# Buttons for operations
tk.Button(root, text="Add Contact", command=add_contact, bg=button_bg, fg=button_fg, font=label_font).pack(pady=10)
tk.Button(root, text="Update Contact", command=update_contact, bg=button_bg, fg=button_fg, font=label_font).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg=button_bg, fg=button_fg, font=label_font).pack(pady=5)

# Listbox to display contacts
tk.Label(root, text="Contacts List:", bg=entry_bg, font=label_font).pack(pady=10)
contact_listbox = tk.Listbox(root, height=8, width=50, bg=entry_bg)
contact_listbox.pack(pady=5)

# Search Section
tk.Label(root, text="Search by Name/Phone:", bg=entry_bg, font=label_font).pack(pady=5)
search_entry = tk.Entry(root, bg=entry_bg)
search_entry.pack(pady=5)
tk.Button(root, text="Search", command=search_contact, bg=button_bg, fg=button_fg, font=label_font).pack(pady=5)

# Run the GUI
root.mainloop()


