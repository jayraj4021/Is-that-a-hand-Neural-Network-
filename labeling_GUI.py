from tkinter import *
from PIL import Image, ImageTk
from os import listdir
from decimal import Decimal

data_dir='/home/jayraj/Desktop/No_mouse_mouse/data_Set/dummy_reg/test/'
files = listdir(data_dir)
total_files = len(files)
file_name='dummy'
coordinate_data_set = "/home/jayraj/Desktop/No_mouse_mouse/data_Set/dummy_reg/coordi_test.csv"
FILE = open(coordinate_data_set,"w")
root= Tk()
fileCounter = 0
coor1 = ""
coor2 = ""

def nextIMG(event):
	global fileCounter 
	global data_dir
	global file_name
	global files
	wlist = root.slaves()
	for w in wlist:
		w.destroy()

	if fileCounter<total_files :
		topFrame = Frame(root)
		topFrame.pack()
		bottomFrame=Frame(root)
		bottomFrame.pack(side=BOTTOM)
		
		load = Image.open(data_dir+files[fileCounter])
		file_name=files[fileCounter]
		fileCounter=fileCounter+1
		photo = ImageTk.PhotoImage(load)
		label1 = Label(topFrame,image=photo)
		label1.image = photo
		label1.bind("<Button-1>",leftClick)
		label1.bind("<Button-3>",rightClick)
		label1.pack()
		
		button1 = Button(bottomFrame,text="nextImage")
		button1.bind("<Button-1>",nextIMG)
		button2 = Button(bottomFrame,text="Done")
		button2.bind("<Button-1>",doneButton)
		status1 = Label(bottomFrame,textvariable=v1,relief=SUNKEN)
		status2 = Label(bottomFrame,textvariable=v2,relief=SUNKEN)
		
		button1.pack(side=LEFT)
		button2.pack(side=LEFT)
		status1.pack(side=LEFT)
		status2.pack(side=LEFT)
	
		v1.set("Coordinate1")
		v2.set("Coordinate2")


def leftClick(event):
	global coor1
	x = round((root.winfo_pointerx() - root.winfo_rootx())/640,4)
	y = round((root.winfo_pointery() - root.winfo_rooty())/480,4)
	coor1 = str(x)+","+str(y)
	v1.set(coor1)

def rightClick(event):
	global coor1
	global coor2
	global file_name
	x = round((root.winfo_pointerx() - root.winfo_rootx())/640,4)
	y = round((root.winfo_pointery() - root.winfo_rooty())/480,4)
	coor2 = str(x)+","+str(y)
	v2.set(coor2)
	FILE.write(file_name+","+coor1+","+coor2+"\n")

def doneButton(event):
	global FILE
	FILE.close()

topFrame = Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame,text="nextImage")
button1.bind("<Button-1>",nextIMG)
button2 = Button(bottomFrame,text="Done")
button2.bind("<Button-1>",doneButton)
v1=StringVar()
v2=StringVar()
status1 = Label(bottomFrame,textvariable=v1,relief=SUNKEN)
status2 = Label(bottomFrame,textvariable=v2,relief=SUNKEN)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
status1.pack(side=LEFT) 
status2.pack(side=LEFT) 

v1.set("Coordinate1")
v2.set("Coordinate2")

root.mainloop()
