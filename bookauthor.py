class publisher:
    def __init__(self,pubname):
        self.pubname=pubname
    def display(self):
        print("publisher name is :",self.pubname)
class book(publisher):
    def __init__(self,pubname,title,author):
        publisher .__init__(self,pubname)
        self.title =title
        self.author = author
    def display(self):
        print("title:",self.title)
        print("author:", self.author)
class Python(book):
    def __init__ (self,pubname,title,author,price,no_of_pages):
        book. __init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Title:",self.title)
        print("Author:", self.author)
        print("Publisher:", self.pubname)
        print("Price:", self.price)
        print("No of pages:", self.no_of_pages)
b1= Python("hello","malik","india",600,900)
b1.display()



