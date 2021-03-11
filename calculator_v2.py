from tkinter import *

root = Tk()
root.title("Calculator of Photographer")


# Calculator_1

frame1 = LabelFrame(root, text="< CALCULATOR - 1 >", bg="#FFDC85")
frame1.pack(padx=5, pady=5)


def calculator1():
    call1 = int(e3.get()) * int(e1.get()) / int(e2.get())
    print(round(call1, 8))


frame2 = LabelFrame(frame1, text="< OBJECT SIZE IN THE CAMERA MATRIX >", fg="maroon", bg="#C9ECEC")
frame2.pack(padx=20, pady=15)

l1 = Label(frame2, text='Enter Camera Matrix size in mm:', width=35, pady=5, bg="#C9ECEC")
l1.grid(row=0, column=0)

e1 = Entry(frame2, width=10, borderwidth=3)
e1.get()
e1.grid(row=0, column=1)
e1.insert(0, '')

l2 = Label(frame2, text='Enter Image Full size in pixels:', width=35, pady=5, bg="#C9ECEC")
l2.grid(row=1, column=0)

e2 = Entry(frame2, width=10, borderwidth=3)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame2, text='Enter Measured Object size on the Image in pixels:', width=35, pady=5, bg="#C9ECEC")
l3.grid(row=2, column=0)

e3 = Entry(frame2, width=10, borderwidth=3)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

c1 = Button(frame2, text="CALCULATE >> RESULT (mm):", width=36, pady=6, fg="blue", command=calculator1)
c1.grid(row=3, column=0)

r1 = Entry(frame2, width=10, borderwidth=3)
r1.grid(row=3, column=1)

# Calculator_2

frame3 = LabelFrame(root, text="< CALCULATOR - 2 >", bg="#FFDC85")
frame3.pack(padx=5, pady=5)


def calculator2():
    call2 = ((int(e4.get()) / 1000) * ((float(e6.get()) / 1000) + (int(e5.get()))) / (float(e6.get()) / 1000)) / 1000
    print(round(call2, 4))


frame4 = LabelFrame(frame3, text="< DISTANCE TO OBJECT >", fg="maroon", bg="#C9ECEC")
frame4.pack(padx=20, pady=15)

b4 = Label(frame4, text='Enter the Lens Focal Length in mm:', width=35, pady=5, bg="#C9ECEC")
b4.grid(row=0, column=0)

e4 = Entry(frame4, width=10, borderwidth=3)
e4.get()
e4.insert(0, '')
e4.grid(row=0, column=1)

b5 = Label(frame4, text='Enter True size of the Object in meter:', width=35, pady=5, bg="#C9ECEC")
b5.grid(row=1, column=0)

e5 = Entry(frame4, width=10, borderwidth=3)
e5.get()
e5.insert(0, '')
e5.grid(row=1, column=1)

b6 = Label(frame4, text='Enter Object size on the Camera Matrix in mm:', width=35, pady=5, bg="#C9ECEC")
b6.grid(row=2, column=0)

e6 = Entry(frame4, width=10, borderwidth=3)
e6.get()
e6.insert(0, '')
e6.grid(row=2, column=1)

c2 = Button(frame4, text="CALCULATE >> RESULT (km):", width=36, pady=5, fg="blue", command=calculator2)
c2.grid(row=3, column=0)

r2 = Entry(frame4, width=10, borderwidth=3)
r2.grid(row=3, column=1)


root.mainloop()
