class Library:

    def __init__(self):
        self.booklist = []
        self.issuedBook = []
        self.bookdict = {}

    def addBook(self):
        book = input("Enter the Name of the Book :")
        book.capitalize()
        if book not in self.booklist:
            self.booklist.append(book)
            self.bookdict[book] = 1
        else:
            self.bookdict[book] += 1
            if book in self.issuedBook:
                self.issuedBook.remove(book)
        print("Book Added Sccessfully")
    
    def issueBook(self):
        book = input("Enter the name of the Book :")
        book.capitalize()
        if book not in self.bookdict:
            print("Don't have any book like this add first!!!")
        else:
            if self.bookdict[book] >= 1:
                self.bookdict[book] -= 1
                self.issuedBook.append(book)
                print("Book Issued Sccessfully!!")
            else:
                print(f"{book} is not availabel") 

    def showAllBooks(self):
        print("Total books in library:",self.booklist)
        print("Issed Books:",self.issuedBook)

obj = Library()

i = 1
while(i):
    print("\n What do You want to perform \n 1.Add Book \n 2.Issue Book \n 3.Show All Books \n (0) Exit")
    ch = input("Enter Your Choice:")
    if(ch=='1'):
        obj.addBook()
    elif(ch=='2'):
        obj.issueBook()
    elif(ch=='3'):
        obj.showAllBooks()
    elif(ch=='0'):
        break
    else:
        print("Invalid Input")

