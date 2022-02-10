from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, lista):
        self.lista = lista
        self.index = 0

    def __next__(self):
        if self.index == len(self.lista):
            raise StopIteration
        else:
            elemento = self.lista[self.index]
            self.index += 1
            return elemento
