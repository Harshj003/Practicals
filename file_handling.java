// to create a new file and write byte stream to it
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.io.FileOutputStream;
public class FileOutputStreamExample2
{
public static void main(String args[])
{
try
{
File myObj = new File("test.txt");
FileOutputStream fout=new
FileOutputStream("/home/kashish/Documents/Java/test.txt");
String s="Welcome to java
class"; byte b[]=s.getBytes();
fout.write(b);
fout.close();
System.out.println("success...");
}
catch(Exception e)
{
System.out.println(e);
}
}
}

// two threads such that one thread will print even number and another will print odd
// number in an ordered fashion
import java.io.FileInputStream;
public class DataStreamExample
{
public static void main(String args[])
{
try
{
FileInputStream fin=new
FileInputStream("/home/kashish/Documents/Java/test.txt");
int i=0;
while((i=fin.read())!=-1)
{
System.out.print((char)i);
}
fin.close();
}
catch(Exception e)
{
System.out.println(e);
}
}
}
