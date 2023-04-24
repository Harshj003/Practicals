#program 1
print(('List').center(50,'-'))


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("\n Accessing list") print("\n list1[0]: ", list1[0])
print("\n list2[1:5]: ", list2[1:5])
print("\n list2[-2]",list2[-2])


list = ['physics', 'chemistry', 1997, 2000] print("\n updating list")
print("\n Value available at index 2 : ") print(list[2])
list[2] = 2001
print("\n New value available at index 2 : ") print(list[2])

list1 = ['physics', 'chemistry', 1997, 2000] print("\n Deleting list element") print(list1)
del list1[2]
 
print("\n After deleting value at index 2 : ") print(list1)

print("\n Basic List Operations") print("\n Length of List [1,2,3] is ") print(len([1, 2, 3]))
print("\n Concatenation of two lists") print([1, 2, 3] + [4, 5, 6])
print("\n Repetition of String") print(['Hello!'] * 4)
print("\n Membership ") print(3 in [1, 2, 3]) print("\n Iterations ") for x in [1, 2, 3]:
print(x)


print(('Tuple').center(50,'-'))


print("\nAccessing Tuple values")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
 

print("\nUpdating Tuple values") tup1 = (12, 34.56)
tup2 = ('abc', 'xyz') tup3 = tup1 + tup2; print(tup3)
print("\nDeleting tuple")
tup = ('physics', 'chemistry', 1997, 2000); print(tup)
del tup
print("After deleting tup : ") #print(tup)	Error

print("\n Basic Tuple Operations") print("legth of tuple (1,2,3):- ")
print(len((1, 2, 3)))
print("Concatenate two tuples (1,2,3) and (4,5,6):-")
print((1, 2, 3) + (4, 5, 6))
print("Repetation of tuple Hi") print(('Hi!',) * 4)
print("Membership of 3 in tuple (1,2,3)")
print(3 in (1, 2, 3))
print("Membership of 4 in tuple (1,2,3)")
 
print(4 in (1, 2, 3)) print("Iteration") for x in (1, 2, 3):
print(x)


L = ('spam', 'Spam', 'SPAM!')
print("L[-2]:-") print(L[-2])

print("\n Built-in Tuple Functions") print("\n Length of Tuple")
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc') print("First tuple length : ", len(tuple1)) print("Second tuple length : ", len(tuple2))

print("\n Maximum and Minimum element from Tuple") tuple1, tuple2 = ('z', 'xyz', 'zara', 'abc'), (456, 700, 200) print("Min value element : ", min(tuple1))
print("Min value element : ", min(tuple2)) print("Max value element : ", max(tuple1)) print("Max value element : ", max(tuple2))

print(('Dictionary').center(50,'-'))
 

print("\n Accessing Dictionary element")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


print("\n Updating Dictionary")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
dict['Age'] = 8
dict['School'] = "DPS School" print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])


print("\n Deleting from Dictionary")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} del dict['Name']
dict.clear() del dict

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} dict['School'] = "DPS School" print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
 

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict['Name']: ", dict['Name'])


dict = {'Name': 'Zara', 'Age': 7}
print("dict['Name']: ", dict['Name'])

#program 2
l = input('Enter elements of list : ') l = l.split()
print('List is : ',l)


for i in l:
if int(i)%2 == 0: l.remove(i)
print('New list : ',l)


l = tuple(input('Enter elements of tuple : ')) x = input('Enter element to search : ')
if x in l:
print('Element ',x,' is present') else:
print('Element ',x,' is not present')


d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {5:50,6:60}
result = {} result.update(d1) result.update(d2)
 
result.update(d3)


##result = {}
##for d in (d1,d2,d3):
##	result.update(d)


print(d1) print(d2) print(d3) print(result)
