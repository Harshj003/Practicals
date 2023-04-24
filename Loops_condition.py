#if else
#Program 1
marks=[] sum1=0

for i in range(0,5):
marks.append(int(input("Enter marks of subject :  "))) 
sum1 = sum1 + marks[i]
print(“Sum of marks is”,sum1)

per = sum1/5 
print(“Percentage is “, per)
if per>90:
print(" A")
elif per>70: 
       print(" B") 
elif per>50: 
       print(" C") 
elif per>30: 
       print(" D")
else:
print(" Fail")

#program 2
num = input("Enter numbers : ").split() even=odd=0

for i in num:
if int(i)%2 == 0: even+=1
else:
odd+=1

print('Number of even numbers is ',even) print('Number of odd numbers is ',odd)

#program 3
temp = input('Enter Temp : ')

degree = int(temp[:-1]) typ = temp[-1]

if typ.upper()=='C':
temp1 = round(degree*9/5)+32 result='F'
elif typ.upper()=='F':
temp1 = round((degree-32)/9*5) result='C'
else:
print('Invalid input.') quit()

print('Converted temp is ',temp1,result)

#Loop
#program 1
num = int(input("Enter a number : "))


for i in range(1,11): print(num,'*',i,'=',num*i)

#program 2
for i in range(1,6): 
for j in range(1,6):
if i>=j:
print('0', end = ' ' ) print('\n')

#program 3
for i in range(0,50):
if i%3 == i%5 == 0: print('APSIT-IT')
elif i%5 == 0: print('IT')
elif i%3 == 0: print('APSIT-')
else:
print(i)
