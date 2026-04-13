book_details = ["harry potter", "lord of the rings", "harry potter", "lord of the rings", "the lean startup", "the great gatsby"]

index_of_first_harry = book_details.index("harry potter")
print(index_of_first_harry)

book_details.pop(index_of_first_harry)

print(book_details)