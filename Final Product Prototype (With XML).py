from tkinter import *
import xml.etree.ElementTree as ET
import tkinter.ttk as ttk

"""""
Initialisation:

Title, icon,geometry (resolution)
"""""
root= Tk()
root.title('Drag and drop')
root.iconbitmap('favicon.ico')
root.geometry("1920x1080")
#root.pack_propagate(0)
""""
Initialisation of frames holding the different elements:

frm_left:
    Cropping
    Small movements
    Resolution changes
    Layer use
    Source selection

frm_Main:
    Space where the windows can be drag and dropped and selected for modification

frm_top:
    Save
"""
frm_Left = Frame(root,bg='#3e423f')
frm_Left.place(x=0,y=0,width=450,height=1080)

frm_Main = Frame(root,bg='#a9a9a9')
frm_Main.place(x=545,y=240,width=1280,height=720)

frm_Top = Frame(root,bg='#6a6e6b')
frm_Top.place(x=450,y=0,width=1520,height=180)

"""
Gridding of frames
"""


for i in range(21):
    frm_Left.columnconfigure(i,weight=1)
for i in range(60):
    frm_Left.rowconfigure(i,weight=1)

for i in range(61):
    frm_Top.columnconfigure(i,weight=1)
for i in range(21):
    frm_Top.rowconfigure(i,weight=1)

'''
Output initialisation
'''
#[State,x,y,width,height,source]
global Layers
Layers=[['False',0,0,0,0,'HDMI1'],['False',0,0,0,0,'HDMI2'],['False',0,0,0,0,'HDMI3'],['False',0,0,0,0,'HDMI4']]

"""
Initialising label variables
"""
label0, label1, label2, label3 = 0,0,0,0

"""
Drag and drop feature
"""

def drag_start(event):
    global Select, label0, label1, label2, label3
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
 
"""
Precise movement
"""
def move_down():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    widget.place(x=widget.winfo_x(),y=widget.winfo_y()+5)

def move_up():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    widget.place(x=widget.winfo_x(),y=widget.winfo_y()-5)

def move_right():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    widget.place(x=widget.winfo_x()+5,y=widget.winfo_y())

def move_left():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    widget.place(x=widget.winfo_x()-5,y=widget.winfo_y())

"""
Cropping
"""

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() + 6
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())
    

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() + 26
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())
    
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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() - 14
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["width"] = widget.winfo_width() - 34
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() + 6
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() + 26
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = widget.winfo_height() - 14
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())

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
    frm_Main.update()
    print(widget.winfo_width(),widget.winfo_height())

"""
Layer enabling
"""

def Initialise_1():
    global label0
    #print(start_1.get())
    if start_1.get() == 0:
        Layers[1][0] = 'False'
        label0.destroy()
    elif start_1.get() == 1:
        label0 = Canvas(frm_Main,bg="red",width=476,height=266)
        label0.place(x=0,y=0)
        label0.create_line(0,0,477,267)
        label0.create_line(477,0,0,267)
        label0.bind("<Button-1>",drag_start)
        label0.bind("<B1-Motion>",drag_motion)
        Layers[0][0] = 'True'

def Initialise_2():
    global label1
    #print(start_2.get())
    if start_2.get() == 0:
        Layers[1][0] = 'False'
        label1.destroy()
    elif start_2.get() == 1:
        label1 = Canvas(frm_Main,bg="blue",width=476,height=266)
        label1.place(x=100,y=100)
        label1.create_line(0,0,477,267)
        label1.create_line(477,0,0,267)
        label1.bind("<Button-1>",drag_start)
        label1.bind("<B1-Motion>",drag_motion)
        Layers[1][0] = 'True'

def Initialise_3():
    global label2
    #print(start_3.get())
    if start_3.get() == 0:
        Layers[2][0] = 'False'
        label2.destroy()
    elif start_3.get() == 1:
        label2 = Canvas(frm_Main,bg="green",width=476,height=266)
        label2.place(x=200,y=200)
        label2.create_line(0,0,477,267)
        label2.create_line(477,0,0,267)
        label2.bind("<Button-1>",drag_start)
        label2.bind("<B1-Motion>",drag_motion)
        Layers[2][0] = 'True'

def Initialise_4():
    global label3
    #print(start_4.get())
    if start_4.get() == 0:
        Layers[3][0] = 'False'
        label3.destroy()
    elif start_4.get() == 1:
        label3 = Canvas(frm_Main,bg="yellow",width=476,height=266)
        label3.place(x=300,y=300)
        label3.create_line(0,0,477,267)
        label3.create_line(477,0,0,267)
        label3.bind("<Button-1>",drag_start)
        label3.bind("<B1-Motion>",drag_motion)
        Layers[3][0] = 'True'

"""
Resolution changing
"""

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
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    print(float(ResChange_entryString.get()))
    widget["height"] = round(int(widget.winfo_height())*float(ResChange_entryString.get())-4)
    widget["width"] = round(int(widget.winfo_width())*float(ResChange_entryString.get())-4)
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())
    widget.delete("all")
    widget.create_line(0,0,widget.winfo_width()-4,widget.winfo_height()-4)
    widget.create_line(widget.winfo_width()-4,0,0,widget.winfo_height()-4)

#small resolution changes
def ChangeRes_inc_up():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = round(int(widget.winfo_height())*1.01-4)
    widget["width"] = round(int(widget.winfo_width())*1.01-4)
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())
    widget.delete("all")
    widget.create_line(0,0,widget.winfo_width()-4,widget.winfo_height()-4)
    widget.create_line(widget.winfo_width()-4,0,0,widget.winfo_height()-4)

def ChangeRes_inc_down():
    global Select
    if Select == 1:
        widget = label0
    elif Select == 2:
        widget = label1
    elif Select == 3:
        widget = label2
    elif Select == 4:
        widget = label3
    #print("start" +  str(widget.winfo_width()),str(widget.winfo_height()))
    widget["height"] = round(int(widget.winfo_height())*0.99-4)
    widget["width"] = round(int(widget.winfo_width())*0.99-4)
    frm_Main.update()
    #print(widget.winfo_width(),widget.winfo_height())
    widget.delete("all")
    widget.create_line(0,0,widget.winfo_width(),widget.winfo_height())
    widget.create_line(widget.winfo_width(),0,0,widget.winfo_height())

"""
Source selection
"""

def source1_select(*arg):
    global Layers
    Layers[0][5] = source1.get()

def source2_select(*arg):
    global Layers
    Layers[1][5] = source2.get()

def source3_select(*arg):
    global Layers
    Layers[2][5] = source3.get()

def source4_select(*arg):
    global Layers
    Layers[3][5] = source4.get()

"""
Widgets: Resolution
"""

ResChange_entryString = StringVar(value='1')
ResChange_Entry = Entry(frm_Left,text = 'Enter resolution multiplier', textvariable= ResChange_entryString)
#Placement
ResChange_Entry.grid(row=27,column=11)

ResChange = Button(frm_Left, text = 'Confirm',  command = lambda: ChangeRes(ResChange_entryString))
#Placement
ResChange.grid(row=28,column=11)

ResChange_up = Button(frm_Left, text = '+',  command = lambda: ChangeRes_inc_up())
#Placement
ResChange_up.grid(row=27,column=12,sticky='w')

ResChange_down = Button(frm_Left, text = '-',  command = lambda: ChangeRes_inc_down())
#Placement
ResChange_down.grid(row=27,column=10,sticky='e')

"""
Widgets: Cropping
"""

wButton_up_10 = Button(frm_Left,text = "Width: +10", command = Wresize_up_10)

wButton_up_30 = Button(frm_Left,text = "Width: +30", command = Wresize_up_30)

wButton_down_10 = Button(frm_Left,text = "Width: -10", command = Wresize_down_10)

wButton_down_30 = Button(frm_Left,text = "Width: -30", command = Wresize_down_30)

hButton_up_10 = Button(frm_Left,text = "Height: +10", command = Hresize_up_10)

hButton_up_30 = Button(frm_Left,text = "Height: +30", command = Hresize_up_30)

hButton_down_10 = Button(frm_Left,text = "Height: -10", command = Hresize_down_10)

hButton_down_30 = Button(frm_Left,text = "Height: -30", command = Hresize_down_30)

#Placement
wButton_up_10.grid(row=3,column=12,sticky='w')
wButton_up_30.grid(row=3,column=12,sticky='e')
wButton_down_10.grid(row=3,column=10)
wButton_down_30.grid(row=3,column=9)
hButton_up_10.grid(row=2,column=11)
hButton_up_30.grid(row=1,column=11)
hButton_down_10.grid(row=4,column=11)
hButton_down_30.grid(row=5,column=11)

"""
Widgets: Initialisaiton
"""

start_1 = IntVar()
start_2 = IntVar()
start_3 = IntVar()
start_4 = IntVar()

Bstart_1 = Checkbutton(frm_Left,text = "Layer 1",variable=start_1,command=Initialise_1)
Bstart_1.grid(row=13,column=11)

Bstart_2 = Checkbutton(frm_Left,text = "Layer 2",variable=start_2,command=Initialise_2)
Bstart_2.grid(row=14,column=11)

Bstart_3 = Checkbutton(frm_Left,text = "Layer 3",variable=start_3,command=Initialise_3)
Bstart_3.grid(row=15,column=11)

Bstart_4 = Checkbutton(frm_Left,text = "Layer 4",variable=start_4,command=Initialise_4)
Bstart_4.grid(row=16,column=11)

"""
Widgets: Precise movement
"""

Bmove_down= Button(frm_Left,text = 'D',command= move_down)
Bmove_down.grid(row=35,column=11)

Bmove_up= Button(frm_Left,text = 'D',command= move_up)
Bmove_up.grid(row=33,column=11)

Bmove_right= Button(frm_Left,text = 'D',command= move_right)
Bmove_right.grid(row=34,column=12)

Bmove_left= Button(frm_Left,text = 'D',command= move_left)
Bmove_left.grid(row=34,column=10)

"""
Widgets: Source selection
"""

source1=StringVar()
combobox1 = ttk.Combobox(frm_Left,textvariable = source1)
combobox1['state']='readonly'
combobox1['values'] = ('HDMI1','HDMI2','HDMI3','HDMI4','HDMI5','HDMI6','HDMI7','HDMI8')

source1.trace_add('write',source1_select)

source2=StringVar()
combobox2 = ttk.Combobox(frm_Left,textvariable = source2,command = source2_select())
combobox2['state']='readonly'
combobox2['values'] = ('HDMI1','HDMI2','HDMI3','HDMI4','HDMI5','HDMI6','HDMI7','HDMI8')

source2.trace_add('write',source2_select)

source3=StringVar()
combobox3 = ttk.Combobox(frm_Left,textvariable = source3,command = source3_select())
combobox3['state']='readonly'
combobox3['values'] = ('HDMI1','HDMI2','HDMI3','HDMI4','HDMI5','HDMI6','HDMI7','HDMI8')

source3.trace_add('write',source3_select)

source4=StringVar()
combobox4 = ttk.Combobox(frm_Left,textvariable = source4,command = source4_select())
combobox4['state']='readonly'
combobox4['values'] = ('HDMI1','HDMI2','HDMI3','HDMI4','HDMI5','HDMI6','HDMI7','HDMI8')

source4.trace_add('write',source4_select)

#Placement
combobox1.grid(row=13,column=12,sticky='w')
combobox2.grid(row=14,column=12,sticky='w')
combobox3.grid(row=15,column=12,sticky='w')
combobox4.grid(row=16,column=12,sticky='w')

"""
Widgets: Output prep
"""
def SaveAll():
    global Layers
    Activated_1,Activated_2,Activated_3,Activated_4 = 0,0,0,0
    if Layers[0][0] == 'True':
        Activated_1 = 1
        Layers[0][1] = label0.winfo_x()
        Layers[0][2] = label0.winfo_y()
        Layers[0][3] = label0.winfo_width()
        Layers[0][4] = label0.winfo_height()
    if Layers[1][0] == 'True':
        Activated_2 = 1
        Layers[1][1] = label1.winfo_x()
        Layers[1][2] = label1.winfo_y()
        Layers[1][3] = label1.winfo_width()
        Layers[1][4] = label1.winfo_height()
    if Layers[2][0] == 'True':
        Activated_3 = 1
        Layers[2][1] = label2.winfo_x()
        Layers[2][2] = label2.winfo_y()
        Layers[2][3] = label2.winfo_width()
        Layers[2][4] = label2.winfo_height()
    if Layers[3][0] == 'True':
        Activated_4 = 1
        Layers[3][1] = label3.winfo_x()
        Layers[3][2] = label3.winfo_y()
        Layers[3][3] = label3.winfo_width()
        Layers[3][4] = label3.winfo_height()

    f = open("xml_output", "a")
    f.write(
        '\t'+'<Macro index="2" name="ACL+ELO" description="">' + '\n' 
        +'<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="0" enable="'+ Layers[0][0] +'"/>' + '\n'
        +'<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="1" enable="'+ Layers[1][0] +'"/>' + '\n'
        +'<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" enable="'+ Layers[2][0] +'"/>' + '\n'
        +'<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" enable="'+ Layers[3][0] +'"/>' + '\n'
        )
    if Activated_1 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="0" input="'+ Layers[0][5] +'"/>' + '\n' )
    if Activated_2 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="1" input="'+ Layers[1][5] +'"/>' + '\n' )
    if Activated_3 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" input="'+ Layers[2][5] +'"/>' + '\n' )
    if Activated_4 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="3" input="'+ Layers[3][5] +'"/>' + '\n' )
        
    if Activated_1 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="0" size="'+ str(round(Layers[0][3]/1280,6)) +'"/>' + '\n') 
    if Activated_2 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="1" size="'+ str(round(Layers[1][3]/1280,6)) +'"/>'  + '\n')
    if Activated_3 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" size="'+ str(round(Layers[2][3]/1280,6)) +'"/>'  + '\n')
    if Activated_4 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="3" size="'+ str(round(Layers[3][3]/1280,6)) +'"/>' + '\n' )

    if Activated_1 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="0" xPosition="'+ str(round((((Layers[0][1]+(Layers[0][3]/2))/1280*1920)-960)/60,6)) +'"/>' + '\n' )
    if Activated_2 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="1" xPosition="'+ str(round((((Layers[1][1]+(Layers[1][3]/2))/1280*1920)-960)/60,6)) +'"/>' + '\n' )
    if Activated_3 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" xPosition="'+ str(round((((Layers[2][1]+(Layers[2][3]/2))/1280*1920)-960)/60,6)) +'"/>' + '\n' )
    if Activated_4 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="3" xPosition="'+ str(round((((Layers[3][1]+(Layers[3][3]/2))/1280*1920)-960)/60,6)) +'"/>' + '\n' )
    
    if Activated_1 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="0" yPosition="'+ str(round((((Layers[0][2]+(Layers[0][4]/2))/720*1080)-540)/60,6)) +'"/>' + '\n' )
    if Activated_2 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="1" yPosition="'+ str(round((((Layers[1][2]+(Layers[1][4]/2))/720*1080)-540)/60,6)) +'"/>' + '\n' )
    if Activated_3 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="2" yPosition="'+ str(round((((Layers[2][2]+(Layers[2][4]/2))/720*1080)-540)/60,6)) +'"/>' + '\n' )
    if Activated_4 == 1:
        f.write('<Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="3" yPosition="'+ str(round((((Layers[3][2]+(Layers[3][4]/2))/720*1080)-540)/60,6)) +'"/>' + '\n' )
    f.write('</Macro>')
    f.close()
    

    

#Layers=[['False',0,0,0,0,'HDMI1'],['False',0,0,0,0,'HDMI2'],['False',0,0,0,0,'HDMI3'],['False',0,0,0,0,'HDMI4']]

Save = Button(frm_Top,text = "Save",font=('TkDefaultFont',15,'bold'), command = SaveAll)
#placemenet
Save.grid(row=2,column=52,rowspan=2,columnspan=3,stick='nswe')














root.mainloop()
