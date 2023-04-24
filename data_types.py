#Program1:
print(" 	COMMENTS 	")
print('Single Line "#"')
print( 'Multi Line ("""---""")')
print( "Multi Line ('''---''')")


print( "")
 
print( "--Datatypes,Expressions,Output Statement & Conversions--") a = 16
a1 = "abc" b = 23.32
c = 2.3+3.2j d = 1.2-2.8j



e = c+d e1 = a*b

print('Type of e is',type(e)) print('Type of e1 is',type(e1))

print( "Sum is",e)
print( 'Multiplication is ', e1)


f = float(a)
print( 'Int to Float', f) g = complex(b)
print( 'Float to Complex', g) h = oct(a)
print( 'Decimal to Octal', h)
 
i = bin(a)
print( 'Decimal to Binary', i) j = hex(a)
print('Decimal to Hexadecimal',j) print("")



print( "------INPUT STATEMENT	")


k=input('What is your name? using raw input ') print( 'Your name is ' + k)

l=input('Enter value of x ') l=int(l)

print('Entered value of x using String Function is ' + str(l)) print('Entered value of x using format function is {0}'.format(l))

a = input('Enter number of Theory subjects : ') b = input('Enter number of Practical subjects : ')
print('In academic year 2018-19, there are {0} Theory and {1} Practical subjects'.format(a,b))


print("accept integer input",int(input()))
 
print("")


print( "-------Knowing the datatype	")
a=12
print(type(a)) b="str" print(type(b)) c=1.2+4j
print(type(c))

#Program 2
a = int(input('Enter value of a : ')) b = int(input('Enter value of b : ')) c = 0

c = a + b print(a,'+',b,'=',c)

c = a - b print(a,'-',b,'=',c)

c = a * b print(a,'*',b,'=',c)

c = a / b print(a,'/',b,'=',c)

c = a % b print(a,'%',b,'=',c)

a = int(input('\nEnter value of a : ')) b = int(input('Enter value of b : ')) c = a**b
 
print(a,'**',b,'=',c)


a = int(input('\nEnter value of a : ')) b = int(input('Enter value of b : ')) c = a//b
print(a,'//',b,'=',c)

#Program 3
print('------Discount Calculator	')


mrp = int(input('Enter MRP of product : ')) discount = int(input('Enter discount of product : '))

cost = mrp - (discount/100)*mrp


print('You have to pay ',cost)
