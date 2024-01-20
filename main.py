def main():
    book = "books/frankenstein"
    read = book_text(book)
    print(read)


def book_text(path):
    with open(path) as f:
        return f.read()


main()