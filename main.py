#creating a bmi calculator
#Simphiwe Sithole

from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

#defining the allowed kg bmi
def bmi_index(bmi):

    if bmi < 18.5:
        messagebox.showinfo('bmi-converter', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-converter', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-converter', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-converter', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('bmi-converter', 'something went wrong!')

ws = Tk()
ws.title('bmi-calculator')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(expand=True)

#Defining the allowed minimum and maximum allowed age

age_lb = Label(
    frame,
    text="Enter Age (2 - 100)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

#This is the gender button (Female or male)
gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)
#This is for the male button
male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

#This is the female button

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

#This is the height butoo
height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

#This is the weight (in kg) button
weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

#This is the calculate, that is activated and calcutes the bmi
cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

#This is the reset button, that will clear what's on the entry box
reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

#This is the exit button, that will allow the user to exit the app
exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
