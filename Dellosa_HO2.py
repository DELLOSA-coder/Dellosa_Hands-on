import tkinter as tk

window = tk.Tk()

window.title("Jeph's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="pink",cursor="hand2")


label = tk.Label(window,text="STUDENT PROFILE",font=("Poppins",35),fg="green",bg="violet")
label.pack()

label = tk.Label(window,text="Name: Dellosa , Jose Philip A. ",font=("Poppins",10),fg="Black")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Age: 20 yrs old",font=("Poppins",10),fg="black")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Course % Section: BSIT - 1B ",font=("Poppins",10),fg="black")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Birthday: May 24 2005 ",font=("Poppins",10),fg="navy blue")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Personal Motto: Bossing! ",font=("Poppins",10),fg="maroon")
label.pack(anchor="w", pady=10)

window.mainloop()