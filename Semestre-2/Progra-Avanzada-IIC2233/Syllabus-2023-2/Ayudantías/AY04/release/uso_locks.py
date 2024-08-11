import threading


class Deposito: 
    def __init__(self):
        self.oro = 0

        
def añadir_oro(Deposito, cantidad):
    for _ in range(cantidad):   ### Propuesto: cambiar este valor a 10**2. ¿Se comporta igual?
        Deposito.oro += int(1) # Este int() redundante es solo para que el ejemplo funcione


class Trabajador(threading.Thread):
    def __init__(self, deposito, cantidad):
        super().__init__()
        self.deposito = deposito
        self.cantidad = cantidad

    def run(self):
        añadir_oro(self.deposito, self.cantidad)
deposito = Deposito()
t1 = Trabajador(deposito, 10**6)
t2 = Trabajador(deposito, 10**6)

t1.start()
t2.start()
t1.join()
t2.join()

print("se añadió", deposito.oro, "al deposito")