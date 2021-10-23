import os
import random
import tkinter as tk
from PIL import Image, ImageTk

class perso:
    def __init__(self,name,annee,picture_path):
        self.name=name
        self.annee=annee
        self.picture_path=os.path.join(script_dir,picture_path)
        self.photoTkinter=None
    
    def photo(self):   #load image
        image = Image.open(self.picture_path).resize((200,256), Image.ANTIALIAS)
        self.photoTkinter = ImageTk.PhotoImage(image)
        return self.photoTkinter

def on_click(m):
    button=button_list[m]
    if button['relief'] == 'raised':
        photo1=ImageTk.PhotoImage(Image.open("delete.jpg"))
        button.config(relief='sunken')
        button.configure(image=photo1)
        button.photo = photo1
    else:
        photo=perso_list[num[m]].photoTkinter
        button.config(relief='raised')
        button.configure(image=photo)
        button.photo = photo

def get():
    global menu_frame
    Game_ID = ent.get()
    menu_frame.destroy()
    menu_frame = game(Game_ID)
    menu_frame.grid()

def get2():
    global menu_frame
    Game_ID = ent2.get()
    menu_frame.destroy()
    menu_frame = game(Game_ID)
    menu_frame.grid()
    
def randomly():
    global menu_frame
    menu_frame.destroy()
    menu_frame = game()
    menu_frame.grid()

def game(Game_ID="0"):
    global num
    global button_list
    global ent
    frame = tk.Frame(root)
    if Game_ID=="0":
        Game_ID=list()
        num=random.sample(range(len(perso_list)), 8*3)
        for i in range(len(num)):
            Game_ID.append(str(num[i]))
        Game_ID='-'.join(Game_ID)
    else:
        num=Game_ID.split('-')
        for i in range(len(num)):
            num[i]=int(num[i])
    cnt=0
    button_list=list()
    for i in range(0,6,2):
        for j in range(8):
            new_button=tk.Button(frame, image=perso_list[num[cnt]].photo(), command=lambda m=cnt : on_click(m),height = 256, width = 200)
            new_button.grid(row=i, column=j)
            button_list.append(new_button)
            tk.Label(frame, text="(%sA) %s" %(str(perso_list[num[cnt]].annee),perso_list[num[cnt]].name)).grid(row=i+1, column=j)
            cnt=cnt+1
    data_string = tk.StringVar()
    data_string.set(Game_ID)
    tk.Label(frame,text="GAME-ID :").grid(row=8, column=0)
    ent = tk.Entry(frame,textvariable=data_string,fg="black",bg="white",state='normal',width=225)
    ent.grid(row=8,column=1,columnspan=7)
    tk.Button(frame, text="Generate with the ID", command = get).grid(row=8, column=8)
    tk.Button(frame, text="Generate radomly",command = randomly).grid(row=7, column=8)
    return frame

def menu():
    global ent2
    frame = tk.Frame(root)
    tk.Button(frame, text = 'Generate Radomly', command = randomly).grid(row = 0, column = 3)
    data_string = tk.StringVar()
    data_string.set('')
    tk.Label(frame,text="GAME-ID :").grid(row=1,column=0)
    ent2=tk.Entry(frame,textvariable=data_string,fg="black",bg="white",state='normal',width=50)
    ent2.grid(row=1,column=1,columnspan=5)
    tk.Button(frame, text = 'Generate with ID',command = get2).grid(row = 1, column = 7)
    return frame

# init   
script_dir = os.path.dirname(os.path.abspath(__file__))
Game_ID=list()
print(script_dir)
file_list=list()
perso_list=list()
folder_list=os.listdir("Pictures")
for folder in folder_list:
    file_list.append(os.listdir("Pictures\%s" %folder))

for i in range(len(file_list)):
    for j in range(len(file_list[i])):
        name=file_list[i][j].split('.')[0]
        annee=i+1
        picture_path="Pictures\%s_a\%s" %(str(i+1),file_list[i][j])
        perso_list.append(perso(name,annee,picture_path))

#main

root = tk.Tk()
root.wm_title('Whoswho')

menu_frame = menu()
menu_frame.grid()

root.mainloop()