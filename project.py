class Person:
  def __init__(self, id, full_name,age,id_on):
    self.id = id
    self.full_name = full_name
    self.age=age
    self.id_on=id_on
####################
class Client(Person):
    def __init__(self,id,full_name,age,id_on, phone_number):
        super().__init__( id, full_name,age,id_on)
        self.phone_number = phone_number

    def print(self):
        print("id=>",self.id," full_nume=>", self.full_name," age=>", self.age," id_on=>", self.id_on," phone_number=>",self.phone_number)
####################
class Librarian(Person):
    def __init__(self, id, full_name, age, id_on,emplyment_type):
        super().__init__(id, full_name, age, id_on)
        self.emplyment_type = emplyment_type

    def print(self):
        print("id=>",self.id," full_nume=>", self.full_name," age=>", self.age," id_on=>", self.id_on," emplyment_type=>",self.emplyment_type)

####################
class Book:
  def __init__(self, id, title,description,author,status):
    self.id = id
    self.title = title
    self.description=description
    self.author=author
    self.status =status


  def reservation(self):
      if self.status=="Activ":
          self.status="InActiv"
          print("succeeded")
      else:
          print("not succeeded")

  def cancl_reservation(self):
      if self.status == "InActiv":
          self.status = "Activ"
          print("succeeded")
      else:
          print("not succeeded")

  def print(self):
        print("id=>",self.id," title=>", self.title, " description=>",self.description," author=>", self.author," status"," status=>", self.status)
####################

c=Client("101","Ayoub",20,999,59233)

l=Librarian(102,"diaa",21,888,"Full")


my_objects = []
my_objects.append(Book("103","Python","hhgfh bv","DiaaSamy","Activ"))
my_objects.append(Book("104","java","blabla","DiaaSamy","Activ"))
my_objects.append(Book("105","dart","cont","DiaaSamy","InActiv"))

a=0
aa=0
print("________________________________________________")
print("1-List of clintes:")
c.print()
print("________________________________________________")
print("2-List of librarians:")
l.print()
print("________________________________________________")
print("3-List of Books:")
for obj in my_objects:
    obj.print()
print("________________________________________________")
print("4-total_borrowed_books:")
for obj in my_objects:
   if obj.status == "InActiv":
       a += 1
   else:
       aa+=1

print(a,"inavailable books")
a=0
print("________________________________________________")
print("5-total_available_books:")
print(aa, "available books")
aa=0
print("________________________________________________")
print("Welcome to the library")
print("1-borrow book now")
print("2-Cancel a book reservation now")
print("*-exit")
op=input()
while op=="1"or op=="2" :
    if op == "1":
        print("Enter the book id:")
        book_id = input()

        for obj in my_objects:
            if obj.id == book_id:
                if obj.status == "Activ":
                    print("Enter your ID")
                    id = input()
                    if c.id == id:
                        obj.reservation()
                        obj.print()

                else:
                    print("book is booked")
                f = True
                break
            else:
                f = False

        if f == False:
            print("not find")

    elif op == "2":
        print("Enter the book id:")
        book_id = input()
        for obj in my_objects:
            if obj.id == book_id:
                if obj.status == "InActiv":
                    print("Enter your ID")
                    id = input()
                    if c.id == id:
                        obj.cancl_reservation()
                        obj.print()



    else:
        exit()
    print("________________________________________________")
    print("1-List of clintes:")
    c.print()
    print("________________________________________________")
    print("2-List of librarians:")
    l.print()
    print("________________________________________________")
    print("3-List of Books:")
    for obj in my_objects:
        obj.print()
    print("________________________________________________")
    print("4-total_borrowed_books:")
    for obj in my_objects:
        if obj.status == "InActiv":
            a += 1
        else:
            aa += 1

    print(a, "inavailable books")
    a = 0
    print("________________________________________________")
    print("5-total_available_books:")
    print(aa, "available books")
    aa = 0
    print("________________________________________________")
    print("1-borrow book now")
    print("2-Cancel a book reservation now")
    print("*-exit")
    op=input()









