// thread creation by extending thread class
class MultithreadingDemo extends Thread
{
public void run()
{
System.out.println("My thread is in running state.");
}
public static void main(String args[])
{
MultithreadingDemo obj = new MultithreadingDemo();
obj.start();
}
}

// two threads such that one threadd will print even numbers and another will print odd number in an ordered fashion
class OddThread extends Thread
{
int limit;
sharedPrinter printer;
public OddThread(int limit, sharedPrinter printer)
{
this.limit = limit;
this.printer = printer;
}
@Override
public void run()
{
int oddNumber = 1;
while (oddNumber <= limit)
{
printer.printOdd(oddNumber);
oddNumber = oddNumber + 2;
}
}
}
class EvenThread extends Thread
{
int limit;
sharedPrinter printer;
public EvenThread(int limit, sharedPrinter printer)
{
this.limit = limit;
this.printer = printer;
}
@Override
public void run()
{
int evenNumber = 2;
while (evenNumber <= limit)
{
printer.printEven(evenNumber);
evenNumber = evenNumber + 2;
}
}
}
class sharedPrinter
{
boolean isOddPrinted = false;
synchronized void printOdd(int number)
{
while (isOddPrinted)
{
try
{
wait();
}
catch (InterruptedException e)
{
e.printStackTrace();
}
}
System.out.println(Thread.currentThread().getName()+" : "+number);
isOddPrinted = true;
try
{
Thread.sleep(1000);
}
catch (InterruptedException e)
{
e.printStackTrace();
}
notify();
}
synchronized void printEven(int number)
{
while (! isOddPrinted)
{
try
{
wait();
}
catch (InterruptedException e)
{
e.printStackTrace();
}
}
System.out.println(Thread.currentThread().getName()+" : "+number);
isOddPrinted = false;
try
{
Thread.sleep(1000);
}
catch (InterruptedException e)
{
e.printStackTrace();
}
notify();
}
}
public class MainClass
{
public static void main(String[] args)
{
sharedPrinter printer = new sharedPrinter();
OddThread oddThread = new OddThread(20, printer); 
oddThread.setName("Odd-Thread");
EvenThread evenThread = new EvenThread(20,printer); 
evenThread.setName("Even-Thread");
oddThread.start();
evenThread.start();
}
}
