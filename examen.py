class ColaEspecial: 
    def __init__ (self, cap=10):
        self.cap = cap
        self.cola = [None]*cap
        self.size = 0
        self.ind = -1
        self.dir = 1

        def insertar(self, item):
            if self.size < self.cap:
                self.ind = (self.ind + 1) % self.cap
                self.cola[self.ind] = item
                self.size += 1
            else:
                self.cola[self.indice] = item
                self.ind = (self.ind + self.dir) % self.cap
                if self.ind == 0 or self.ind == self.cap -1:
                    self.dir *= -1

        def show(self):
            return [x for x in self.cola if x is not None]     
        
        def main():
            cola=ColaEspecial()
            alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            print("Insertando letras del alfabeto en la cola:")
            for letra in alfabeto:
                cola.insertar(letra)
                print(f"Despues de insertar {letra}: {cola.mostrar()}")
        if _name_=="_main_":
            main()

               


    