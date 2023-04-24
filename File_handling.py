#Studentpickle.py
class student:
	def __init__(self,roll,name,age):
		self.roll=roll
		self.name=name
		self.age=age
	def display(self):
		print(self.roll,self.name,self.age)

#Experiment9.py

import pickle,studentpickle

print("******CREATING PICKLE******")
f=open("studentpickle.dat","wb")
n=int(input("How many students??"))
for i in range(n):
	roll=int(input("Enter your roll no:"))
	name=input("Enter your name:")
	age=int(input("Enter your age:"))
	s=studentpickle.student(roll,name,age)
	pickle.dump(s,f)
f.close()
print("******LOADING PICKLE*******")
f=open('studentpickle.dat','rb')
for i in range(n):
	
s1=pickle.load(f)
	print("Roll no:",s1.roll)
	print("Name:",s1.name)
	print("Age:",s1.age)
f.close()
