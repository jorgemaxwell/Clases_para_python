import math

class potencia:

    def __init__(self, x, n):

        self.x = x
        self.n = n

    def operacion (self):
        return math.pow(self.x, self.n)

if __name__ == "__main__":

    ejemplo1 = potencia(2,-3)
    print(ejemplo1.operacion())