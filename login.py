from tkinter import *
root = Tk()
root.title('LOGIN')
root.geometry("500x300")

def getvals():
    print("Accepted")

#heading
Label(root, text="Ingrese sus datos", font="ar 15 bold").grid(row=0, column=3)

#field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment mood")

#Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#variable for storing data
namevalue =StringVar
phonevalue = StringVar
gendervalue = StringVar
emergency = StringVar
paymentmood = StringVar
checkvalue = IntVar

#creating enty fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergency)
paymentmoodentry = Entry(root, textvariable=paymentmood)

#Packing Fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
checkbtn.grid(row=6, column=3)

#Submit button
Button(text="Submit",command=getvals).grid(grow=8,column=3)

root.mainloop()
