import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Profile Builder")
window.resizable(True,True)
window.configure(bg="Neon",cursor="cross")
window.geometry("400x400")

def create_id():
    fname = entry_fname.get()
    mname = entry_mname.get()
    lname = entry_lname.get()
    birth_year = entry_birth.get()
    gender = gender_var.get()

   
    current_year = datetime.now().year
    age = current_year - int(birth_year)

    full_name = fname + " " + mname + " " + lname

   
    id_window = tk.Toplevel(window)
    id_window.title("Student ID")
    id_window.geometry("300x250")
    id_window.configure(bg="pink")

    title = tk.Label(id_window, text="Student ID", font=("Arial", 16, "bold"), bg="pink")
    title.pack(pady=10)

    name_label = tk.Label(id_window, text="Name: " + full_name, bg="pink")
    name_label.pack()

    age_label = tk.Label(id_window, text="Age: " + str(age) + " years old", bg="pink")
    age_label.pack()

    gender_label = tk.Label(id_window, text="Gender: " + gender, bg="pink")
    gender_label.pack()


window = tk.Tk()
window.title("Profile Builder")
window.geometry("400x250")
window.configure(bg="lightgreen")


entry_fname = tk.Entry(window)
entry_fname.grid(row=0, column=0, padx=10, pady=5)
tk.Label(window, text="First Name", bg="lightgreen").grid(row=1, column=0)

entry_mname = tk.Entry(window)
entry_mname.grid(row=0, column=1)
tk.Label(window, text="Middle Name", bg="lightgreen").grid(row=1, column=1)

entry_lname = tk.Entry(window)
entry_lname.grid(row=0, column=2)
tk.Label(window, text="Last Name", bg="lightgreen").grid(row=1, column=2)

entry_birth = tk.Entry(window)
entry_birth.grid(row=2, column=0, pady=10)
tk.Label(window, text="Birth Year", bg="lightgreen").grid(row=3, column=0)


gender_var = tk.StringVar()
gender_var.set("Male")

tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", bg="lightgreen").grid(row=2, column=1)
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", bg="lightgreen").grid(row=2, column=2)


submit_btn = tk.Button(window, text="Submit", command=create_id)
submit_btn.grid(row=4, column=1, pady=20)

window.mainloop()
