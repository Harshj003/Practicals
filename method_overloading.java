// Method overloading with different number of parameters in argument list
class Overloading1
{
public void disp(char c)
{
System.out.println(c);
}
public void disp(char c,int num)
{
System.out.println(c+" "+num);
}
}
class Sample
{
public static void main(String args[])
{
Overloading1 obj = new Overloading1();
obj.disp('a');
obj.disp('a',10);
}
}

// Method overloading with difference in data type of parameters
class Overloading2
{
public void disp(char c)
{
System.out.println(c);
}
public void disp(int c)
{
System.out.println(c);
}
}
class Sample2
{
public static void main(String args[])
{
Overloading2 obj = new Overloading2();
obj.disp('a');
obj.disp(5);
}
}

// Overloading - sequence of data type of arguments
class Overloading3
{
public void disp(char c,int num)
{
System.out.println("I'm the first definition of method disp");
}
public void disp(int num,char c)
{
System.out.println("I'm the second definition of method disp");
}
}
class Sample3
{
public static void main(String args[])
{
Overloading3 obj = new Overloading3();
obj.disp('x',51);
obj.disp(52,'y');
}
}

// Method overloading with type promotion
class Demo
{
void disp(int a,double b)
{
System.out.println("Method A");
Department of Information Technology | APSIT
}
void disp(int a,double b,double c)
{
System.out.println("Method B");
}
public static void main(String args[])
{
Demo obj = new Demo();
obj.disp(100,20.67f);
}
}

// Constructer overloading
class Student5
{
int id;
String name;
int age;
Student5(int i,String n)
{
id = i;
name = n;
}
Student5(int i,String n,int a)
{
id = i;
name = n;
age = a;
}
Department of Information Technology | APSIT
void display()
{
System.out.println(id+" "+name+" "+age);
}
public static void main(String args[])
{
Student5 s1 = new Student5(111,"Kashish");
Student5 s2 = new Student5(222,"Sanskruti",25);
s1.display();
s2.display();
}
}
