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
