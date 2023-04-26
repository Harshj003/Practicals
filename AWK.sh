#print even numbers in range
#!/bin/bash
read -p "Number:" num
awk '{for(i=0;i<=$1;i++) if(i%2 == 0) print i}'<<<$num

#awk script to print fibonacci series
#!/bin/bash
echo "how many no"
read num
echo "num is $num"
awk 'BEGIN{
a = 0;
b = 1;
for(i=0;i<'${num}';i++)
  {
    print a;
    c = a+b;
    a = b;
    b = c;
  }
}'
