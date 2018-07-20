from PIL import Image

from tkinter import filedialog
import tkinter as tk
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
#要索引的字符列表
def convert(img):
    img = img.convert("L")  # 转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))     # 获取每个坐标像素点的灰度
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)] #获取对应坐标的字符值
        txt += '\n'
    return  txt

def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r,g,b = img.getpixel((j, i))           #获取每个坐标像素点的rgb值
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)   #通过灰度转换公式获取灰度
            unit = (256.0+1)/length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt
def get_txt(pic_file):
    save_file = 'saveText/1.txt'
    
    img = Image.open(pic_file)      #读取图像文件
    (width,height) = img.size
    #img = img.resize((int(width*0.2),int(height*0.1)))  #对图像进行一定缩小,图片的大小可以根据上传图片的大小来按需调节，
    img = img.resize((100,50))
    #print(img.size)

    txt = convert(img)
    #print(txt)

    return txt
def open_file():
    path = filedialog.askopenfilename(title='打开图片文件', filetypes=[('jpg', '*.jpg'),('png','*.png'), ('All Files', '*')])
    txt = get_txt(path)
    txtString.set(txt)
    text.delete(1.0,tk.END)
    text.insert(1.0, txt)  # INSERT表示在光标位置插入
    text.see(tk.END)
    text.update()
def save_file():
    path = filedialog.askdirectory(title='选择保存路径')
    
    f = open(path+'/1.txt',"w")
    f.write(txtString.get())            #存储到文件中
    f.close()
def copy(event=None):
    #text.event_generate("<<Copy>>")    
    root.clipboard_append(txtString.get())
root = tk.Tk()

root.geometry('750x700+750+700')
root.title('图片转文本')
#root.iconbitmap('icon/icon.ico')
txtString = tk.StringVar()


btn1 = tk.Button(root, text='打开图片文件',font =("宋体",10,'bold'),width=30,height=2, command=open_file)
btn2 = tk.Button(root, text='复制',font = ('宋体',10,'bold'),width=15,height=2,command = copy)
btn3 = tk.Button(root, text='保存',font = ('宋体',10,'bold'),width=15,height=2,command = save_file)
btn4 = tk.Button(root, text='退出',font = ("宋体",10,'bold'),width=30,height=2, command=root.quit)

btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row = 0, column = 2)
btn4.grid(row = 0, column = 3)

text=tk.Text(root,width=100,height=50)
text.grid(row=1,columnspan=4)
#menubar=tk.Menu(root)
#filemenu=tk.Menu(menubar)
#root.config(menu=menubar)

#filemenu.add_command(label="复制",command=copy)
#menubar.add_cascade(label="文件",menu=filemenu)


root.mainloop()
