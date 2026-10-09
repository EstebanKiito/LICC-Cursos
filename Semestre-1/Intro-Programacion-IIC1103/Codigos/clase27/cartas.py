import random
class Carta:
    def __init__(self, num, s):
        self.num = num
        self.pinta = s

    def diferencia(self, other):
        return abs(self.num-other.num)

    def cambiar_pinta(self, nueva_pinta):
        if nueva_pinta in 'DTPC':
            self.pinta = nueva_pinta
            return True
        return False

    def __str__(self):
        t = ''
        if self.num == 13:
            t+='K'
        elif self.num == 12:
            t+='Q'
        elif self.num == 11:
            t+='J'
        elif self.num == 1:
            t+='A'
        else:
            t+=str(self.num)
        t+=self.pinta
        return t

class Mazo:
    def __init__(self):
        self.cartas = []
        for pinta in 'CDTP':
            for numero in range(1,14):
                carta = Carta(numero, pinta)
                self.cartas.append(carta)

    def quedan_cartas(self):
        if len(self.cartas)>0:
            return True
        else:
            return False
    def sacar(self):
        pos = random.randint(0,len(self.cartas)-1)
        c = self.cartas.pop(pos)
        return c





m = Mazo()
while m.quedan_cartas(): #True o False, según si quedan cartas en el mazo
    carta = m.sacar() #retorna Carta al azar del mazo
    print(carta,end=' ')
