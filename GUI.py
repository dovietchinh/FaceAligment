from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import cv2
from faceswap import faceswapfunc
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img1():
    global path_input_1
    x = openfn()
    img = Image.open(x)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=20,y=20)
    path_input_1 = x
def open_img2():
    global path_input_2
    x = openfn()
    img = Image.open(x)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=20,y=320+20) 
    path_input_2 = x   
def open_camera():
    global path_input_2
    cap=cv2.VideoCapture(0)
    cv2.namedWindow('a',cv2.WINDOW_NORMAL)
    while(1):
        ret,frame = cap.read()
        if ret==True:
            cv2.imshow('a',frame)
        if(cv2.waitKey(1)==ord('q')):
            frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame2=Image.fromarray(frame2)
            img = frame2.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.place(x=20,y=320+20)
            cv2.imwrite('a.png',frame)
            path_input_2='a.png'
            break
    cv2.destroyAllWindows()

def process():
    faceswapfunc('b.png',path_input_1,path_input_2)
    x='b.png'
    img = Image.open(x)
    img = img.resize((600, 600), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=320+20,y=20) 
path_input_1 =""
path_input_2 =""
path_output =""
root = Tk()
root.geometry("1600x1000")
root.resizable(width=True, height=True)
btn = Button(root, text='open image', command=open_img1)
btn.place(x=1000,y=100)
btn3 = Button(root,text='open_image2',command=open_img2)
btn3.place(x=1000,y=200)
btn2 = Button(root,text= 'open camera',command=open_camera)
btn2.place(x=1000,y=300)
btn_process = Button(root,text = 'show result',command = process)
btn_process.place(x=1000,y=400)

root.mainloop()