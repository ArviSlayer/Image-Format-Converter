from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

app = Tk()
app.geometry('200x200')
app.resizable(0,0)
app.title("ArviS | Image Format Converter")
img = PhotoImage(file="icon.png")
width, height = img.width(), img.height()
canvas = Canvas(app, width=width, height=height)
canvas.place(x=0,y=0)
canvas.create_image((0, 0), image=img, anchor="nw")

checkformat = IntVar()
checkformat.set(1)

checkpng = ttk.Radiobutton(app,text="PNG Formatına Dönüştür",variable=checkformat,value=1).pack()
checkjpg = ttk.Radiobutton(app,text="JPG Formatına Dönüştür",variable=checkformat,value=2).pack()
checkjpeg = ttk.Radiobutton(app,text="JPEG Formatına Dönüştür",variable=checkformat,value=3).pack()



def process(extension):
        try:
            fileExtension = str(extension)
            source = getSource()
            im = Image.open(source)
            rgb_im = im.convert("RGB")
            target = f"{getTarget()}"+"/output."+fileExtension
            rgb_im.save(target)
            messagebox.showinfo("Arvİs | Image Format Converter",f"Dönüştürme İşlemi Başarılı \n Kaydedilen Dizin:\n{target}")
        except Exception as e:
            messagebox.showerror("Hata, Desteklenmeyen Format",f"{e}")

def getSource():
    return filedialog.askopenfilename()

def getTarget():
    return filedialog.askdirectory()

def convert():
    
    checker = checkformat.get()
    if checker==1:
        process("png")
    elif checker==2:
        process("jpg")
    else:
        process("jpeg")

button = ttk.Button(app,text="Çevir",command=convert).place(x=63,y=110)
app.mainloop()
