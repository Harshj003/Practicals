// Program to demonstrate inheritance
class Teacher
{
String name;
String Qualification;
String Designation;
double Experience;
void DisplayInfo()
{
System.out.println("The Teacher information is: "+"\n"+"Name="+name+"\
n"+"Qualification="+Qualification+"\n"+"Designation="+Designation+"\n");
}
}
class AssistantProfessor extends Teacher
{
public AssistantProfessor(String n,String q,String d,double e)
{
name = n;
Qualification =
q;
Designation = d;
Experience = e;
}
Department of Information Technology | APSIT
}
class AssociateProfessor extends Teacher
{
public AssociateProfessor(String n,String q,String d,double e)
{
name = n;
Qualification =
q;
Designation = d;
Experience = e;
}
}
class Professor extends Teacher
{
public Professor(String n,String q,String d,double e)
{
name = n;
Qualification =
q;
Designation = d;
Experience = e;
}
}
public class TestInheritance
{
public static void main(String args[])
{
AssistantProfessor obj1 = new AssistantProfessor("Kashish","IT","Asst.
Professor",10.6);
AssociateProfessor obj2 = new AssociateProfessor("Tanvi","CO","Associate
Professor",20.6);
Professor obj3 = new Professor("Shreya","CSE","Professor",10.6);
obj3.DisplayInfo();
}
}
