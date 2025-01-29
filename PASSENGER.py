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

def insert_passenger():
    PNR_NO = PNR_NO_entry.get()
    PNAME = PNAME_entry.get()
    PHONE = PHONE_entry.get()
    EMAIL = EMAIL_entry.get()
    AGE = AGE_entry.get()
    GENDER = gender_var.get()

    if not (PNR_NO and PNAME and PHONE and EMAIL and AGE and GENDER):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    insert_query = "INSERT INTO PASSENGER (PNR_NO, PNAME, PHONE, EMAIL, AGE, GENDER) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (PNR_NO, PNAME, PHONE, EMAIL, AGE, GENDER))
    conn.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")
    clear_fields()

def update_passenger():
    selected_pnrno = PNR_NO_entry.get()
    new_name = PNAME_entry.get()
    new_phone = PHONE_entry.get()
    new_email = EMAIL_entry.get()
    new_age = AGE_entry.get()
    new_gender = gender_var.get()

    if not (selected_pnrno and new_name and new_phone and new_email and new_age and new_gender):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if selected_pnrno and new_name and new_phone and new_email and new_age and new_gender:
        sql = "UPDATE PASSENGER SET PNAME = %s, PHONE = %s, EMAIL = %s, AGE = %s, GENDER = %s WHERE PNR_NO = %s"
        values = (new_name, new_phone, new_email, new_age, new_gender, selected_pnrno)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        clear_fields()

        PNR_NO_entry.delete(0, tk.END)
        PNAME_entry.delete(0, tk.END)
        PHONE_entry.delete(0, tk.END)
        EMAIL_entry.delete(0, tk.END)
        AGE_entry.delete(0, tk.END)
        gender_var.set("")  # Clear the gender selection
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_passenger():
    selected_pnrno = PNR_NO_entry.get()

    if not selected_pnrno:
        messagebox.showerror("Error", "Please enter a valid ID.")
        return

    if selected_pnrno:
        sql = "DELETE FROM PASSENGER WHERE PNR_NO = %s"
        values = (selected_pnrno,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
        PNR_NO_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a valid ID.")

def show_passenger():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM PASSENGER")
    records = cursor.fetchall()

    for record in records:
        listbox.insert(tk.END, f"PNR_NO: {record[0]}, PNAME: {record[1]}, PHONE: {record[2]}, EMAIL: {record[3]}, AGE: {record[4]}, GENDER: {record[5]}")
def clear_fields():
    PNR_NO_entry.delete(0, tk.END)
    PNAME_entry.delete(0, tk.END)
    PHONE_entry.delete(0, tk.END)
    EMAIL_entry.delete(0, tk.END)
    AGE_entry.delete(0, tk.END)
    gender_var.set("") 
window = tk.Tk()
window.title("PASSENGER DETAILS")
label_style = ttk.Style()
label_style.configure("PASSENGER WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")

PNR_NO_label = tk.Label(window, text="PASSENGER NUMBER:", bg="lightblue")
PNR_NO_entry = tk.Entry(window)

PNAME_label = tk.Label(window, text="PASSENGER NAME:", bg="lightblue")
PNAME_entry = tk.Entry(window)

PHONE_label = tk.Label(window, text="PASSENGER PHONE:", bg="lightblue")
PHONE_entry = tk.Entry(window)

EMAIL_label = tk.Label(window, text="PASSENGER EMAIL:", bg="lightblue")
EMAIL_entry = tk.Entry(window)

AGE_label = tk.Label(window, text="PASSENGER AGE:", bg="lightblue")
AGE_entry = tk.Entry(window)

gender_label = tk.Label(window, text="PASSENGER GENDER:", bg="lightblue")
gender_var = tk.StringVar()

listbox = tk.Listbox(window, width=50)

PNR_NO_label.pack()
PNR_NO_entry.pack()

PNAME_label.pack()
PNAME_entry.pack()

PHONE_label.pack()
PHONE_entry.pack()

EMAIL_label.pack()
EMAIL_entry.pack()

AGE_label.pack()
AGE_entry.pack()

gender_frame = ttk.LabelFrame(frame_passenger_details, text="GENDER")
gender_frame.pack(side="top", padx=5, pady=5, fill="both")
gender_var = tk.StringVar()
gender_var.set("") 
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
male_radio.pack(side="left", padx=5, pady=5)
female_radio.pack(side="left", padx=5, pady=5)
buttons_frame = ttk.LabelFrame(window)
buttons_frame.pack(side="top", padx=10, pady=10, fill="both")
insert_button = tk.Button(buttons_frame, text="Insert Data", command=insert_passenger)
update_button = tk.Button(buttons_frame, text="Update Data", command=update_passenger)
delete_button = tk.Button(buttons_frame, text="Delete Data", command=delete_passenger)
show_button = tk.Button(buttons_frame, text="Show Records", command=show_passenger)

insert_button.pack(side="left", padx=5, pady=5)
update_button.pack(side="left", padx=5, pady=5)
delete_button.pack(side="left", padx=5, pady=5)
show_button.pack(side="left", padx=5, pady=5)

listbox_frame = ttk.LabelFrame(window, text="Passenger Records")
listbox_frame.pack(side="top", padx=10, pady=10, fill="both")
listbox = tk.Listbox(listbox_frame, width=50)
listbox.pack(side="top", padx=5, pady=5, fill="both", expand=True)
clear_fields_button = tk.Button(buttons_frame, text="Clear Fields", command=clear_fields)
clear_fields_button.pack(side="left", padx=5, pady=5)
window.mainloop()
conn.close()