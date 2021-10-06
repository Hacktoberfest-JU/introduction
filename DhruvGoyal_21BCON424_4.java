//*****************************************************************RANGE OF PRIME NUMBERS********************************************************
import java.util.*;
import java.io.*;

//MAIN PROGRAM

class Primeno

{
    public static void main (String args[])

    {
        Scanner sc = new Scanner (System.in);
        int i, j, num=0, count=0; int x,y;
        System.out.println ("Enter Range to find out prime numbers in the range:");
        
        x = sc.nextInt();             //lower limit
        y = sc.nextInt();                //upper limit
System.out.println("The prime numbers in given range are:");
    for(i=x;i<=y;i++)
    {int c=0;
        for(num=i;num>=1;num--)
        {if(i%num==0)
            c++;
        }
        if(c==2)
        {System.out.print(i+"\t");
    count++;
System.out.println();}
    }
    System.out.println("Total number of prime numbers in the given range:"+count);
}
}
