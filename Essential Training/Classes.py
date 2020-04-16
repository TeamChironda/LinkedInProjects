class Employee:
  raise_amount=1.5 # this variable can be  accessed through the class or the instance
  def __init__(self, first, last, age, pay):
       self.name=first
       self.surname=last
       self.eta=age
       self.paid=pay
       self.myemail= first +'.'+last+'@company.com'
  def printNames(self):
      print('Emp1: {}{}{}'.format(self.name, self.surname, self.eta))

  def apply_raise(self):
      self.paid=int(self.paid*Employee.raise_amount) #  the variable raise amount can be accesses through the class or the self istance

  @classmethod
  def set_raise_amt(cls, amount):
      cls.raise_amount=amount # this will update all the employee amount since it is a method from a class
###################################################################################################################################################################################
emp1=Employee('Zacarias Vasco', ' Chironda', 25, 2500)
emp2=Employee('Carlos Vasco', ' Chironda', 20, 800 )
###################################################################################################################################################################################
Employee.set_raise_amt(0.55)

#print( emp1.__dict__) # emp instance does not contain the
#print(Employee.__dict__)# see what the class contains
#print(emp1.paid)
#emp1.apply_raise()
#print(emp1.paid)
#print(emp1.printNames(), emp2 .printNames())






