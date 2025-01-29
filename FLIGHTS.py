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

create_table_query = """
CREATE TABLE IF NOT EXISTS FLIGHTS (
    F_NO VARCHAR(10) PRIMARY KEY,
    FNAME VARCHAR(20),
    DEPT_TIME VARCHAR(10),
    DEPT_PLACE VARCHAR(20),
    ARRIVE_TIME VARCHAR(10),
    ARRIVE_PLACE VARCHAR(20),
    PNR_NO VARCHAR(10),
    FOREIGN KEY(PNR_NO) REFERENCES PASSENGER(PNR_NO)
)
"""
cursor.execute(create_table_query)
conn.commit()

def insert_flights():
    F_NO = F_NO_entry.get()
    FNAME = FNAME_entry.get()
    DEPT_TIME = DEPT_TIME_entry.get()
    DEPT_PLACE = DEPT_PLACE_entry.get()
    ARRIVE_TIME = ARRIVE_TIME_entry.get()
    ARRIVE_PLACE = ARRIVE_PLACE_entry.get()
    PNR_NO = PNR_NO_entry.get()

    insert_query = "INSERT INTO FLIGHTS(F_NO, FNAME, DEPT_TIME, DEPT_PLACE, ARRIVE_TIME, ARRIVE_PLACE, PNR_NO) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (F_NO, FNAME, DEPT_TIME, DEPT_PLACE, ARRIVE_TIME, ARRIVE_PLACE, PNR_NO))
    conn.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")

def update_flights():
    selected_fno = F_NO_entry.get()
    new_fname = FNAME_entry.get()
    new_depttime = DEPT_TIME_entry.get()
    new_deptplace = DEPT_PLACE_entry.get()
    new_arrivetime = ARRIVE_TIME_entry.get()
    new_arriveplace = ARRIVE_PLACE_entry.get()
    new_pnrno = PNR_NO_entry.get()

    if selected_fno and new_fname and new_depttime and new_deptplace and new_arrivetime and new_arriveplace and new_pnrno:
        sql = "UPDATE FLIGHTS SET DEPT_TIME = %s, ARRIVE_TIME = %s WHERE F_NO = %s"
        values = (new_depttime, new_arrivetime, selected_fno)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        DEPT_TIME_entry.delete(0, tk.END)
        ARRIVE_TIME_entry.delete(0, tk.END)
        F_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def count_passengers_in_flight():
    selected_fno = F_NO_entry.get()

    if selected_fno:
        sql = "SELECT COUNT(*) FROM FLIGHTS WHERE F_NO = %s"
        cursor.execute(sql, (selected_fno,))
        count = cursor.fetchone()[0]

        messagebox.showinfo("Passenger Count", f"Number of passengers on Flight {selected_fno}: {count}")
    else:
        messagebox.showerror("Error", "Please enter a flight number.")

def show_flights():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM FLIGHTS")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"F_NO: {record[0]} FNAME: {record[1]}, DEPT_TIME: {record[2]}, DEPT_PLACE: {record[3]}, ARRIVE_TIME: {record[4]}, ARRIVE_PLACE: {record[5]}, PNR_NO: {record[6]}")

window = tk.Tk()
window.title("FLIGHT DETAILS")
label_style = ttk.Style()
label_style.configure("FLIGHTS WINDOW", font=("Helvetica", 20))
window.configure(bg="pink")

F_NO_label = tk.Label(window, text="FLIGHT NUMBER:", bg="pink")
F_NO_entry = tk.Entry(window)

FNAME_label = tk.Label(window, text="FLIGHT NAME:", bg="pink")
FNAME_entry = tk.Entry(window)

DEPT_TIME_label = tk.Label(window, text="DEPARTURE TIME:", bg="pink")
DEPT_TIME_entry = tk.Entry(window)

DEPT_PLACE_label = tk.Label(window, text="DEPARTURE PLACE:", bg="pink")
DEPT_PLACE_entry = tk.Entry(window)

ARRIVE_TIME_label = tk.Label(window, text="ARRIVAL TIME:", bg="pink")
ARRIVE_TIME_entry = tk.Entry(window)

ARRIVE_PLACE_label = tk.Label(window, text="ARRIVAL PLACE", bg="pink")
ARRIVE_PLACE_entry = tk.Entry(window)

PNR_NO_label = tk.Label(window, text="PASSENGER NUMBER ", bg="pink")
PNR_NO_entry = tk.Entry(window)


count_passengers_button = tk.Button(window, text="Count Passengers", foreground="black", background="lightblue", command=count_passengers_in_flight)
insert_button = tk.Button(window, text="Insert Data", foreground="black", background="lightyellow", command=insert_flights)
update_button = tk.Button(window, text="Update Data", foreground="black", background="orange", command=update_flights)
show_button = tk.Button(window, text="Show Records", foreground="black", background="lightgreen", command=show_flights)
listbox = tk.Listbox(window, width=50)

F_NO_label.pack()
F_NO_entry.pack()

FNAME_label.pack()
FNAME_entry.pack()

DEPT_TIME_label.pack()
DEPT_TIME_entry.pack()

DEPT_PLACE_label.pack()
DEPT_PLACE_entry.pack()

ARRIVE_TIME_label.pack()
ARRIVE_TIME_entry.pack()

ARRIVE_PLACE_label.pack()
ARRIVE_PLACE_entry.pack()

PNR_NO_label.pack()
PNR_NO_entry.pack()

insert_button.pack()
update_button.pack()
show_button.pack()

insert_button.pack(pady=5)  
update_button.pack(pady=5) 
count_passengers_button.pack(pady=5) 
show_button.pack(pady=5) 

listbox.pack()

window.mainloop()
conn.close()