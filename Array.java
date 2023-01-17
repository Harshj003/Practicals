// Program to demonstrate single dimensional java array
import java.util.*;
class Array1
{
public static void main(String args[])
{
int a[] = new int[5];
a[0] = 10;
a[1] = 20;
a[2] = 70;
a[3] = 40;
a[4] = 50;
for(int i=0;i<a.length;i++)
{
System.out.println(a[i]);
}
}
}

// Passing array to method in java
import java.util.*;
class Array2
{
static void min(int arr[])
{
int min = arr[0];
for(int i=1;i<arr.length;i++)
if(min>arr[i])
min=arr[i];
System.out.println(min);
}
public static void main(String args[])
{
int a[] = {33,3,4,5};
min(a);
}
}

// Program to demonstrate 2 dimensional java array
import java.util.*;
class Array3
{
public static void main(String args[])
{
int a[][] = {{1,3,4},{3,4,5}};
int b[][] = {{1,3,4},{3,4,5}};
int c[][] = new int[2][3];
for(int i=0;i<2;i++)
{
for(int j=0;j<3;j++)
{
c[i][j] = a[i][j] + b[i][j];
System.out.println(c[i][j]+" ");
}
System.out.println();
}
}
}

// Program to test whether given element is present in the vector or not
import java.util.Vector;
public class vector2
{
public static void main(String args[])
{
Vector<String>v = new
Vector<String>(); v.add("Apple");
v.add("Orange");
v.add("Guava");
v.add("Papaya");
v.add("Pineapple");
v.add("Apple");
v.add("Orange");
boolean x = v.contains("Guava");
System.out.println("Does Vector contain Guava?
"+x);
int index =
v.indexOf("Papaya");
if(index==-1)
System.out.println("Vector does not contain Papaya");
else
System.out.println("Vector contains Papaya at index: "+index);
int lastIndex =
v.lastIndexOf("Orange"); if(index==-1)
System.out.println("Vector does not contain Orange");
else
  System.out.println("Last Occurrence of Orange is at index: "+lastIndex);
}
}

