from tkinter import *

class Tabla: 

    def __init__(self,root, x , y, lista = []):
        self.x = x
        self.y = y
        self.root = root  
        self.lista = lista    

    def listar(self):
        for i in range(4):
            for j in range(3):
                e = Entry(self.root, width=5, fg='blue', font=('Arial',12,'bold'), justify=CENTER)
                e.grid(row = self.x + i, column = self.y + j)
                if len(self.lista) >= 4: 
                    e.insert(END, self.lista[i][j])
                e.configure(state='disabled')

    

    



    