#Python program that implements a half adder circuit:
def half_adder(a, b):
sum = a ^ b
carry = a &amp; b
return sum, carry
# Main program
# Input bits
a = 1
b = 1
# Call the half_adder function
sum, carry = half_adder(a, b)
# Print the results
print(&quot;Half Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)

USER DEFINED
# Half Adder Circuit
def half_adder(a, b):
sum = a ^ b
carry = a &amp; b
return sum, carry
# Get input bits from user
a = int(input(&quot;Enter value for a (0 or 1): &quot;))
b = int(input(&quot;Enter value for b (0 or 1): &quot;))
# Call the half_adder function
sum, carry = half_adder(a, b)
# Print the results
print(&quot;Half Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)

FULL ADDER
Python program that implements a full adder circuit:

# Full Adder Circuit
def full_adder(a, b, c):
sum = a ^ b ^ c
carry = (a &amp; b) | (b &amp; c) | (c &amp; a)
return sum, carry
# Main program
# Input bits
a = 1
b = 1
c = 0
# Call the full_adder function
sum, carry = full_adder(a, b, c)
# Print the results
print(&quot;Full Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b, &quot;, c =&quot;, c)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)

USER DEFINED:
def full_adder(a, b, c):
sum = a ^ b ^ c
carry = (a &amp; b) | (b &amp; c) | (c &amp; a)
return sum, carry
# Get input bits from user
a = int(input(&quot;Enter value for a (0 or 1): &quot;))
b = int(input(&quot;Enter value for b (0 or 1): &quot;))
c = int(input(&quot;Enter value for c (0 or 1): &quot;))
# Call the full_adder function
sum, carry = full_adder(a, b, c)
# Print the results
print(&quot;Full Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b, &quot;, c =&quot;, c)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)

Combine full and half adder program
# Half Adder Circuit

def half_adder(a, b):
sum = a ^ b
carry = a &amp; b
return sum, carry

# Full Adder Circuit

def full_adder(a, b, c):
sum = a ^ b ^ c
carry = (a &amp; b) | (b &amp; c) | (c &amp; a)
return sum, carry

# Main program

# Half Adder Test
a = 1
b = 0
sum, carry = half_adder(a, b)
print(&quot;Half Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)

# Full Adder Test
a = 1
b = 1
c = 1
sum, carry = full_adder(a, b, c)
print(&quot;\nFull Adder:&quot;)
print(&quot;Input: a =&quot;, a, &quot;, b =&quot;, b, &quot;, c =&quot;, c)
print(&quot;Sum:&quot;, sum)
print(&quot;Carry:&quot;, carry)
