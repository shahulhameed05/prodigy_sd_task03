import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if name and phone and email:
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        update_contact_list()
        messagebox.showinfo("Success", f"Contact {name} added.")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields must be filled out.")

def edit_contact():
    name = entry_name.get()
    if name in contacts:
        phone = entry_phone.get()
        email = entry_email.get()
        if phone and email:
            contacts[name] = {'phone': phone, 'email': email}
            save_contacts(contacts)
            update_contact_list()
            messagebox.showinfo("Success", f"Contact {name} updated.")
        else:
            messagebox.showwarning("Input Error", "Phone and email must be filled out.")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        update_contact_list()
        messagebox.showinfo("Success", f"Contact {name} deleted.")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

def on_contact_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        name = event.widget.get(index)
        contact = contacts[name]
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(tk.END, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(tk.END, contact['email'])

# Load contacts from file
contacts = load_contacts()

# Create main application window
root = tk.Tk()
root.title("Contact Management System")

# Create and place labels and entry widgets for contact details
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Create and place buttons for adding, editing, and deleting contacts
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Edit Contact", command=edit_contact).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=3, column=2, padx=10, pady=10)

# Create and place listbox to display contacts
listbox_contacts = tk.Listbox(root)
listbox_contacts.grid(row=0, column=3, rowspan=4, padx=10, pady=5)
listbox_contacts.bind('<<ListboxSelect>>', on_contact_select)

# Populate the listbox with contacts
update_contact_list()

# Run the application
root.mainloop()
