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
        print(self.id, self.full_name, self.age, self.id_on,self.phone_number)
####################
class Librarian(Person):
    def __init__(self, id, full_name, age, id_on,emplyment_type):
        super().__init__(id, full_name, age, id_on)
        self.emplyment_type = emplyment_type

    def print(self):
        print(self.id, self.full_name, self.age, self.id_on, self.emplyment_type)

####################
class Book:
  def __init__(self, id, title,description,author):
    self.id = id
    self.title = title
    self.description=description
    self.author=author
    self.status ="Activ"


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
        print(self.id, self.title, self.description, self.author, self.status)
####################
class Borrowing_Order:
  def __init__(self, id, date,client_id,book_id,status):
    self.id = id
    self.date = date
    self.client_id=client_id
    self.book_id=book_id
    self.status =status
####################
c=Client(101,"Ayoub",20,999,59233)

l=Librarian(102,"diaa",21,888,"Full")

b=Book(103,"Python","hhgfh bv","DiaaSamy")
b2=Book(104,"java","blabla","DiaaSamy")
b3=Book(105,"dart","cont","DiaaSamy")

my_objects = []
my_objects.append(Book(103,"Python","hhgfh bv","DiaaSamy"))
my_objects.append(Book(104,"java","blabla","DiaaSamy"))
my_objects.append(Book(105,"dart","cont","DiaaSamy"))

a=0
print("1-List of clintes\n2-List of librarians\n3-List of Books\n4-List of borrowed_orders\n5-total_borrowed_books\n6-total_available_books\n7-total_borrowed_orders\n8-Exit")
op=input()
if op=="1":
    c.print()
elif op=="2":
    l.print()
elif op=="3":
    for obj in my_objects:
        obj.print()
elif op=="4":
   print()
elif op=="5":
    print()
elif op=="6":
    for obj in my_objects:
        obj.status=="Activ"
        a+=1
    print(a ,"available books")


elif op=="7":
    print()
else :
    exit











# b.print()
# b.reservation()
# b.print()
# b.cancl_reservation()
# b.print()




