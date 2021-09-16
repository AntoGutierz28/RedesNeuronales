import random as r

class Neurona:

    def __init__(self, factorAprendizaje):
        self.w1 = r.random()
        self.w2 = r.random()
        self.u = r.random()
        self.e = factorAprendizaje
        self.W1 = []
        self.W2 = []
        self.U = []
        self.W1.append(self.w1)
        self.W2.append(self.w2)
        self.U.append(self.u)

    def entradas(self, x):
        x1, x2 = x[0], x[1]
        Y = x1*self.w1 + x2*self.w2 - self.u
        return 1 if Y >= 0 else -1

    def actualizar(self, x):
        x1, x2, t = x[0], x[1], x[2]
        self.w1 = self.w1 + 2*t*x1*self.e
        self.w2 = self.w2 + 2*t*x2*self.e
        self.u = self.u + 2*t*self.e*(-1)
        self.W1.append(self.w1)
        self.W2.append(self.w2)
        self.U.append(self.u)
        print('Peso 1 :', self.w1, '- Peso 2 :',
              self.w2, ' - Umbral :', self.u)


