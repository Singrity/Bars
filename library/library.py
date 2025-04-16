class Library:
    
    def __init__(self, name, rooms_limit=10):
        self.name = name
        self.rooms = [Room(f"Room_{i}") for i in range(rooms_limit)]

    def add_book(self, book):
        room = self._get_available_room()
        if room:
            room.add_book(book)
        else:
            print(f"Library is full of books!")
            return False
        
    def get_books(self):
        res = []
        for room in self.rooms:
            for rack in room.racks:
                for shelf in rack.shelfs:
                    res += shelf.books

        return res
    

    def _get_available_room(self):
        for room in self.rooms:
            if room.available:
                return room
        

    def __repr__(self):
        return self.name



class Room:

    def __init__(self, name, racks_limit=10):
        self.racks = [Rack(f"Rack_{i}") for i in range(racks_limit)]
        self.name = name

        self.available = True
    
    def add_book(self, book):
        rack = self._get_available_rack()
        if rack:
            rack.add_book(book)
            self.available = self.racks[-1].available

    def _get_available_rack(self):
        for rack in self.racks:
            if rack.available:
                return rack

    def get_books(self):
        res = []
        for rack in self.racks:
            for shelf in rack.shelfs:
                res += shelf.books

        return res

    def __repr__(self):
        return self.name


class Rack:

    def __init__(self, name, shelfs_limit=10):
        self.shelfs = [Shelf(f"Shelf_{i}") for i in range(shelfs_limit)]
        self.name = name
        self.available = True

    def add_book(self, book):
        shelf = self._get_available_shelf()
        if shelf:
            shelf.add_book(book)
            self.available = self.shelfs[-1].available

    def _get_available_shelf(self):
        for shelf in self.shelfs:
            if shelf.available:
                return shelf

    def get_books(self):
        res = []
        for shelf in self.shelfs:
            res += shelf.books

        return res


    def __repr__(self):
        return self.name


class Shelf:

    def __init__(self, name, books_limit=10):
        self.books = []
        self.name = name
        self.books_limit = books_limit
        self.available = True
    
    def add_book(self, book):
        if len(self.books) < self.books_limit:
            self.books.append(book)
            if len(self.books) >= self.books_limit:
                self.available = False
        else:
    
            self.available = False


    def __repr__(self):
        return self.name


class Book:

    def __init__(self, title, autor, book_id):
        self.title = title
        self.autor = autor
        self.id = book_id

    def __repr__(self):
        return self.title



