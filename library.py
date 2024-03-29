# library_management-sysytem

#Scope
#Library Class -----> Book availability  | Book issue          | add the book back
#Customer Class ---->                    | Requesting the book | Returning the book

### creating a class called library where giving the book to customer and return and add the book back to the library 
class library:
  def __init__(self,book):
    self.book_list = book
  def show(self):
    print(*self.book_list)
  def lend_book(self,books):
    if books in self.book_list:
      self.book_list.remove(books)
      print("book issued")
      return True
    else:
      print("book not available try with another book")
      return False
  def accept_book(self,books):
    self.book_list.append(books)
    print("Book recieved Thank you visit again")
    return True



###creating a class called customer where cutomer requesting book and returning a book
class customer:
  def __init__(self):
    self.bookList=[]
  def add_book(self,books):
    self.bookList.append(books)
  def show(self):
     print(*self.bookList)
  def request_book(self):
    print("Enter a book")
    print("-----------------------------------")
    self.book = input()
    return self.book
  def returning_book(self):
    print("Enter a book")
    print("-----------------------------------")
    self.book= input()
    return self.book
  def returning_book_lib(self,books):
    if books in self.bookList:
      self.bookList.remove(books)
      print("book removed from customer and added to the library")
      return True
    else:
      print("Please enter the correct book which you have taken")
      return False
      
### creating an object for library and customer
lib_cbe = library(['book1','book5','book3','book2','book5'])
naren = customer()

###cheking with condition 
while True:
  print("--------------------------------------------------------------------------")
  print("select the choice below")
  print("1-Book Availability\n2-lend a book\n3-Customer borrowed book\n4-returning the book\n5-exit")
  print("---------------------------------------------------------------------------")
  choice = int(input("Enter your choice : "))
  if choice==1:
    lib_cbe.show()
  elif choice==2:
    requested_book=naren.request_book()
    status = lib_cbe.lend_book(requested_book)
    if status==True:
      naren.add_book(requested_book)
  elif choice==3:
    naren.show()
  elif choice==4:
    requested_book = naren.returning_book()
    status = naren.returning_book_lib(requested_book)
    if status==True:
        lib_cbe.accept_book(requested_book)
  elif choice==5:
    break
