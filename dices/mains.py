import tkinter
from PIL import Image, ImageTk
import pygame
import random

root = tkinter.Tk()
root.title("DICE")
root.geometry('800x600')

pygame.mixer.init()   

bg =tkinter.PhotoImage(file="images\jj2.png")
my_label =tkinter.Label(root, image=bg,bd=0)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

label1 =tkinter.Label(root,font=("Sans Serif",400,'bold'),text="" ,fg="Red")

click_btn = tkinter.PhotoImage(file ="images\cp.gif")

Dice = [r'images\1.png',r'images\2.png',r'images\3.png',r'images\4.png',r'images\5.png',r'images\6.png']

image1 =ImageTk.PhotoImage(Image.open(random.choice(Dice)))
label1 = tkinter.Label(root,image=image1)
label1.image = image1

def rolling():
    image1 =ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    label1.configure(image=image1)
    label1.image = image1
    label1.pack(expand=True)
    pygame.mixer.music.load(filename=r"images\roll.wav")
    pygame.mixer.music.play()

button = tkinter.Button(root,image = click_btn,command=rolling,height=40,width=200)
button.pack(pady=5) 

root.mainloop()