library = []
user_book_one =  input("Enter the name of a book you own:")
user_book2_maybe =  input("Enter the name of another book you own (or press'Enter' to skip): ")
library = user_book2_maybe + user_book_one
print(f"Your Library: {library}")