from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os
from tkinter.font import Font

class App:
    def __init__(self, master):
        self.master = master
        master.title("圖片上傳")
        master.geometry("800x600")
        
        # 設定左側的 Listbox (文字)
        self.filesName_listbox_Label = Label(root, text="檔名")
        self.filesName_listbox_Label.grid(row=0, column=0, sticky="w")
        
        
        # self.listbox_font = ("Arial", 110)
        # self.filesName_listbox = Listbox(root, selectmode=MULTIPLE, font=self.listbox_font)
        self.filesName_listbox = Listbox(root, selectmode=MULTIPLE)
        self.filesName_listbox.grid(row=1, column=0, sticky="nsew")       

        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        
        self.filesName_listbox_contents = []
        
       # 設定右側的 Listbox (圖片)
        self.filesImages_listbox_Label = Label(root, text="圖片")
        self.filesImages_listbox_Label.grid(row=0, column=1, sticky="w")
       
        self.filesImages_listbox = Listbox(root, selectmode=MULTIPLE)
        self.filesImages_listbox.grid(row=1, column=1, sticky="nsew")
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        
        self.filesImages_listbox_contents = []

        # 設定上傳按鈕
        self.upload_button = Button(root, text="上傳圖片", command=self.upload)
        self.upload_button.grid(row=2, column=0, columnspan=2, padx=10,pady=10, ipadx=10, ipady=10, sticky="nsew")
        
    def upload(self):
         # set the filetypes to .jpg, .png and .tiff
        filetypes = [("JPEG", "*.jpg"), ("PNG", "*.png"), ("TIFF", "*.tiff")]
        # show file dialog
        files = filedialog.askopenfilenames(
            filetypes=filetypes, title="Select files to convert")
        
        for file in files:
            if file not in self.filesName_listbox_contents:
                # 文件名稱放在左側的 Listbox
                self.filesName_listbox.insert(END, file)
                   
                # 圖片放在右側的 Listbox
                # 建立一個新的frame (用來放圖片) 並放在listbox裡
                fileImage_frame = Frame(self.filesImages_listbox, bd=2, relief="solid")
                fileImage_frame.grid(sticky="nsew")

                # 開啟圖片
                img = Image.open(file)
                img = img.resize((120, 120), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

                # 建立一個label 用來顯示圖片 並把圖片放在frame裡
                label = Label(fileImage_frame, image=img)
                label.image = img
                label.grid(sticky="nsew")
                fileImage_frame.columnconfigure(0, weight=1)
                fileImage_frame.rowconfigure(0, weight=1)                

                # 記錄圖片和檔案名稱
                self.filesName_listbox_contents.append(file)
                self.filesImages_listbox_contents.append(fileImage_frame)
                
if __name__ == '__main__':

    root = Tk()
    app = App(root)
    root.mainloop()