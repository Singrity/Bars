from library import Library, Book

if __name__ == "__main__":
    library = Library("Lib_1")
    for i in range(1_000_000):
        is_book_inserted = library.add_book(Book(f"test_title{i}", "test_author", 123))
        if not is_book_inserted:
            break
    print(len(library.get_books()))
