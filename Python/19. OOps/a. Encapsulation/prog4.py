class LibraryBook:
    def __init__(self):
        self.title = "ABC"
        self._author = "Vishal"
        self.__stock = 99

    def add_stock(self, amt):
        self.__stock += amt 

    def get_stock(self):
        return self.__stock
    
l1 = LibraryBook()
print(l1.title)
print(l1.get_stock())
l1.add_stock(10)
print(l1.get_stock())