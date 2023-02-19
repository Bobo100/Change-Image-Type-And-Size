from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os


class App:
    def __init__(self, master):
        self.master = master
        master.title("圖片上傳")

        self.input_files_listbox = Listbox(root, selectmode=MULTIPLE)
        self.input_files_listbox.pack(fill=BOTH, expand=1)

        # self.images = []
        self.input_files = []

        # 新增圖片按鈕
        self.add_files_button = Button(
            root, text="Add Files", command=self.add_files)
        self.add_files_button.pack(pady=10)

        # 圖片轉換按鈕
        self.convert_to_png_button = Button(
            master, text="Convert to PNG", command=self.convert_to_png)
        self.convert_to_png_button.pack(pady=10)

    def add_files(self):
        # set the filetypes to .jpg, .png and .tiff
        filetypes = [("JPEG", "*.jpg"), ("PNG", "*.png"), ("TIFF", "*.tiff")]
        # show file dialog
        files = filedialog.askopenfilenames(
            filetypes=filetypes, title="Select files to convert")

        # add files to listbox
        for file in files:
            # check if the file is already in input_files list            
            if file not in self.input_files_listbox.get(0, END):
                # 建立一個新的frame (用來放圖片和檔名) 並放在listbox裡
                file_frame = Frame(self.input_files_listbox)
                file_frame.pack(fill=BOTH)

                # 開啟圖片
                img = Image.open(file)
                img = img.resize((120, 120), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

                # 建立一個label 用來顯示圖片
                label = Label(file_frame, image=img)
                label.image = img
                label.pack(side=LEFT)

                # 建立一個label 用來顯示檔名 (路徑)
                filename_label = Label(file_frame, text=os.path.basename(file))
                filename_label.pack(side=LEFT, padx=10)
            
                remove_button = Button(
                    file_frame, text="Remove", command=lambda file=file: self.remove_file(file))
                remove_button.pack(side=RIGHT, padx=5)
                
                # 把檔案路徑加入到input_files
                # self.input_files.append(file)
                self.input_files.append((file_frame, file))
                self.input_files_listbox.insert(END, file)
                
    def remove_file(self, file):
        for i, (frame, filepath) in enumerate(self.input_files):
            if filepath == file:
                frame.destroy()
                self.input_files_listbox.delete(i)
                del self.input_files[i]
                break

    def convert_to_png(self):
        # show file dialog
        selected_files = self.input_files_listbox.curselection()
        if not selected_files:
            messagebox.showerror("Error", "Please select files to convert")
            return

        initial_file = self.input_files[selected_files[0]]
        print(initial_file)
        initial_file_name = os.path.splitext(os.path.basename(initial_file))[0]
        initial_directory = os.path.dirname(initial_file)

        # get output directory and filename
        outfile = filedialog.asksaveasfilename(
            defaultextension='.png', initialdir=initial_directory, initialfile=initial_file_name)

        # convert files
        for file in selected_files:
            input_file = self.input_files[file]
            with Image.open(input_file) as im:
                # get the filename for the output file
                output_filename = os.path.join(os.path.dirname(
                    outfile), os.path.splitext(os.path.basename(input_file))[0] + ".png")
                im.save(output_filename, format='png')

        # show completion message
        messagebox.showinfo("Conversion Complete",
                            "Files have been converted to PNG format.")


root = Tk()
root.geometry("600x900")
app = App(root)
root.mainloop()
