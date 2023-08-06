import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter import font as tkfont

# Create the main window
root = tk.Tk()
root.title("Move files")
root.geometry("600x400")
root.configure(bg="#FFFFFF") 
font_hel = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Function to create a button and bind it to a script
def create_button(script_name):
    return tk.Button(root, text=script_name[:-3], command=lambda: run_script(script_name))

# Function to run the selected Python script
def run_selected_script():
    selected_value = listbox_var.get()
    if selected_value == "":
        messagebox.showwarning("Error", "Please select a file extension.")
        return

    # Convert the selected value to an integer index
    selected_index = termination.index(selected_value)
    extension = termination[selected_index]

    # Get the source_folder and destination_folder paths from the entry widgets
    path1 = entry1.get()
    path2 = entry2.get()

    # Check if the paths are valid directories
    if not os.path.isdir(path1) or not os.path.isdir(path2):
        messagebox.showwarning("Error", "Please enter valid directory paths for both Source Folder and Destination Folder.")
        return

    try:
        os.system(f"python automation.py --source_folder {path1} --destination_folder {path2} --extension {extension}")
        messagebox.showinfo("Success", "Files transferred successfully!")
    except Exception as e:
        # Display a warning pop-up with the error message
        messagebox.showwarning("Error", f"An error occurred: {e}")

# Function to open a file dialog and update the corresponding entry widget
def open_file_dialog(entry_widget):
    path = filedialog.askdirectory()
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)

# List of file extensions
termination = ["png", "jpeg", "pdf","zip","pptx","ppt","xlsx","csv","xls"] 

# Create a dropdown menu to display the available options
tk.Label(root, text="Extension:",font=font_hel,bg="#FFFFFF",highlightcolor='#CCFF00').pack()

listbox_var = tk.StringVar(root)
listbox_var.set("")  # Set a default empty value
listbox = tk.OptionMenu(root, listbox_var, *termination)
listbox.pack(pady=10)

# Labels for paths
tk.Label(root, text="Source Folder:",font=font_hel,bg="#FFFFFF",highlightcolor='#CCFF00').pack()

# Create an entry widget for the source folder
entry1 = tk.Entry(root)
entry1.pack(pady=15)

# Create a button to open file dialog for the source folder
source_folder_button = tk.Button(root, text="Browse", command=lambda: open_file_dialog(entry1))
source_folder_button.pack()

# Create an entry widget for the destination folder
tk.Label(root, text="Destination Folder:",font=font_hel,bg="#FFFFFF",highlightcolor='#CCFF00').pack()
entry2 = tk.Entry(root)
entry2.pack(pady=15)

# Create a button to open file dialog for the destination folder
destination_folder_button = tk.Button(root, text="Browse", command=lambda: open_file_dialog(entry2))
destination_folder_button.pack()

# Create a button to run the selected option
run_script_button = tk.Button(root, text="Transfer Files", command=run_selected_script)
run_script_button.pack(pady=10)

# Modify the listbox font
listbox.config(font=font_hel,highlightbackground='#FFFFFF',highlightcolor='#CCFF00')

# Modify the buttons font
source_folder_button.config(font=font_hel, highlightbackground="#FFFFFF",highlightcolor='#CCFF00')
destination_folder_button.config(font=font_hel, highlightbackground='#FFFFFF',highlightcolor='#CCFF00')
run_script_button.config(font=font_hel,highlightbackground='#FFFFFF',highlightcolor='#CCFF00')

# Run the main loop 
root.mainloop()