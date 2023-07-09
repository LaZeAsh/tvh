import tkinter as tk
from tkinter import ttk
import call
global activity
global activity_time
global activity_location
global activity_type
global person_name
global phone_number

def submit_data():
    person_name = name_entry.get()
    phone_number = phone_entry.get()
    is_appointment = appointment_var.get()
    is_reservation = reservation_var.get()
    activity = activity_entry.get()
    activity_time = activity_time_entry.get()
    activity_location = activity_location_entry.get()

    if is_appointment > is_reservation:
        activity_type = "appointment"
    elif is_appointment < is_reservation:
        activity_type = "reservation"
    else:
        # Default to appointments
        activity_type = "appointment"

    print("Name:", person_name)
    print("Phone Number:", phone_number)
    print("Is Appointment:", is_appointment)
    print("Is Reservation:", is_reservation)
    print("Activity:", activity)
    print("Activity Time:", activity_time)
    print("Activity Location:", activity_location)

    # Clear the fields after submission
    clear_fields()
    
    Hm = call.Phone()
    Hm.dial(person_name, activity_type, activity_location, activity_time, activity)

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    appointment_var.set(0)
    reservation_var.set(0)
    activity_entry.delete(0, tk.END)
    activity_time_entry.delete(0, tk.END)
    activity_location_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Form")

# Create a frame
frame = ttk.Frame(root)
frame.pack(pady=20, padx=20)

# Entry field for "Name"
name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10)

# Entry field for "Phone Number"
phone_label = ttk.Label(frame, text="Phone Number:")
phone_label.grid(row=1, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=1, column=1, padx=10)

# Checkbox for "Appointment"
appointment_var = tk.IntVar()
appointment_checkbox = ttk.Checkbutton(frame, text="Appointment", variable=appointment_var)
appointment_checkbox.grid(row=2, columnspan=2, sticky=tk.W, padx=10, pady=(10, 0))

# Checkbox for "Reservation"
reservation_var = tk.IntVar()
reservation_checkbox = ttk.Checkbutton(frame, text="Reservation", variable=reservation_var)
reservation_checkbox.grid(row=3, columnspan=2, sticky=tk.W, padx=10, pady=(0, 10))

# Entry field for "Activity"
activity_label = ttk.Label(frame, text="Activity:")
activity_label.grid(row=4, column=0, sticky=tk.W)
activity_entry = ttk.Entry(frame)
activity_entry.grid(row=4, column=1, padx=10)

# Entry field for "Activity Time"
activity_time_label = ttk.Label(frame, text="Activity Time:")
activity_time_label.grid(row=5, column=0, sticky=tk.W)
activity_time_entry = ttk.Entry(frame)
activity_time_entry.grid(row=5, column=1, padx=10)

# Entry field for "Activity Location"
activity_location_label = ttk.Label(frame, text="Activity Location:")
activity_location_label.grid(row=6, column=0, sticky=tk.W)
activity_location_entry = ttk.Entry(frame)
activity_location_entry.grid(row=6, column=1, padx=10)

submit_button = ttk.Button(frame, text="Submit", command=submit_data)
submit_button.grid(row=7, columnspan=2, pady=(20, 0))

# Create a table
table_frame = ttk.Frame(root)
table_frame.pack(pady=(0, 20), padx=20)

# Define the table headers
header1 = ttk.Label(table_frame, text="Business Name", anchor=tk.W, width=20)
header1.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
header2 = ttk.Label(table_frame, text="Phone Number", anchor=tk.CENTER, width=20)
header2.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

# Define table rows
business_names = [f"Business {row + 1}" for row in range(5)]
phone_numbers = [f"123-456-{row + 1:02d}" for row in range(5)]

for row, (business_name, phone_number) in enumerate(zip(business_names, phone_numbers), start=1):
    label1 = ttk.Label(table_frame, text=business_name, anchor=tk.W)
    label1.grid(row=row, column=0, sticky=tk.NSEW, padx=5, pady=5)
    button = ttk.Button(table_frame, text=phone_number, width=15, command=lambda number=phone_number: do_something(number))
    button.grid(row=row, column=1, sticky=tk.NSEW, padx=5, pady=5)

# Set weights to make the table expand horizontally
table_frame.columnconfigure(0, weight=1)
table_frame.columnconfigure(1, weight=1)

# Function for the phone number button action
def do_something(phone_number):
    print(f"Phone number clicked: {phone_number}")

root.mainloop()
