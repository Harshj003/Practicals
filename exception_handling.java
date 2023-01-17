// exception handling using try-catch block
class Division
{
public static void main(String args[])
{
int num1,num2;
try
{
num1 = 0;
num2 = 62/num1;
System.out.println(num2);
System.out.println("Hey I'm at the end of try block");
}
catch(ArithmeticException e)
{
System.out.println("You should not divide any number by zero");
}
System.out.println("I'm out of try catch block in java.");
}
}

// use of multiple catch blocks
class Example2
{
public static void main(String args[])
{
try
{
int a[]=new int[7];
a[4]=30/0;
System.out.println("First print statement in try block");
}
catch(ArithmeticException e)
{
System.out.println("Warning: ArithmeticException");
}
catch(ArrayIndexOutOfBoundsException e)
{
System.out.println("Warning: ArrayIndexOutOfBoundsException");
}
catch(Exception e)
{
System.out.println("Warning: Some other exception");
}
System.out.println("Out of try-catch block...");
}
}

// use of throw keyword
public class ThrowExample
{
static void checkEligibility(int stuage, int stuweight)
{
if(stuage<12 && stuweight<40)
{
  throw new ArithmeticException("Student is not eligible for registration");
}
else
{
  System.out.println("Studenty Entry is valid!!");
}
}
public static void main(String args[])
{
System.out.println("Welcome to the Registration process!!!!");
checkEligibility(10,39);
System.out.println("Have a Nice Day..");
}
}

// use of finally keyword
class Finally
{
public static void main(String args[])
{
try
{
int num=121/0;
System.out.println(num);
}
catch(ArithmeticException e)
{
System.out.println("Number should not be divided by 0");
}
finally
{
System.out.println("This is finally block");
}
System.out.println("Out of try-catch-finally");
}
}

// use of finally keyword with return statement
class JavaFinally
{
public static void main(String args[])
{
System.out.println(JavaFinally.myMethod());
}
public static int myMethod()
{
try
{
return 112;
}
finally
{
System.out.println("This is finally block");
System.out.println("Finally block ran even after return statement");
}
}
}
