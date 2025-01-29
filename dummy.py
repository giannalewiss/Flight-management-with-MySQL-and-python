import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",  
    user="gianna", 
    password="gianna", 
    database="AIRLINES"  
)
print(conn) 
print("mysql server connected succesfully")
cursor = conn.cursor()



def insert_passenger():
    PNR_NO=PNR_NO_entry.get()
    PNAME =PNAME_entry.get()
    PHONE =PHONE_entry.get()
    EMAIL =EMAIL_entry.get()
    AGE =AGE_entry.get()
    GENDER =gender_var.get()

    insert_query = "INSERT INTO PASSENGER(PNR_NO,PNAME,PHONE,EMAIL,AGE,GENDER)VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (PNR_NO, PNAME,PHONE,EMAIL,AGE,GENDER))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data inserted successfully!")

window = tk.Tk()
window.title("PASSENGER DETAILS")
label_style = ttk.Style()
label_style.configure("PASSENGER WINDOW", font=("Helvetica", 20))
window.configure(bg="lightblue")



def update_passenger():
    selected_pnrno = PNR_NO_entry.get()
    new_name = PNAME_entry.get()
    new_phone = PHONE_entry.get()
    new_email = EMAIL_entry.get()
    new_age = AGE_entry.get()
    new_gender = gender_var.get()

    
    if selected_pnrno and new_name and new_phone and new_email and new_age and new_gender:
        sql = "UPDATE PASSENGER SET PNAME= %s,PHONE= %s,EMAIL= %s,AGE= %s,GENDER=%s WHERE PNR_NO = %s"
        values = (new_name,new_phone,new_email,new_age,new_gender,selected_pnrno)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
        PNR_NO_entry.delete(0, tk.END)
        PNAME_entry.delete(0, tk.END)
        PHONE_entry.delete(0, tk.END)
        EMAIL_entry.delete(0, tk.END)
        AGE_entry.delete(0, tk.END)
        gender_var.set("")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_passenger():
    selected_pnrno = PNR_NO_entry.get()
    
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
        listbox.insert(tk.END, f"PNR_NO: {record[0]}, PNAME: {record[1]}, PHONE: {record[2]}, EMAIL: {record[3]}, AGE: {record[4]},GENDER: {record[4]}")
def gender_selected():
    selected_gender =gender_var.get()
    print("Selected gender:", selected_gender)

pnrno_label = tk.Label(window, text="PASSENGER NUMBER:",bg="lightblue")
PNR_NO_entry = tk.Entry(window)

name_label = tk.Label(window, text="PASSENGER NAME:",bg="lightblue")
PNAME_entry = tk.Entry(window)

phone_label = tk.Label(window, text="PASSENGER PHONENO:",bg="lightblue")
PHONE_entry = tk.Entry(window)

email_label = tk.Label(window, text="PASSENGER EMAIL:",bg="lightblue")
EMAIL_entry = tk.Entry(window)

age_label = tk.Label(window, text="PASSENGER AGE:",bg="lightblue")
AGE_entry = tk.Entry(window)

gender_label = tk.Label(window, text="PASSENGER GENDER:",bg="lightblue")
gender_label.pack()
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", command=gender_selected)
female_radio = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", command=gender_selected)


# Create buttons for CRUD operations
button_style = ttk.Style()
insert_button = tk.Button(window, text="Insert", foreground="black",background="lightyellow", command=insert_passenger)
update_button = tk.Button(window, text="Update",foreground="black",background="orange" ,command=update_passenger)
delete_button = tk.Button(window, text="Delete", foreground="black",background="pink",command=delete_passenger)
show_button = tk.Button(window, text="Show Records",foreground="black",background="lightgreen",command=show_passenger)

# Create a listbox to display records
listbox = tk.Listbox(window, width=50)

# Pack widgets
pnrno_label.pack()
PNR_NO_entry.pack()

name_label.pack()
PNAME_entry.pack()

phone_label.pack()
PHONE_entry.pack()

email_label.pack()
EMAIL_entry.pack()

age_label.pack()
AGE_entry.pack()

gender_label.pack()


male_radio.pack()
female_radio.pack()

insert_button.pack()
update_button.pack()
delete_button.pack()
show_button.pack()

listbox.pack()
window.mainloop()
conn.close()