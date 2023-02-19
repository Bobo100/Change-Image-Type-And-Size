import tkinter as tk

class MyApplication:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x900")

        self.input_files_images_frame = tk.Frame(self.master)
        self.input_files_images_frame.grid(row=0, column=0, sticky="nsew")
        self.master.columnconfigure(0, weight=1) # 設定第 0 列權重為 1

root = tk.Tk()
app = MyApplication(root)
root.mainloop()
