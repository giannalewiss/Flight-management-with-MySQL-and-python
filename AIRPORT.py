import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="gianna",
    password="gianna",
    database="AIRLINES"
)
cursor = conn.cursor()

def insert_airport():
    ACODE = ACODE_entry.get()
    ANAME = ANAME_entry.get()

    if ACODE and ANAME:
        insert_query = "INSERT INTO AIRPORT (ACODE, ANAME) VALUES (%s, %s)"
        cursor.execute(insert_query, (ACODE, ANAME))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def update_airport():
    new_ACODE = ACODE_entry.get()
    new_ANAME = ANAME_entry.get()

    if new_ACODE and new_ANAME:
        sql = "UPDATE AIRPORT SET ANAME = %s WHERE ACODE = %s"
        values = (new_ANAME, new_ACODE)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_airport():
    new_ACODE = ACODE_entry.get()

    if new_ACODE:
        sql = "DELETE FROM AIRPORT WHERE ACODE = %s"
        values = (new_ACODE,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
    else:
        messagebox.showerror("Error", "Please enter a valid ACODE.")

def show_airport():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM AIRPORT")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"ACODE: {record[0]}, ANAME: {record[1]}")

window = tk.Tk()
window.title("AIRPORT DETAILS")
label_style = ttk.Style()
label_style.configure("AIRPORT.WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")

ACODE_label = tk.Label(window, text="AIRPORT CODE:", bg="lightblue")
ACODE_entry = tk.Entry(window)

ANAME_label = tk.Label(window, text="AIRPORT NAME:", bg="lightblue")
ANAME_entry = tk.Entry(window)

insert_button = tk.Button(window, text="Insert Data", foreground="black", background="lightyellow", command=insert_airport)
update_button = tk.Button(window, text="Update Data", foreground="black", background="grey", command=update_airport)
delete_button = tk.Button(window, text="Delete Data", foreground="black", background="pink", command=delete_airport)
show_button = tk.Button(window, text="Show Records", foreground="black", background="lightgreen", command=show_airport)

listbox = tk.Listbox(window, width=50)

ACODE_label.pack()
ACODE_entry.pack()

ANAME_label.pack()
ANAME_entry.pack()

insert_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)
show_button.pack(pady=5)

listbox.pack()

window.mainloop()
conn.close()
