#Arithmetic operation
#!/bin/bash
#Works as string
expr '10 + 30'
#Works as string
expr 10+30
expr 10+30
expr 30%9
myval1= expr 30 / 10
echo $myval1
myval2=$( expr 30 - 10)
echo $myval2

#simple interest
#!/bin/bash
echo " Enter the principle value: "
read p
echo " Enter the rate of interse: "
read r
echo " Enter the time period: "
read t
s= expr $p \* $t \* $r / 100
echo "The simple interest is "
echo $s

#Check wheter a leap year or not
#!/bin/bash
echo "LEAP YEAR SHELL SCRIPT"
echo -n "Enter a year: "
read year_checker
if [ expr $year_checker % 4 -eq 0]
then
  echo "$year_checker is a leap year"
else
  echo "$year_checker is not a leap year"
  fi
