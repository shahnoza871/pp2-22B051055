import tkinter as tk
from tkinter import messagebox

from main import *

def create_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.configure(bg="black")
    return new_window

def create_button_function(title, entry_widget=None):
    def button_function():
        new_window = create_new_window(title)

        if title == "Recurrence Relations":
            entry_label = tk.Label(new_window, text="Write the number of entries in your SINGE ROOTED relation", fg="white", bg="black")
            entry_label.pack(pady=5)

            entry_var = tk.StringVar()
            entry_widget = tk.Entry(new_window, textvariable=entry_var, bg="black", fg="white", insertbackground="white")
            entry_widget.pack(pady=5)

            entry_frame = tk.Frame(new_window, bg="black")
            entry_frame.pack(pady=5)

            def create_coefficient_index_pairs():
                try:
                    num_entries = int(entry_var.get())
                    clear_entries(entry_frame)

                    coefficients_label = tk.Label(entry_frame, text="Coefficients", fg="white", bg="black")
                    coefficients_label.grid(row=0, column=0, padx=5)

                    indexes_label = tk.Label(entry_frame, text="Indexes", fg="white", bg="black")
                    indexes_label.grid(row=0, column=1, padx=5)

                    for i in range(num_entries):
                        coefficient_entry = tk.Entry(entry_frame, bg="black", fg="white", insertbackground="white", width=5)
                        coefficient_entry.grid(row=i + 1, column=0, padx=5, pady=2)

                        index_entry = tk.Entry(entry_frame, bg="black", fg="white", insertbackground="white", width=5)
                        index_entry.grid(row=i + 1, column=1, padx=5, pady=2)

                except ValueError:
                    messagebox.showwarning("Invalid Input", "Please enter a valid number.")

            def clear_entries(frame):
                for widget in frame.winfo_children():
                    widget.destroy()

            def get_initial_value_entries(new_window, num_entries):
                entry_label = tk.Label(new_window, text="Enter initial values for exact solution", fg="white", bg="black")
                entry_label.pack(pady=5)

                initial_value_entries = []

                for i in range(num_entries):
                    initial_value_entry = tk.Entry(new_window, bg="black", fg="white", insertbackground="white", width=5)
                    initial_value_entry.pack(pady=2)
                    initial_value_entries.append(initial_value_entry)

                return initial_value_entries
            
            def display_general_solution():
                rr = get_coefficient_index_pairs(entry_frame)
                result = homogeneous_RR(rr)
                general_solution_label.config(text=f"General Solution: {result}")

            def display_exact_solution():
                rr = get_coefficient_index_pairs(entry_frame)
                num_entries = int(entry_var.get())
                initial_value_entries = get_initial_value_entries(new_window, num_entries)
                result = exact_solution(rr, initial_value_entries)
                exact_solution_label.config(text=f"Exact Solution: {result}")


            def get_coefficient_index_pairs(frame):
                coefficients = []
                indexes = []
                for widget in frame.winfo_children():
                    if isinstance(widget, tk.Entry):
                        value = widget.get()
                        if widget.grid_info()["column"] == 0:
                            coefficients.append(float(value))
                        else:
                            indexes.append(int(value))
                return list(zip(coefficients, indexes)) 
        

            ok_button = tk.Button(new_window, text="OK", command=create_coefficient_index_pairs, bg="black", fg="white")
            ok_button.pack(pady=5)

            result_label = tk.Label(new_window, text="", fg="white", bg="black")
            result_label.pack(pady=10)

            # Create labels for displaying results
            general_solution_label = tk.Label(new_window, text="", fg="white", bg="black")
            general_solution_label.pack(pady=10)

            exact_solution_label = tk.Label(new_window, text="", fg="white", bg="black")
            exact_solution_label.pack(pady=10)

            # General Solution button
            general_solution_button = tk.Button(new_window, text="Display General Solution", command=display_general_solution, bg="black", fg="white")
            general_solution_button.pack(side=tk.RIGHT, pady=5, padx=5)

            # Exact Solution button
            exact_solution_button = tk.Button(new_window, text="Display Exact Solution", command=display_exact_solution, bg="black", fg="white")
            exact_solution_button.pack(side=tk.RIGHT, pady=5, padx=5)

        elif title in ["General Solution", "Exact Solution"]:
            # If "General Solution" or "Exact Solution" is pressed, clear everything

            if title == "Exact Solution":
                new_window = create_new_window("Enter Initial Values")
                try:
                    num_entries = int(entry_widget.get())
                except ValueError:
                    num_entries = 0
                    messagebox.showwarning("Invalid Input", "Please enter a valid number.")

                initial_values_label = tk.Label(new_window, text="Enter the initial values", fg="white", bg="black")
                initial_values_label.pack()

                initial_values_frame = tk.Frame(new_window, bg="black")
                initial_values_frame.pack()

                initial_value_entries = []

                for i in range(num_entries):
                    initial_value_entry = tk.Entry(initial_values_frame, bg="black", fg="white", insertbackground="white", width=5)
                    initial_value_entry.grid(row=0, column=i, padx=2, pady=2)
                    initial_value_entries.append(initial_value_entry)

                def submit_initial_values():
                    try:
                        values = [float(entry.get()) for entry in initial_value_entries]
                        # Here you can use the values for further calculations or processing
                        print(values)  # Example: print the values or pass them to a function
                    except ValueError:
                        messagebox.showwarning("Invalid Input", "Please enter valid numeric values.")

                submit_button = tk.Button(new_window, text="Submit", command=submit_initial_values, bg="black", fg="white")
                submit_button.pack(pady=5)

            
        elif title == "Operation on Binary Numbers":
            binary_operation_window()

        elif title == "Operation on Octal Numbers":
            octal_operation_window()

        else:
            tk.Label(new_window, text=f"This is the {title} window", fg="white", bg="black").pack(padx=10, pady=10)

    return button_function

def create_exact_solution_entries():
    create_button_function("Exact Solution")()

def binary_operation_window():
    new_window = create_new_window("Operation on Binary Numbers")

    binary_value_label = tk.Label(new_window, text="Enter a binary number:", fg="white", bg="black")
    binary_value_label.pack(pady=5)

    binary_value_entry = tk.Entry(new_window, bg="black", fg="white", insertbackground="white")
    binary_value_entry.pack(pady=5)

    binary = Binary('0')  # Default value, change as needed

    def update_binary_label():
        nonlocal binary
        binary = Binary(binary_value_entry.get())
        binary_result_label.config(text=f"Binary: {binary.num}")

    def convert_to_decimal():
        decimal_result_label.config(text=f"Decimal: {binary.to_decimal()}")

    def convert_to_octal():
        octal_result_label.config(text=f"Octal: {binary.to_octal()}")

    def perform_binary_sum():
        other_binary = Binary(other_binary_entry.get())
        sum_result = binary.sum(other_binary)
        binary_result_label.config(text=f"Binary: {sum_result.num}")

    def perform_binary_product():
        other_binary = Binary(other_binary_entry.get())
        product_result = binary.product(other_binary)
        binary_result_label.config(text=f"Binary: {product_result.num}")

    binary_result_label = tk.Label(new_window, text="Binary: 0", fg="white", bg="black")
    binary_result_label.pack(pady=5)

    decimal_result_label = tk.Label(new_window, text="Decimal: 0", fg="white", bg="black")
    decimal_result_label.pack(pady=5)

    octal_result_label = tk.Label(new_window, text="Octal: 0", fg="white", bg="black")
    octal_result_label.pack(pady=5)

    convert_button = tk.Button(new_window, text="Convert", command=update_binary_label, bg="black", fg="white")
    convert_button.pack(pady=5)

    decimal_button = tk.Button(new_window, text="To Decimal", command=convert_to_decimal, bg="black", fg="white")
    decimal_button.pack(pady=5)

    octal_button = tk.Button(new_window, text="To Octal", command=convert_to_octal, bg="black", fg="white")
    octal_button.pack(pady=5)

    other_binary_entry_label = tk.Label(new_window, text="Enter another binary number:", fg="white", bg="black")
    other_binary_entry_label.pack(pady=5)

    other_binary_entry = tk.Entry(new_window, bg="black", fg="white", insertbackground="white")
    other_binary_entry.pack(pady=5)

    sum_button = tk.Button(new_window, text="Sum", command=perform_binary_sum, bg="black", fg="white")
    sum_button.pack(pady=5)

    product_button = tk.Button(new_window, text="Product", command=perform_binary_product, bg="black", fg="white")
    product_button.pack(pady=5)

def octal_operation_window():
    new_window = create_new_window("Operation on Octal Numbers")

    octal_value_label = tk.Label(new_window, text="Enter an octal number:", fg="white", bg="black")
    octal_value_label.pack(pady=5)

    octal_value_entry = tk.Entry(new_window, bg="black", fg="white", insertbackground="white")
    octal_value_entry.pack(pady=5)

    octal = Octal('0')  # Default value, change as needed

    def update_octal_label():
        nonlocal octal
        octal = Octal(octal_value_entry.get())
        octal_result_label.config(text=f"Octal: {octal.num}")

    def convert_to_decimal():
        decimal_result_label.config(text=f"Decimal: {octal.to_decimal()}")

    def convert_to_binary():
        binary_result_label.config(text=f"Binary: {octal.to_binary()}")

    def perform_octal_sum():
        other_octal = Octal(other_octal_entry.get())
        sum_result = octal.sum(other_octal)
        octal_result_label.config(text=f"Octal: {sum_result.num}")

    def perform_octal_product():
        other_octal = Octal(other_octal_entry.get())
        product_result = octal.product(other_octal)
        octal_result_label.config(text=f"Octal: {product_result.num}")

    octal_result_label = tk.Label(new_window, text="Octal: 0", fg="white", bg="black")
    octal_result_label.pack(pady=5)

    decimal_result_label = tk.Label(new_window, text="Decimal: 0", fg="white", bg="black")
    decimal_result_label.pack(pady=5)

    binary_result_label = tk.Label(new_window, text="Binary: 0", fg="white", bg="black")
    binary_result_label.pack(pady=5)

    convert_button = tk.Button(new_window, text="Convert", command=update_octal_label, bg="black", fg="white")
    convert_button.pack(pady=5)

    decimal_button = tk.Button(new_window, text="To Decimal", command=convert_to_decimal, bg="black", fg="white")
    decimal_button.pack(pady=5)

    binary_button = tk.Button(new_window, text="To Binary", command=convert_to_binary, bg="black", fg="white")
    binary_button.pack(pady=5)

    other_octal_entry_label = tk.Label(new_window, text="Enter another octal number:", fg="white", bg="black")
    other_octal_entry_label.pack(pady=5)

    other_octal_entry = tk.Entry(new_window, bg="black", fg="white", insertbackground="white")
    other_octal_entry.pack(pady=5)

    sum_button = tk.Button(new_window, text="Sum", command=perform_octal_sum, bg="black", fg="white")
    sum_button.pack(pady=5)

    product_button = tk.Button(new_window, text="Product", command=perform_octal_product, bg="black", fg="white")
    product_button.pack(pady=5)

# Create the main Tkinter window
root = tk.Tk()
root.title("Math and Logic Operations")
root.configure(bg="black")

# List of button titles
button_titles = [
    "Recurrence Relations",
    "Operation on Binary Numbers",
    "Operation on Octal Numbers",
    "Sets",
    "Graphs",
    "Logic",
    "Combinatorics",
    "Diana - button2",
    "Diana - button3",
    "Recursion",
    "Binary Search",
    "Factorials"
]

# Number of columns in the grid
num_columns = 2

# Create buttons for different functionalities and arrange in a grid
for i, title in enumerate(button_titles):
    button = tk.Button(root, text=title, command=create_button_function(title), width=20, height=2, bg="black", fg="white")
    button.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
