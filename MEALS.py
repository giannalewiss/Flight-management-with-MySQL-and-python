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

def insert_meals():
    S_NO = S_NO_entry.get()
    ITEM = ITEM_entry.get()
    RATE = RATE_entry.get()
    F_NO = F_NO_entry.get()

    insert_query = "INSERT INTO MEALS (S_NO, ITEM, RATE, F_NO) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (S_NO, ITEM, RATE, F_NO))
    conn.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")

def update_meals():
    selected_S_NO = S_NO_entry.get()
    new_ITEM = ITEM_entry.get()
    new_RATE = RATE_entry.get()
    new_F_NO = F_NO_entry.get()

    if selected_S_NO and new_ITEM and new_RATE and new_F_NO:
        sql = "UPDATE MEALS SET ITEM = %s, RATE = %s, F_NO = %s WHERE S_NO = %s"
        values = (new_ITEM, new_RATE, new_F_NO, selected_S_NO)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        S_NO_entry.delete(0, tk.END)
        ITEM_entry.delete(0, tk.END)
        RATE_entry.delete(0, tk.END)
        F_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_meals():
    selected_S_NO = S_NO_entry.get()

    if selected_S_NO:
        sql = "DELETE FROM MEALS WHERE S_NO = %s"
        values = (selected_S_NO,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
        S_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a valid S_NUMBER.")

def show_meals():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM MEALS")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"S_NO: {record[0]}, ITEM: {record[1]}, RATE: {record[2]}, F_NO: {record[3]}")

window = tk.Tk()
window.title("MEAL DETAILS")
label_style = ttk.Style()
label_style.configure("MEALS WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")

S_NO_label = tk.Label(window, text="S_NUMBER:", bg="lightblue")
S_NO_entry = tk.Entry(window)

ITEM_label = tk.Label(window, text="ITEM NAME:", bg="lightblue")
ITEM_entry = tk.Entry(window)

RATE_label = tk.Label(window, text="RATE:", bg="lightblue")
RATE_entry = tk.Entry(window)

F_NO_label = tk.Label(window, text="FLIGHT NUMBER:", bg="lightblue")
F_NO_entry = tk.Entry(window)

insert_button = tk.Button(window, text="Insert Data", foreground="black", background="lightyellow", command=insert_meals)
update_button = tk.Button(window, text="Update Data", foreground="black", background="grey", command=update_meals)
delete_button = tk.Button(window, text="Delete Data", foreground="black", background="pink", command=delete_meals)
show_button = tk.Button(window, text="Show Records", foreground="black", background="lightgreen", command=show_meals)

listbox = tk.Listbox(window, width=50)

S_NO_label.pack()
S_NO_entry.pack()

ITEM_label.pack()
ITEM_entry.pack()

RATE_label.pack()
RATE_entry.pack()

F_NO_label.pack()
F_NO_entry.pack()

insert_button.pack(pady=5)  
update_button.pack(pady=5)  
delete_button.pack(pady=5)  
show_button.pack(pady=5)

listbox.pack()

window.mainloop()
conn.close()