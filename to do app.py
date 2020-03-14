from tkinter import *
 

class Main:
 	def __init__(self):
 		self.root = Tk()
 		self.root.geometry("500x450")
 		self.addPic = PhotoImage(file = "add.png")
 		self.addEntry = Entry(self.root,font = ("consolas",21))
 		self.addEntry.place(x = 60,y = 43)
 		self.addButton = Button(self.root,image = self.addPic,bd = 0)
 		self.addButton.place(x = 390,y = 40)
 		self.toDoListBox = Listbox(self.root,width = 37,height = 13,font = ("consolas",15))
 		self.toDoListBox.place(x = 60, y = 100)


 		self.root.mainloop()

Main()