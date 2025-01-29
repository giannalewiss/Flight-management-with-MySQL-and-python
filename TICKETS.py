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

def insert_tickets():
    PNR_NO = PNR_NO_entry.get()
    SEATNO = SEATNO_entry.get()
    CLASS = CLASS_entry.get()
    GATENO = GATENO_entry.get()

    if PNR_NO and SEATNO and CLASS and GATENO:
        insert_query = "INSERT INTO TICKETS (PNR_NO, SEATNO, CLASS, GATENO) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (PNR_NO, SEATNO, CLASS, GATENO))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def update_tickets():
    new_PNR_NO = PNR_NO_entry.get()
    new_SEATNO = SEATNO_entry.get()
    new_CLASS = CLASS_entry.get()
    new_GATENO = GATENO_entry.get()

    if new_PNR_NO and new_SEATNO and new_CLASS and new_GATENO:
        sql = "UPDATE TICKETS SET SEATNO = %s, CLASS = %s, GATENO = %s WHERE PNR_NO = %s"
        values = (new_SEATNO, new_CLASS, new_GATENO, new_PNR_NO)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_tickets():
    new_PNR_NO = PNR_NO_entry.get()

    if new_PNR_NO:
        sql = "DELETE FROM TICKETS WHERE PNR_NO = %s"
        values = (new_PNR_NO,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
    else:
        messagebox.showerror("Error", "Please enter a valid PNR_NO.")

def show_tickets():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM TICKETS")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"PNR_NO: {record[0]}, SEATNO: {record[1]}, CLASS: {record[2]}, GATENO: {record[3]}")

window = tk.Tk()
window.title("TICKET DETAILS")
label_style = ttk.Style()
label_style.configure("TICKETS.WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")

PNR_NO_label = tk.Label(window, text="PASSENGER NUMBER:", bg="lightblue")
PNR_NO_entry = tk.Entry(window)

SEATNO_label = tk.Label(window, text="SEAT NUMBER:", bg="lightblue")
SEATNO_entry = tk.Entry(window)

CLASS_label = tk.Label(window, text="CLASS:", bg="lightblue")
CLASS_entry = tk.Entry(window)

GATENO_label = tk.Label(window, text="GATE NUMBER:", bg="lightblue")
GATENO_entry = tk.Entry(window)

insert_button = tk.Button(window, text="Insert Data", foreground="black", background="lightyellow", command=insert_tickets)
update_button = tk.Button(window, text="Update Data", foreground="black", background="grey", command=update_tickets)
delete_button = tk.Button(window, text="Delete Data", foreground="black", background="pink", command=delete_tickets)
show_button = tk.Button(window, text="Show Records", foreground="black", background="lightgreen", command=show_tickets)

listbox = tk.Listbox(window, width=50)

PNR_NO_label.pack()
PNR_NO_entry.pack()

SEATNO_label.pack()
SEATNO_entry.pack()

CLASS_label.pack()
CLASS_entry.pack()

GATENO_label.pack()
GATENO_entry.pack()

insert_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)
show_button.pack(pady=5)

listbox.pack()

window.mainloop()
conn.close()
