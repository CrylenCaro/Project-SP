from tkinter import *
import xml.etree.ElementTree as ET

#Initialisation
root= Tk()
root.title('Drag and drop')
root.iconbitmap('favicon.ico')
root.geometry("1920x1080")
#root.pack_propagate(0)

frm = Frame(root,bg="gray")
frm.place(x=400,y=200,width=960,height=540)


def drag_start(event):
    global Select
    widget = event.widget
    if widget == label0:
        Select = 1
    elif widget == label1:
        Select = 2
    elif widget == label2:
        Select = 3
    elif widget == label3:
        Select = 4
    widget.startX = event.x
    widget.startY = event.y

#+4 for dimensions 
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
 
def Wresize_up_10():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() + 6
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())
    

def Wresize_up_30():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() + 26
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())
    
def Wresize_down_10():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() - 14
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Wresize_down_30():
    
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() - 34
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Hresize_up_10():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() + 6
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Hresize_up_30():
    
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() + 26
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Hresize_down_10():

    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() - 14
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Hresize_down_30():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() - 34
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

def Initialise():
    if start_0.get()==1:
        global label0
        label0 = Canvas(frm,bg="red",width=477,height=267)
        label0.place(x=0,y=0)
        label0.bind("<Button-1>",drag_start)
        label0.bind("<B1-Motion>",drag_motion)
        Layers[0][0] = True
    if start_1.get()==1:
        global label1
        label1 = Canvas(frm,bg="blue",width=477,height=267)
        label1.place(x=100,y=100)
        label1.bind("<Button-1>",drag_start)
        label1.bind("<B1-Motion>",drag_motion)
        Layers[1][0] = True
    if start_2.get()==1:
        global label2
        label2 = Canvas(frm,bg="green",width=477,height=267)
        label2.place(x=200,y=200)
        label2.bind("<Button-1>",drag_start)
        label2.bind("<B1-Motion>",drag_motion)
        Layers[2][0] = True
    if start_3.get()==1:
        global label3
        label3 = Canvas(frm,bg="yellow",width=477,height=267)
        label3.place(x=300,y=300)
        label3.bind("<Button-1>",drag_start)
        label3.bind("<B1-Motion>",drag_motion)
        Layers[3][0] = True

def ChangeRes(Multi):
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = round(int(widget.winfo_height())*float(ResChange_entryString.get())-4)
    widget["width"] = round(int(widget.winfo_width())*float(ResChange_entryString.get())-4)
    frm.update()
    print(widget.winfo_width(),widget.winfo_height())

ResChange_entryString = StringVar(value='1')
ResChange_Entry = Entry(root,text = 'Enter resolution multiplier', textvariable= ResChange_entryString)
ResChange_Entry.pack()

ResChange = Button(root, text = 'Confirm',  command = lambda: ChangeRes(ResChange_entryString))
ResChange.pack()

wButton_up_10 = Button(root,text = "Width: +10", command = Wresize_up_10)
wButton_up_10.pack(side = TOP, anchor = NW, padx=30)

wButton_up_30 = Button(root,text = "Width: +30", command = Wresize_up_30)
wButton_up_30.pack(side = TOP, anchor = NW, padx=30)

wButton_down_10 = Button(root,text = "Width: -10", command = Wresize_down_10)
wButton_down_10.pack(side = TOP, anchor = NW, padx=30)

wButton_down_30 = Button(root,text = "Width: -30", command = Wresize_down_30)
wButton_down_30.pack(side = TOP, anchor = NW, padx=30)

hButton_up_10 = Button(root,text = "Height: +10", command = Hresize_up_10)
hButton_up_10.pack(side = TOP, anchor = NW, padx=30)

hButton_up_30 = Button(root,text = "Height: +30", command = Hresize_up_30)
hButton_up_30.pack(side = TOP, anchor = NW, padx=30)

hButton_down_10 = Button(root,text = "Height: -10", command = Hresize_down_10)
hButton_down_10.pack(side = TOP, anchor = NW, padx=30)

hButton_down_30 = Button(root,text = "Height: -30", command = Hresize_down_30)
hButton_down_30.pack(side = TOP, anchor = NW, padx=30)

start_0 = IntVar()
start_1 = IntVar()
start_2 = IntVar()
start_3 = IntVar()

Bstart_0 = Checkbutton(root,text = "Layer 1",variable=start_0)
Bstart_0.pack(side=BOTTOM, anchor = SW,padx=30,pady=30)

Bstart_1 = Checkbutton(root,text = "Layer 2",variable=start_1)
Bstart_1.pack(side=BOTTOM, anchor = SW,padx=30,pady=30)

Bstart_2 = Checkbutton(root,text = "Layer 3",variable=start_2)
Bstart_2.pack(side=BOTTOM, anchor = SW,padx=30,pady=30)

Bstart_3 = Checkbutton(root,text = "Layer 4",variable=start_3)
Bstart_3.pack(side=BOTTOM, anchor = SW,padx=30,pady=30)

START_BUTTON = Button(root,text = "Start", command = Initialise)
START_BUTTON.pack(side = TOP, anchor = NE)

#[State,x,y,width,height]
global Layers
Layers=[[False,0,0,0,0],[False,0,0,0,0],[False,0,0,0,0],[False,0,0,0,0]]

def SaveAll():
    if Layers[0][0] == True:
        Layers[0][1] = label0.winfo_x()
        Layers[0][2] = label0.winfo_y()
        Layers[0][3] = label0.winfo_width()
        Layers[0][4] = label0.winfo_height()
    if Layers[1][0] == True:
        Layers[1][1] = label1.winfo_x()
        Layers[1][2] = label1.winfo_y()
        Layers[1][3] = label1.winfo_width()
        Layers[1][4] = label1.winfo_height()
    if Layers[2][0] == True:
        Layers[2][1] = label2.winfo_x()
        Layers[2][2] = label2.winfo_y()
        Layers[2][3] = label2.winfo_width()
        Layers[2][4] = label2.winfo_height()
    if Layers[3][0] == True:
        Layers[3][1] = label3.winfo_x()
        Layers[3][2] = label3.winfo_y()
        Layers[3][3] = label3.winfo_width()
        Layers[3][4] = label3.winfo_height()
    print(Layers)
    
Save = Button(root,text = "Save", command = SaveAll)
Save.pack(side = TOP, anchor = NE)


root.mainloop()
