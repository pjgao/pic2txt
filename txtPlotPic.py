from tkinter import ttk    
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)


#要索引的字符列表
def convert(img, bin = False):
    #print(size)
    try:
        if pathVariable.get().split('.')[-1] in ['mp4','avi']:
            #img = cv2.resize(img,(img.shape[0]//10,img.shape[1]//10))
            img = cv2.resize(img,(100,50))
        elif img.shape[0] >= 50 and img.shape[1] >= 100:
            img = cv2.resize(img,(100,50))
        #优化显示效果，统一缩放到100x50
    except:
        messagebox.showwarning('文件错误','文件大小有误，请重新选择')

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if bin:
    #二值化
        _,img = cv2.threshold(img,thresh.get()*255//100,255,cv2.THRESH_BINARY)
    txt = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            #print(i,j,img[i][j])
            location = int(img[i][j]/(256/length))
            txt += ascii_char[location]
        txt += '\n'
    return  txt


def update_txt_by_img(img,txtString,bin = False):
    txt = convert(img, bin = bin)
            
    txtString.set(txt)
    text.delete(1.0,tk.END)
    text.insert(1.0, txt)  # INSERT表示在光标位置插入
    text.see(tk.END)
    text.update()
def open_file():    
    
    path = filedialog.askopenfilename(title='打开图片文件', filetypes=[('All Files', '*'),('mp4','*.mp4'),('jpg', '*.jpg'),('png','*.png')])
    pathVariable.set(path)
    if path.split('.')[-1] in ['mp4','avi']:
        v = cv2.VideoCapture(path)
        WIDTH = v.get(3)        
        HEIGHT = v.get(4)    #FRAME_RATE = v.get(5)
        FRAME_NUM = int(v.get(7))
        flag = True
        for i in range(FRAME_NUM):            
            cv2.waitKey(1)
            _,img = v.read()   
            update_txt_by_img(img,txtString,bin = binary.get())
            if stopVariable.get():
                while(stopVariable.get()):
                    pass

    elif path.split('.')[-1] in ['png','jpg','jpeg']:
       
        img = cv2.imread(path)
        update_txt_by_img(img,txtString,binary.get())
    
    
def save_file():
    path = filedialog.askdirectory(title='选择保存路径')
    
    f = open(path+'/1.txt',"w")
    f.write(txtString.get())            #存储到文件中
    f.close()
def copy(event=None):
#text.event_generate("<<Copy>>")    
    root.clipboard_append(txtString.get())

def check():
    #binary.set(True)
    if pathVariable.get().split('.')[-1] in ['jpg','jpeg','png']:
        img = cv2.imread(pathVariable.get())
        update_txt_by_img(img,txtString,binary.get())
                
def thresh_scale():
    '''
    当选择的是图片时，更新阈值后需要重新读取图片再显示出来
    '''
    if binary.get() and pathVariable.get().split('.')[-1] in ['png','jpg','jpeg']:
        img = cv2.imread(pathVariable.get())
        update_txt_by_img(img,txtString,binary.get())        
def stop_music():   
    #stopVariable.set(not stopVariable.get())
    pass
    
def ck2_callback():
    print(stopVariable.get())

root = tk.Tk()

root.geometry('750x700+750+700')
root.title('图片转文本')
#root.iconbitmap('icon/icon.ico')
txtString = tk.StringVar()
binary = tk.BooleanVar()
thresh = tk.IntVar()
pathVariable = tk.StringVar()
stopVariable = tk.BooleanVar()
#stopVariable.set(False)

btn11 = tk.Button(root, text='打开图片或视频',font =("宋体",10,'bold'),width=30,height=2, command=open_file)
btn12 = tk.Button(root, text='复制',font = ('宋体',10,'bold'),width=15,height=2,command = copy)
btn13 = tk.Button(root, text='保存',font = ('宋体',10,'bold'),width=15,height=2,command = save_file)
btn14 = tk.Button(root,text = '停/启',font = ('宋体',10,'bold'),width =15,height=2,command=stop_music)
btn15 = tk.Button(root, text='退出',font = ("宋体",10,'bold'),width=15,height=2, command=root.quit)

ck1 = tk.Checkbutton(root, text='二值化', width=5,command=check,variable = binary)
label11 = tk.Label(root, text='阈值:',width=5,height=2)
spin = tk.Spinbox(root, from_=1,to=100, width=5, bd=8,textvariable=thresh,command = thresh_scale) 
ck2 = tk.Checkbutton(root, text='暂停',width=5,variable=stopVariable,command=ck2_callback)
ck1.grid(row =1,column = 0 )
spin.grid(row=1,column=2)
label11.grid(row=1,column=1,sticky='E')
ck2.grid(row=1,column=3)
btn11.grid(row = 0, column = 0,columnspan=3)
btn12.grid(row = 0, column = 3)
btn13.grid(row = 0, column = 4)
btn14.grid(row = 0, column = 5)
btn15.grid(row = 0, column = 6)

text=tk.Text(root,width=100,height=50)
text.grid(row=2,columnspan=7)
#menubar=tk.Menu(root)
#filemenu=tk.Menu(menubar)
#root.config(menu=menubar)

#filemenu.add_command(label="复制",command=copy)
#menubar.add_cascade(label="文件",menu=filemenu)


root.mainloop()
