# Write a Python program to implement a class named BookStore with the following specifications:
## The class should contain two instance variables:
#### Name(Book Name)
#### Author(Book Author)
## The class should contain one class variable:
#### NoOfBooks(initialize it to 0)
## Define a constructor(__init__) that accepts Name and Author and initializes instance variables
## Inside the constuctor, increment the class variable NoOfBook by 1 whenever a new object is created
## Implement an instance method:
#### Display() - should display book details in the format
###### <BookName> by <Author>. No of books: <NoOfBooks>

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("WIngs of Fire", "A.P.J. Abdul Kalam")
    obj2 = BookStore("Atomic Habits", "James Clear")

    obj1.Display() 
    obj2.Display() 

if __name__ == "__main__":
    main() 