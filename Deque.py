class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None  # Nodo inicial de la deque
        self.tail = None  # Nodo final de la deque

    def isEmpty(self):
        """Retorna True si la deque está vacía, False en caso contrario."""
        return self.head is None

    def insertLeft(self, data):
        """Inserta un elemento al inicio de la deque."""
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertRight(self, data):
        """Inserta un elemento al final de la deque."""
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def removeLeft(self):
        """Elimina y retorna el elemento al inicio de la deque."""
        if self.isEmpty():
            raise IndexError("removeLeft from empty deque")
        data = self.head.data
        if self.head == self.tail:  # Si solo hay un elemento
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def removeRight(self):
        """Elimina y retorna el elemento al final de la deque."""
        if self.isEmpty():
            raise IndexError("removeRight from empty deque")
        data = self.tail.data
        if self.head == self.tail:  # Si solo hay un elemento
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def peekLeft(self):
        """Retorna el elemento al inicio de la deque sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("peekLeft from empty deque")
        return self.head.data

    def peekRight(self):
        """Retorna el elemento al final de la deque sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("peekRight from empty deque")
        return self.tail.data