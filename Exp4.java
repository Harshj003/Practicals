// Fibonacci and reverse of number without recurssion
public class ABC
{
 public static void main(String args[]) {
 Scanner in = new Scanner(System.in);
 System.out.println("1. Fibonacci Series");
 System.out.println("2. Reverse of Number");
 System.out.print("Enter your choice: ");
 int ch = in.nextInt();

switch (ch)
{
 case 1:
 int a = 0, b = 1;
 System.out.print(a + " " + b);

 for (int i = 3; i <= 10; i++)
{
 int term = a + b;
 System.out.print(" " + term);
 a = b;
 b = term;
 }
 break;
 case 2:
 System.out.print("Enter number: ");
 int num = in.nextInt();
 int rev = 0;
int R;
 while (num != 0)
{
 R = num%10;
 rev = rev*10+R;
 Num = num/10;
 }
 System.out.println("Reverse of number " + " = " + rev);
 break;
 default:
 System.out.println("Incorrect choice");
 break;
 }
 }
}

// Fibonacci and reverse of number with recurssion
import java.util.*;
class Menu{
  static int n1= 0, n2 = 1, n3 = 0;
  static void FibNum(int n){
    if(n>0){
      n3 = n1+n2;
      System.out.println(" "+n3);
      n1 = n2;
      n2 = n3;
      FibNum(n-1);
    }
  }
  public static void reverseNumber(int number){
    if(numbet<10){
      System.out.println(number);
      return;
    }
    else{
      System.out.println(number%10);
      reverseNumber(numbet/10);
    }
  }
  public static void main(String args[]){
    int ch;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter your choice");
    ch = sc.nextInt();
    switch(ch){
      case 1:
        System.out.println("Enter value of n: ");
        int n = sc.nextInt();
        System.out.println("Fibonacci Series up to "+n+" Terms: ");
        System.out.println(n1+" "+n2);
        FibNum(n-2);
        System.out.println("\n");
        break;
        
      case 2:
        System.out.println("Enter the number that you want to reverse: ");
        int num = sc.nextInt();
        System.out.println("The reverse of the given number is: ");
        reverseNumber(num);
        break;
    }
  }
}
