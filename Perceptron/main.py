from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tabla import *
from perceptron import * 
import matplotlib.pyplot as plt
    
def cambiar():
    t2.lista = []
    t2.listar()
    if rbValue.get() == 0:
        t1.lista = [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]]
    else:
        t1.lista = [[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,-1]]
    lblPeso1.config(text = "Peso 1")
    lblPeso2.config(text = "Peso 2")
    lblUmbral.config(text = "Umbral")
    t1.listar()

def entrenar():
    plt.close()
    i = 0
    n = Neurona(0.5)
    while i < 4:
        y = n.entradas(t1.lista[i])
        for j in range(3):
            e = Entry(root, width=5, font=('Arial',12,'bold'), justify=CENTER)
            e.grid(row = 3 + i, column = 6 + j)
            if j != 3:
                e.insert(END,t1.lista[i][j])
            else:
                e.insert(END,y)
            e.configure(state='disabled')

        if y != t1.lista[i][2]:
            n.actualizar(t1.lista[i])
            i = 0
        else:
            i = i + 1  
        lblPeso1.config(text = "Peso 1 : "+ str(n.w1))
        lblPeso2.config(text = "Peso 2 : "+ str(n.w2))
        lblUmbral.config(text = "Umbral : "+ str(n.u))

    if len(n.W1) > 2:
        tiempo = [i for i in range(len(n.W1))]
        plt.plot(tiempo, n.W1)
        plt.plot(tiempo, n.W2)
        plt.plot(tiempo, n.U)
        plt.legend(['W1',"W2","U"])
        plt.show()    

    
root = Tk()
root.title('Perceptron Simple')

lblTitle = Label(root, text = "Perceptron de simple")
lblTitle.grid(column = 0,  columnspan = 12, row = 0)
lblTitle.config(font=("Comic Sans MS",20))

lblTitle = Label(root, text = "Compuertas:", height = 3)
lblTitle.grid(column = 1, columnspan = 3, row = 1)
lblTitle.config(font=("Verdana",12))

t1 = Tabla(root,3,1,[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]])
t1.listar()

rbValue = IntVar()
rbOperator1 = Radiobutton(root, text = "AND", variable = rbValue, value = 0, indicatoron = 0, width=5, command = cambiar)
rbOperator1.grid(column = 4, row = 1)
rbOperator1.config(font=("Verdana",12))
rbOperator2 = Radiobutton(root, text = "OR", variable = rbValue, value = 1, indicatoron = 0, width=5, command = cambiar)
rbOperator2.grid(column = 5, row = 1)
rbOperator2.config(font=("Verdana",12))

lblTitle = Label(root, text = "Salida esperada")
lblTitle.grid(column = 1, columnspan = 3, row = 2)
lblTitle.config(font=("Verdana",12))

lblTitle = Label(root, text = "Salida Obtenido")
lblTitle.grid(column = 6, columnspan = 3, row = 2)
lblTitle.config(font=("Verdana",12))

t2 = Tabla(root,3,6)
t2.listar()

btnSubmit = Button(root, text = "Entrenar", command = entrenar)
btnSubmit.grid(column = 4, columnspan = 2, row = 3, )
btnSubmit.config(font=("Verdana",12))

lblPeso1 = Label(root, text = "Peso 1",width = 40)
lblPeso1.grid(column = 4, columnspan = 2, row = 4)
lblPeso1.config(font=("Verdana",12))

lblPeso2 = Label(root, text = "Peso 2")
lblPeso2.grid(column = 4, columnspan = 2, row = 5)
lblPeso2.config(font=("Verdana",12))

lblUmbral = Label(root, text = "Umbral")
lblUmbral.grid(column = 4, columnspan = 2, row = 6)
lblUmbral.config(font=("Verdana",12))

my_img = PhotoImage(file = "perceptron.png")
image1 = Label(image = my_img)
image1.grid(column = 1, columnspan = 8, row = 7)

root.mainloop()