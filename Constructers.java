// Program for default constructer
class student
{
int id;
String name;
boolean b;
void display()
{
System.out.println(id+" "+name+" "+b);
}
public static void main(String args[])
{
student s1 = new student();
student s2 = new student();
student s3 = new student();
s1.display();
s2.display();
s3.display();
}
}

// Program for using parameterized constructer
class Stud
{
int id;
String name;
Stud(int i,String n)
{
id = i;
name = n;
}
void display()
{
System.out.println(id+" "+name);
}
public static void main(String args[])
{
Stud s1 = new Stud(111,"Kashish");
Stud s2 = new Stud(222,"Tanvi");
s1.display();
Department of Information Technology | APSIT
s2.display();
}
}

// Program for constructer chaining
class emp
{
public String empName;
public int empSalary;
public String address;
public emp()
{
this("Kashish");
}
public emp(String name)
{
this(name,120035);
}
public emp(String name, int sal)
{
this(name,sal,"Thane");
}
public emp(String name,int sal,String addr)
Department of Information Technology | APSIT
{
this.empName=name;
this.empSalary=sal;
this.address=addr;
}
void disp()
{
System.out.println("Employee Name: "+empName);
System.out.println("Employee Salary: "+empSalary);
System.out.println("Employee Address: "+address);
}
public static void main(String args[])
{
emp obj = new emp();
obj.disp();
}
}
