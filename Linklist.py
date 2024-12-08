class Link:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def getFirst(self):
        return self.head

    def add(self, data):
        """Añade un nuevo elemento al inicio de la lista."""
        new_link = Link(data, self.head)
        self.head = new_link

    def __iter__(self):
        """Define un iterador para la lista, como en lista 5-23."""
        next = self.getFirst()
        while next is not None:
            yield next.getData()
            next = next.getNext()

    def traverse(self, func=print):
        """Aplica una función a todos los elementos de la lista.
           De forma predeterminada, imprime cada elemento."""
        for data in self:
            func(data)

    def __len__(self):
        """Retorna la longitud de la lista."""
        return sum(1 for _ in self)

    def __str__(self):
        """Construye una representación en cadena de la lista."""
        result = "[" + " > ".join(str(data) for data in self) + "]"
        return result