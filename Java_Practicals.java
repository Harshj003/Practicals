// Reading input by creating an object of scanner class
import java.util.Scanner;
class Student
{
public static void main(String args[])
{
Scanner s1 = new Scanner(System.in);
System.out.println("Enter an Integer: ");
int a;
a = s1.nextInt();
System.out.println("The entered integer is "+a);
}
}

// Use of system.out.println
import java.util.Scanner;
class Test
Department of Information Technology | APSIT
{
public static void main(String args[])
{
Scanner sc = new Scanner(System.in);
System.out.println("Enter your ID: ");
int roll = sc.nextInt();
System.out.println("Enter your name: ");
String name = sc.next();
System.out.println("Enter your fee: ");
double fee = sc.nextDouble();
System.out.println("Roll No.: "+roll+"Name: "+name+"Fee:"+fee);
sc.close();
}
}

// Experiment 1
import java.util.*;
public class Employee
{
public static void main(String args[])
{
Scanner obj = new Scanner(System.in);
String id;
String ename;
double bsal;
System.out.println("Enter Employee ID: ");
id = obj.next();
System.out.println("Enter Employee Name: ");
ename = obj.next();
System.out.println("Enter Employee Basic Salary: ");
Department of Information Technology | APSIT
bsal = obj.nextDouble();
double HRA = (10*bsal)/100;
double DA = (73*bsal)/100;
double GS = bsal + DA + HRA;
double incometax = (30*GS)/100;
double NET = GS - incometax;
System.out.println("employee Id :"+id+"\n"+"Employee name : "+ename+"\n"+"Employee
DA= "+DA+"\n"+"Employee HRA="+HRA+"\n"+"Employee Gross Salary ="+GS+"\n"+"Employee Net Salary ="+NET);
}
}
