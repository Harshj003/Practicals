class Person:
  def adhaar(self): 
    n=int(input("Adhaar no. : ")) 
    print("Adhaar no. = ",n)

class Student(Person): 
  def moodleId(self):
    n=int(input("Moodle ID : "))
    print("Moodle ID = ",n)

class Employee(Person): 
  def empId(self):
    n=int(input("Employee ID : ")) 
    print("Employee ID = ",n)

class Researcher(Student,Employee): 
  def restopic(self):
    n=input("Research Topic : ") 
    print("Research Topic = ",n)

r=Researcher() 
r.restopic() 
r.empId() 
r.moodleId() 
r.adhaar()

e=Employee() 
e.empId() 
e.adhaar()
 
s=Student() 
s.moodleId() 
s.adhaar()
