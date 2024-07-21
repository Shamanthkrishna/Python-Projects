import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import csv

# Function to handle form submission
def submit_form():
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    email = email_var.get()
    mobile = mobile_var.get()
    address = address_text.get("1.0", tk.END).strip()
    gender = gender_var.get()
    dob = dob_var.get()
    nationality = nationality_var.get()
    blood_group = blood_group_var.get()
    job_title = job_title_var.get()
    company = company_var.get()
    industry = industry_var.get()
    education = education_var.get()
    institution = institution_var.get()
    field_of_study = field_of_study_var.get()
    interests = interests_var.get()
    skills = skills_var.get()
    emergency_contact = emergency_contact_var.get()
    
    # Check if all fields are filled
    if all([first_name, last_name, email, mobile, address, gender, dob, nationality, blood_group,
            job_title, company, industry, education, institution, field_of_study, interests, skills, emergency_contact]):
        
        # Save data to CSV
        with open('registration_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, email, mobile, address, gender, dob, nationality,
                             blood_group, job_title, company, industry, education, institution,
                             field_of_study, interests, skills, emergency_contact])
        
        messagebox.showinfo("Success", "Registration Successful")

        # Clear all fields
        first_name_var.set("")
        last_name_var.set("")
        email_var.set("")
        mobile_var.set("")
        address_text.delete("1.0", tk.END)
        gender_var.set("")
        dob_var.set("")
        nationality_var.set("")
        blood_group_var.set("")
        job_title_var.set("")
        company_var.set("")
        industry_var.set("")
        education_var.set("")
        institution_var.set("")
        field_of_study_var.set("")
        interests_var.set("")
        skills_var.set("")
        emergency_contact_var.set("")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to open the date picker
def open_date_picker():
    date_picker_window = tk.Toplevel(app)
    date_picker_window.title("Select Date of Birth")
    date_picker_window.geometry("250x150")
    date_picker_window.grab_set()

    def select_date():
        selected_date = date_entry.get_date()
        dob_var.set(selected_date.strftime('%Y-%m-%d'))
        date_picker_window.destroy()

    date_entry = DateEntry(date_picker_window, date_pattern='y-mm-dd')
    date_entry.pack(pady=10)

    tk.Button(date_picker_window, text="Select Date", command=select_date).pack(pady=10)

# Setting up the main application window
app = tk.Tk()
app.title("Comprehensive Registration Form")
app.geometry("600x800")
app.configure(bg="#f0f0f0")

# Creating a canvas and a scrollbar
canvas = tk.Canvas(app, bg="#f0f0f0")
scrollbar = ttk.Scrollbar(app, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Configure the scrollbar and canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Bind mouse wheel event for scrolling
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

app.bind_all("<MouseWheel>", on_mouse_wheel)

# Variables to store user input
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
mobile_var = tk.StringVar()
address_var = tk.StringVar()
gender_var = tk.StringVar()
dob_var = tk.StringVar()
nationality_var = tk.StringVar()
blood_group_var = tk.StringVar()
job_title_var = tk.StringVar()
company_var = tk.StringVar()
industry_var = tk.StringVar()
education_var = tk.StringVar()
institution_var = tk.StringVar()
field_of_study_var = tk.StringVar()
interests_var = tk.StringVar()
skills_var = tk.StringVar()
emergency_contact_var = tk.StringVar()

# Creating and placing widgets in the scrollable frame

# Main Heading
tk.Label(scrollable_frame, text="Registration Form", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

# Basic Information Section
tk.Label(scrollable_frame, text="Basic Information", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, columnspan=4, pady=10, sticky="w")
tk.Label(scrollable_frame, text="First Name").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=first_name_var).grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(scrollable_frame, text="Last Name").grid(row=2, column=2, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=last_name_var).grid(row=2, column=3, padx=10, pady=5, sticky="ew")

tk.Label(scrollable_frame, text="Email").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=email_var).grid(row=3, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Mobile Number").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=mobile_var).grid(row=4, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

# Line Separator
ttk.Separator(scrollable_frame, orient="horizontal").grid(row=5, column=0, columnspan=4, sticky="ew", pady=10)

# Address Section
tk.Label(scrollable_frame, text="Address", font=("Helvetica", 12), bg="#f0f0f0").grid(row=6, column=0, columnspan=4, pady=10, sticky="w")
address_text = tk.Text(scrollable_frame, height=4, width=50)
address_text.grid(row=7, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

# Line Separator
ttk.Separator(scrollable_frame, orient="horizontal").grid(row=8, column=0, columnspan=4, sticky="ew", pady=10)

# Personal Information Section
tk.Label(scrollable_frame, text="Personal Information", font=("Helvetica", 12), bg="#f0f0f0").grid(row=9, column=0, columnspan=4, pady=10, sticky="w")
tk.Label(scrollable_frame, text="Gender").grid(row=10, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(scrollable_frame, text="Male", variable=gender_var, value="Male", bg="#f0f0f0").grid(row=10, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(scrollable_frame, text="Female", variable=gender_var, value="Female", bg="#f0f0f0").grid(row=10, column=2, padx=10, pady=5, sticky="w")

tk.Label(scrollable_frame, text="Date of Birth").grid(row=11, column=0, padx=10, pady=5, sticky="w")
dob_entry = tk.Entry(scrollable_frame, textvariable=dob_var)
dob_entry.grid(row=11, column=1, padx=10, pady=5, columnspan=2, sticky="ew")
tk.Button(scrollable_frame, text="Select Date", command=open_date_picker).grid(row=11, column=3, padx=10, pady=5)

tk.Label(scrollable_frame, text="Nationality").grid(row=12, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=nationality_var).grid(row=12, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Blood Group").grid(row=13, column=0, padx=10, pady=5, sticky="w")
blood_group_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
blood_group_menu = ttk.Combobox(scrollable_frame, textvariable=blood_group_var, values=blood_group_options, state="readonly")
blood_group_menu.grid(row=13, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

# Line Separator
ttk.Separator(scrollable_frame, orient="horizontal").grid(row=14, column=0, columnspan=4, sticky="ew", pady=10)

# Professional Information Section
tk.Label(scrollable_frame, text="Professional Information", font=("Helvetica", 12), bg="#f0f0f0").grid(row=15, column=0, columnspan=4, pady=10, sticky="w")
tk.Label(scrollable_frame, text="Job Title").grid(row=16, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=job_title_var).grid(row=16, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Company").grid(row=17, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=company_var).grid(row=17, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Industry").grid(row=18, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=industry_var).grid(row=18, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

# Line Separator
ttk.Separator(scrollable_frame, orient="horizontal").grid(row=19, column=0, columnspan=4, sticky="ew", pady=10)

# Educational Information Section
tk.Label(scrollable_frame, text="Educational Information", font=("Helvetica", 12), bg="#f0f0f0").grid(row=20, column=0, columnspan=4, pady=10, sticky="w")
tk.Label(scrollable_frame, text="Highest Level of Education").grid(row=21, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=education_var).grid(row=21, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Institution Attended").grid(row=22, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=institution_var).grid(row=22, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Field of Study").grid(row=23, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=field_of_study_var).grid(row=23, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

# Line Separator
ttk.Separator(scrollable_frame, orient="horizontal").grid(row=24, column=0, columnspan=4, sticky="ew", pady=10)

# Additional Information Section
tk.Label(scrollable_frame, text="Additional Information", font=("Helvetica", 12), bg="#f0f0f0").grid(row=25, column=0, columnspan=4, pady=10, sticky="w")
tk.Label(scrollable_frame, text="Interests").grid(row=26, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=interests_var).grid(row=26, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Skills").grid(row=27, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=skills_var).grid(row=27, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

tk.Label(scrollable_frame, text="Emergency Contact").grid(row=28, column=0, padx=10, pady=5, sticky="w")
tk.Entry(scrollable_frame, textvariable=emergency_contact_var).grid(row=28, column=1, padx=10, pady=5, columnspan=3, sticky="ew")

# Register Button
tk.Button(scrollable_frame, text="Register", command=submit_form).grid(row=29, column=0, columnspan=4, pady=20)

# Adjust the weight of rows and columns to ensure proper alignment
for i in range(30):  # Adjust based on the number of rows
    scrollable_frame.grid_rowconfigure(i, weight=1)
for j in range(4):  # Adjust based on the number of columns
    scrollable_frame.grid_columnconfigure(j, weight=1)

# Running the application
app.mainloop()
