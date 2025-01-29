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

def insert_payment():
    MODE = MODE_entry.get()
    AMOUNT = AMOUNT_entry.get()
    PNR_NO = PNR_NO_entry.get()

    insert_query = "INSERT INTO PAYMENT (MODE, AMOUNT, PNR_NO) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (MODE, AMOUNT, PNR_NO))
    conn.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")

def update_payment():
    new_MODE = MODE_entry.get()
    new_AMOUNT = AMOUNT_entry.get()
    new_PNR_NO = PNR_NO_entry.get()

    if new_MODE and new_AMOUNT and new_PNR_NO:
        sql = "UPDATE PAYMENT SET AMOUNT = %s WHERE PNR_NO = %s"
        values = (new_AMOUNT, new_PNR_NO)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        MODE_entry.delete(0, tk.END)
        AMOUNT_entry.delete(0, tk.END)
        PNR_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_payment():
    new_PNR_NO = PNR_NO_entry.get()

    if new_PNR_NO:
        sql = "DELETE FROM PAYMENT WHERE PNR_NO = %s"
        values = (new_PNR_NO,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
        PNR_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a valid PNR_NUMBER.")

def show_payment():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM PAYMENT")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"MODE: {record[0]}, AMOUNT: {record[1]}, PNR_NO: {record[2]}")

window = tk.Tk()
window.title("PAYMENT DETAILS")
label_style = ttk.Style()
label_style.configure("PAYMENT.WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")

MODE_label = tk.Label(window, text="MODE OF PAYMENT:", bg="lightblue")
MODE_entry = tk.Entry(window)

AMOUNT_label = tk.Label(window, text="TOTAL AMOUNT:", bg="lightblue")
AMOUNT_entry = tk.Entry(window)

PNR_NO_label = tk.Label(window, text="PNR_NO", bg="lightblue")
PNR_NO_entry = tk.Entry(window)

insert_button = tk.Button(window, text="Insert Data", foreground="black", background="lightyellow", command=insert_payment)
update_button = tk.Button(window, text="Update Data", foreground="black", background="orange", command=update_payment)
delete_button = tk.Button(window, text="Delete Data", foreground="black", background="pink", command=delete_payment)
show_button = tk.Button(window, text="Show Records", foreground="black", background="lightgreen", command=show_payment)

listbox = tk.Listbox(window, width=50)

MODE_label.pack()
MODE_entry.pack()

AMOUNT_label.pack()
AMOUNT_entry.pack()

PNR_NO_label.pack()
PNR_NO_entry.pack()

insert_button.pack(pady=5)  
update_button.pack(pady=5)  
delete_button.pack(pady=5)  
show_button.pack(pady=5)

listbox.pack()

window.mainloop()
conn.close()
