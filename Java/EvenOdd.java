import java.util.Scanner;
public class EvenOdd
{
	public void main(String[] args)
	{
	     Scanner input = new Scanner(System.in);
	     System.out.println("Enter a number: ");
   	     int number = input.nextInt();
             if(number % 2 == 0)
 		System.out.println("The Entered number is even.");
   	     else
                System.out.println("The Entered number is odd.");   	    
	}
}