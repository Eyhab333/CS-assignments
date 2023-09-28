library = []
wishlist = []

user_book_one =  input("Enter the name of a book you own: ")
user_book2_maybe =  input("Enter the name of another book you own (or press'Enter' to skip): ")
library.append(user_book_one)
if user_book2_maybe:
  library.append(user_book2_maybe)
print(f"Your Library: {library}")

wish_book_one = input("Enter the name of a book you wish ti have in the future: ")
wish_book_two = input("Enter the name of another book you wish to have (or press'Enter' to skip): ")
wishlist.append(wish_book_one)
if wish_book_two:
  wishlist.append(wish_book_two)
print(f"your wishlist: {wishlist}")

# Enter the name of a book from your wishlist that you've acquired  (or press'Enter' to skip):
acquired_book = input("Enter the name of a book from your wishlist that you've acquired  (or press'Enter' to skip): ")

# Updated Library: 
# Updated Wishlist:

# Enter the name of a book from your library you wish to donate (or press'Enter' to skip): 
input("Enter the name of a book from your library you wish to donate (or press'Enter' to skip):")
# Final Library after Donations: 