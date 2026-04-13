book_details = ["harry potter", "lord of the rings", "harry potter", "lord of the rings", "the lean startup", "the great gatsby"]

sorted_books = sorted(book_details, key=len, reverse=True)
print(sorted_books)