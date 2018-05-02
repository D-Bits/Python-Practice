from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()
    def init_window(self):
        self.master.title("Mileage Calculator")
        
        self.milesLabel=Label(self.master, text="Enter the total miles")
        self.milesLabel.place(x=10, y=10)

        self.milesEntry=Entry(self.master)
        self.milesEntry.place(x=15, y=30)

        self.gasLabel=Label(self.master, text="Enter the total gas used")
        self.gasLabel.place(x=10, y=80)

        self.gasEntry=Entry(self.master)
        self.gasEntry.place(x=15, y=100)

        #Create the submit button
        self.submit=Button(self.master, text="Submit", command=self.calculate)
        self.submit.place(x=10, y=140)

        self.message=""
        self.resultLabel=Label(self.master, text=self.message)

    def calculate(self):
        miles=float(self.milesEntry.get())
        gallons=float(self.gasEntry.get())
        self.mpg= miles / gallons
        print("The total MPG is: ", self.mpg, " miles per gallon")
        

root=Tk()
root.geometry=("1600x1600")

app=Window(root)
root.mainloop()
