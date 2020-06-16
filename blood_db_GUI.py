import tkinter as tk      # Standard bindings to Tk (tk-inter(face))
from tkinter import ttk   # Binding to newer "themed widgets"


def design_window():

    def cancel_cmd():
        # Function called when cancel button is pressed
        root.destroy()  # Closes the window stored in the "root" variable

    def ok_button_work():
        # Function called with ok button is pressed
        print("Database entry:")
        name = name_entry.get()
        print("Name is {}".format(name))
        print("Blood Type is {}{}".format(blood_letter.get(),
                                          rh_value.get()))
        print("Nearest center is {}".format(center_location.get()))

    def brun():
        # Function called when checkbox is clicked
        print("Checked the box")

    root = tk.Tk()
    root.title("Blood Database Interface")

    top_description = ttk.Label(root, text="Blood Donor Database")
    top_description.grid(column=0, row=0, columnspan=2, sticky="W")

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)

    name_entry = tk.StringVar()
    name_entry.set("Enter your name")
    name_entry_box = ttk.Entry(root, width=30, textvariable=name_entry)
    name_entry_box.grid(column=1, row=1)

    blood_letter = tk.StringVar()
    button_A = ttk.Radiobutton(root, text="A", variable=blood_letter,
                               value="A")
    button_A.grid(column=0, row=2, sticky="W")
    button_B = ttk.Radiobutton(root, text="B", variable=blood_letter,
                               value="B")
    button_B.grid(column=0, row=3, sticky="W")
    button_AB = ttk.Radiobutton(root, text="AB", variable=blood_letter,
                               value="AB")
    button_AB.grid(column=0, row=4, sticky="W")
    button_O = ttk.Radiobutton(root, text="O", variable=blood_letter,
                               value="O")
    button_O.grid(column=0, row=5, sticky="W")

    rh_value = tk.StringVar()
    rh_value.set("+")
    rh_check = ttk.Checkbutton(root, text="Rh Factor", variable=rh_value,
                               onvalue="+", offvalue="-", command=brun)
    rh_check.grid(column=1, row=3)

    ok_button = ttk.Button(root, text="Ok", command=ok_button_work)
    ok_button.grid(column=1, row=5)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_cmd)
    cancel_button.grid(column=2, row=5)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)
    center_location = tk.StringVar()
    center_location.set("None selected")
    center_box = ttk.Combobox(root, textvariable=center_location)
    center_box['values'] = ("None selected", "Durham", "Raleigh", "Cary", "Apex")
    center_box.state(['readonly'])
    center_box.grid(column=2, row=1)

    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    design_window()