// program to add 2 integer nos using interface
import java.util.*;
interface I1
{
public void add(int X,int Y);
}
class ABC implements I1
{
public void add(int X,int Y)
{
int Z=X+Y;
System.out.println("addition="+Z);
}
public static void main(String A[])
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter two integer no");
int a=sc.nextInt();
Department of Information Technology | APSIT
int b=sc.nextInt();
ABC obj=new ABC();
obj.add(a,b);
}
}

// program to extend an interface
import java.util.*;
interface I1
{
public void add(int X,int Y);
}
class ABC implements I1
{
public void add(int X,int Y)
{
int Z=X+Y;
System.out.println("addition="+Z);
}
public void subtract(int x, int y){
int S = x-y;
System.out.println("Substraction="+S);
}
public static void main(String A[])
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter two integer no");
int a=sc.nextInt();
int b=sc.nextInt();
ABC obj=new ABC();
obj.add(a,b);
obj.substract(a,b);
}
}
