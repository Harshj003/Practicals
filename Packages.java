// program to create package
package letmecalculate;
public class Calculator
{
public int add(int a,int b)
{
return a+b;
}
public static void main(String args[])
{
Calculator obj = new Calculator();
System.out.println(obj.add(10,20));
}
}

// program to use above created package
import letmecalculate.Calculator;
public class Demo1
{
public static void main(String args[])
{
Calculator obj = new Calculator();
System.out.println(obj.add(100,200));
}
}
