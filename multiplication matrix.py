import tkinter as tk
from tkinter import ttk
import numpy as np

def multiply_matrices():
    # Get the values entered by the user
    rows_a = int(rows_a_entry.get())
    cols_a = int(cols_a_entry.get())
    rows_b = int(rows_b_entry.get())
    cols_b = int(cols_b_entry.get())

    # Check if matrix multiplication is possible
    if cols_a != rows_b:
        result_label.config(text="Matrix dimensions are not compatible for multiplication.")
        return

    # Create matrices A and B from user input
    matrix_a = []
    matrix_b = []
    for i in range(rows_a):
        row = []
        for j in range(cols_a):
            entry = a_entries[i][j].get()
            row.append(float(entry))
        matrix_a.append(row)

    for i in range(rows_b):
        row = []
        for j in range(cols_b):
            entry = b_entries[i][j].get()
            row.append(float(entry))
        matrix_b.append(row)

    # Perform matrix multiplication
    result_matrix = np.dot(np.array(matrix_a), np.array(matrix_b))

    # Display the result in the GUI
    result_label.config(text="Result Matrix:")
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, str(result_matrix))
    result_text.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Matrix Multiplication")

# Create labels and entry fields for matrix dimensions
rows_a_label = ttk.Label(window, text="Matrix A Rows:")
rows_a_label.grid(row=0, column=0)
rows_a_entry = ttk.Entry(window)
rows_a_entry.grid(row=0, column=1)

cols_a_label = ttk.Label(window, text="Matrix A Columns:")
cols_a_label.grid(row=1, column=0)
cols_a_entry = ttk.Entry(window)
cols_a_entry.grid(row=1, column=1)

rows_b_label = ttk.Label(window, text="Matrix B Rows:")
rows_b_label.grid(row=0, column=6)
rows_b_entry = ttk.Entry(window)
rows_b_entry.grid(row=0, column=7)

cols_b_label = ttk.Label(window, text="Matrix B Columns:")
cols_b_label.grid(row=1, column=6)
cols_b_entry = ttk.Entry(window)
cols_b_entry.grid(row=1, column=7)

rows_a_label = ttk.Label(window, text="")
rows_a_label.grid(row=6, column=0)

# Create labels and entry fields for matrix A
a_label = ttk.Label(window, text="Matrix A:")
a_label.grid(row=7, column=0)
a_entries = []
for i in range(4):
    row_entries = []
    for j in range(4):
        entry = ttk.Entry(window)
        entry.grid(row=7 + i, column=1 + j)
        row_entries.append(entry)
    a_entries.append(row_entries)

# Create labels and entry fields for matrix B
b_label = ttk.Label(window, text="Matrix B:")
b_label.grid(row=7, column=6)
b_entries = []
for i in range(4):
    row_entries = []
    for j in range(4):
        entry = ttk.Entry(window)
        entry.grid(row=7 + i, column=7 + j)
        row_entries.append(entry)
    b_entries.append(row_entries)

# Create a button to calculate the result
multiply_button = ttk.Button(window, text="Multiply", command=multiply_matrices)
multiply_button.grid(row=20, column=6)

# Create labels and text widget to display the result
result_label = ttk.Label(window, text="")
result_label.grid(row=22, column=0)
result_text = tk.Text(window, height=4, width=40, state=tk.DISABLED)
result_text.grid(row=22, column=2, columnspan=8)

window.mainloop()
