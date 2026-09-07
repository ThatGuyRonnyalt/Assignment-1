class Book:
    def __init__(self, title, author, price):
        # Constructor: sets up the attributes when a book is created
        self.title = title
        self.author = author
        self.price = price
    
    def display_details(self):
        # Method to print the book info nicely
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print("-" * 20)

# Instantiate two book objects
book1 = Book("Python Programming", "John Mudododo", 29.99)
book2 = Book("Data Structures", "Jane Mufarinya", 34.50)

print("Book Details:")
book1.display_details()
book2.display_details()