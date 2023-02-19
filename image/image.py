from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# create UI
root = Tk()
root.title("File Selector")

root.geometry("600x900")


# input files control
input_files = []
input_files_listbox = Listbox(root, selectmode=MULTIPLE)
input_files_listbox.pack(fill=BOTH, expand=1)

# set the filetypes to .jpg, .png and .tiff
filetypes = [("JPEG", "*.jpg"), ("PNG", "*.png"), ("TIFF", "*.tiff")]

def add_files():
    # show file dialog
    files = filedialog.askopenfilenames(filetypes=filetypes, title="Select files to convert")

    # add files to listbox
    for file in files:
        input_files.append(file)
        input_files_listbox.insert(END, file)

# add files button
add_files_button = Button(root, text="Add Files", command=add_files)
add_files_button.pack(pady=10)

# convert to png button
def convert_to_png():
    # show file dialog
    selected_files = input_files_listbox.curselection()
    if not selected_files:
        messagebox.showerror("Error", "Please select files to convert")
        return
    
    initial_file = input_files[selected_files[0]]
    initial_file_name = os.path.splitext(os.path.basename(initial_file))[0]
    initial_directory = os.path.dirname(initial_file)

    # get output directory and filename
    outfile = filedialog.asksaveasfilename(defaultextension='.png', initialdir=initial_directory, initialfile=initial_file_name)

    # convert files
    for file in selected_files:
        input_file = input_files[file]
        with Image.open(input_file) as im:
            # get the filename for the output file
            output_filename = os.path.join(os.path.dirname(outfile), os.path.splitext(os.path.basename(input_file))[0] + ".png")
            im.save(output_filename, format='png')
    
    # show completion message
    messagebox.showinfo("Conversion Complete", "Files have been converted to PNG format.")


convert_to_png_button = Button(root, text="Convert to PNG", command=convert_to_png)
convert_to_png_button.pack(pady=10)


# convert to jpg button
def convert_to_jpg():
    # show file dialog
    selected_files = input_files_listbox.curselection()
    if not selected_files:
        messagebox.showerror("Error", "Please select files to convert")
        return
    initial_file = input_files[selected_files[0]]
    initial_file_name = os.path.splitext(os.path.basename(initial_file))[0]
    outfile = filedialog.asksaveasfilename(defaultextension='.jpg', initialfile=initial_file_name)

    # convert files
    for file in selected_files:
        with Image.open(input_files[file]) as im:
            im.save(outfile, format='jpg')

convert_to_jpg_button = Button(root, text="Convert to JPG", command=convert_to_jpg)
convert_to_jpg_button.pack(pady=10)

root.mainloop()
