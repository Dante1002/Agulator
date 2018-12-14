from tkinter import *
import funkcje as f

root = Tk()
theLabel = Label(root, text="This wasn't hard",height=5)
theLabel.pack()



Frame1 = Frame(root)
Frame2 = Frame(root)
Frame3 = Frame(root)
Frame4 = Frame(root)
Frame5 = Frame(root)

Frame1.pack(side=TOP)
Frame2.pack(side=TOP)
Frame3.pack(side=TOP)
Frame4.pack(side=TOP)
Frame5.pack(side=TOP)

x=2
y=5

button1 = Button(Frame1, text="%", fg="red", height=x, width= y)
button2 = Button(Frame1, text="CE", fg="red", height=x, width=y)
button3 = Button(Frame1, text="C", fg="red", height=x, width=y)
button4 = Button(Frame1, text="delete", fg="red", height=x, width= y)
button5 = Button(Frame1, text="/", fg="red", height=x, width= y)

button21 = Button(Frame2, text="sqrt", fg="red", height=x, width= y)
button22 = Button(Frame2, text="7", fg="green", height=x, width= y)
button23 = Button(Frame2, text="8", fg="green",height=x, width= y)
button24 = Button(Frame2, text="9", fg="green",height=x, width= y)
button25 = Button(Frame2, text="x", fg="green",height=x, width= y)


button31 = Button(Frame3, text="x^2", fg="red", height=x, width= y)
button32 = Button(Frame3, text="5", fg="green" ,height=x, width= y)
button33 = Button(Frame3, text="6", fg="green",height=x, width= y)
button34 = Button(Frame3, text="7", fg="green",height=x, width= y)
button35 = Button(Frame3, text="-", fg="green",height=x, width= y)

button41 = Button(Frame4, text="x^3", fg="red", height=x, width= y)
button42 = Button(Frame4, text="1", fg="green" ,height=x, width= y, command = f.show_number(1))
button43 = Button(Frame4, text="2", fg="green",height=x, width= y)
button44 = Button(Frame4, text="3", fg="green",height=x, width= y)
button45 = Button(Frame4, text="+", fg="green",height=x, width= y)

button51 = Button(Frame5, text="1/x", fg="red", height=x, width= y)
button52 = Button(Frame5, text="+-", fg="green",height=x, width= y)
button53 = Button(Frame5, text="0", fg="green",height=x, width= y)
button54 = Button(Frame5, text=",", fg="green",height=x, width= y)
button55 = Button(Frame5, text="=", fg="red",height=x, width= y)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

button21.pack(side=LEFT)
button22.pack(side=LEFT)
button23.pack(side=LEFT)
button24.pack(side=LEFT)
button25.pack(side=LEFT)

button31.pack(side=LEFT)
button32.pack(side=LEFT)
button33.pack(side=LEFT)
button34.pack(side=LEFT)
button35.pack(side=LEFT)

button41.pack(side=LEFT)
button42.pack(side=LEFT)
button43.pack(side=LEFT)
button44.pack(side=LEFT)
button45.pack(side=LEFT)

button51.pack(side=LEFT)
button52.pack(side=LEFT)
button53.pack(side=LEFT)
button54.pack(side=LEFT)
button55.pack(side=LEFT)




root.mainloop()