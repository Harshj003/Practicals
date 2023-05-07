## MAIN
def booths_algorithm():
#Gets Multiplicand
multiplicand_dec = getInput(&quot;Mutiplicand&quot;)

#Gets Multiplier
multiplier_dec = getInput(&quot;Multiplier&quot;)

#Converts Multiplicand
multiplicand_bin = convertDec(multiplicand_dec)

#Converts Multiplier
multiplier_bin = convertDec(multiplier_dec)

#Perform Booth&#39;s algorithm
boothsTriumph(multiplicand_bin,multiplier_bin)
print(&quot;Decimal Result: &quot; + str(int(multiplier_dec)*int(multiplicand_dec)))

## Parent function for logical process
def boothsTriumph(mcand, plier):
#Create full product line for Booth&#39;s Algorithm
print(&quot;multipcand: &quot; + mcand + &quot; multiplier: &quot; + plier)
product = &quot;00000000&quot; + plier + &quot;0&quot;
print(&quot;Product: &quot; + product)
#Display product line to user
print(buildLine(0,mcand,product))
#Iterate through Booth&#39;s Algorithm
for i in range(1,9):
operation = product[len(product)-2:]
product = perform_operation(product,mcand,operation)
print(buildLine(i,mcand,product))
#Print out final value in binary and decimal
product = shift(product)
product = product[9:17]
print(&quot;Product: &quot; + product)

return

## Perform the necessary algorithmic operation
def perform_operation(product,mcand,operation):
if operation == &quot;00&quot;:
product = shift(product)
print(&quot;No Op&quot;)
return product
elif operation == &quot;01&quot;:
##Product = Product + mcand
temp = binAdd(product[0:8],mcand)
product = temp + product[8:]
product = shift(product)
print(&quot;Add&quot;)
return product
elif operation == &quot;10&quot;:
##Product = Product - mcand
product = subtraction(product,mcand)
product = shift(product)
print(&quot;Sub&quot;)
return product
elif operation == &quot;11&quot;:
product = shift(product)
print(&quot;No Op&quot;)
return product
else:
print(&quot;An error has occured when choosing operation: Exiting program&quot;)
return 0

## Performs Subtraction operation
def subtraction(product,mcand):
carry = 0
prime_product = product[:8]
final_product = &quot;&quot;
for i in range(len(prime_product)-1,-1,-1):
if (mcand[i] == &quot;0&quot; and prime_product[i] == &quot;0&quot;):

if (carry == 1):
final_product = &quot;1&quot; + final_product
else:
final_product = &quot;0&quot; + final_product
elif (mcand[i] == &quot;1&quot; and prime_product[i] == &quot;0&quot;):
if (carry == 1):
final_product = &quot;0&quot; + final_product
else:
final_product = &quot;1&quot; + final_product
carry = 1
elif (mcand[i] == &quot;0&quot; and prime_product[i] == &quot;1&quot;):
if (carry == 1):
final_product = &quot;0&quot; + final_product
carry = 0
else:
final_product = &quot;1&quot; + final_product
elif (mcand[i] == &quot;1&quot; and prime_product[i] == &quot;1&quot;):
if (carry == 1):
final_product = &quot;1&quot; + final_product
#Again, not sure if this is what really happens to carry
carry = 1
else:
final_product = &quot;0&quot; + final_product
else:
print(&quot;An error has occurred when subtracting: Exiting program&quot;)
return 0

return final_product + product[8:]

## Shifts in left
def shift(product):
product = &quot;0&quot;+product[:len(product)-1]
return product

##Adds the two binary strings
def binAdd(num, num2):
product = &quot;&quot;
carry = &quot;0&quot;
for i in range(len(num)-1,-1,-1):
if carry == &quot;0&quot;:
if num[i] == &quot;0&quot; and num2[i] == &quot;0&quot;:
product = &quot;0&quot; + product
elif num[i] == &quot;1&quot; and num2[i] == &quot;1&quot;: #case 1 and 1
product = &quot;0&quot; + product
carry = &quot;1&quot;
else:
product = &quot;1&quot; + product
elif carry == &quot;1&quot;:
if num[i] == &quot;0&quot; and num2[i] == &quot;0&quot;:
product = &quot;1&quot; + product
carry = &quot;0&quot;
elif num[i] == &quot;1&quot; and num2[i] == &quot;1&quot;: #case 1 and 1
product = &quot;1&quot; + product
carry = &quot;1&quot;
else:
product = &quot;0&quot; + product
carry = &quot;1&quot;
return product
## Shows step-by-step process
def buildLine(iteration, mcand, product):
line = &quot;Step: &quot; + str(iteration) + &quot; | Multiplicand: &quot; + mcand + &quot; | Product: &quot; \
+ product[0:8] + &quot; | &quot; + product[8:16] + &quot; | &quot; + product[16]
return line
## Formats numbers from decimal to binary
def convertDec(dec):
# If the value is negative, calls twos_complement
if int(dec)&lt;0:
bin = twos_complement(int(dec))
# Else simply converts to binary

else:
bin = &quot;{0:b}&quot;.format(int(dec))
# Iterates through and makes the binary value 8
for i in range(8-len(bin)):
bin = &quot;0&quot; + bin
return bin
## Gets input for for algorithm
def getInput(varName):
#Request input
boothIn = input(&#39;Please enter your &#39; + varName + &quot;: &quot;)
#Parse input
while int(boothIn)&gt;127 or int(boothIn)&lt;-128:
print(&quot;Absolute value too big, please try again&quot;)
boothIn = input(&#39;Please enter your &#39; + varName + &quot;: &quot;)
return boothIn
## Converts negative numbers
def twos_complement(dec):
#Convert to dec, adding 1, then removing negative
adjusted = abs(int(dec) + 1)
#Turns into binary number
binint = &quot;{0:b}&quot;.format(adjusted)
#Flip bits
flipped = flip(binint)
# Iterates through and makes the binary value 8
for i in range(8-len(flipped)):
flipped = &quot;1&quot; + flipped
return flipped
## Flips the bits into a string
def flip(string):
flipped_string = &quot;&quot;
for bit in string:
if bit == &quot;1&quot;:
flipped_string += &quot;0&quot;
else:
flipped_string += &quot;1&quot;
return flipped_string
## CALL MAIN

booths_algorithm()
