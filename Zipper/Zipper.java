/*
    Zipper - Author: Cameron MacDonald

    Debugging statements are commented out, but feel free to use them to analyze runtime or see the arrays* 
    that are filled for each case.

    *Beware when running large cases, this will dump a lot of text into the terminal.

    This code has been written assuming perfect input following ACM competition standards.
*/

import java.util.*;
import java.io.*;

public class Zipper {

    public static void main(String args[])
    {

        Scanner sc = new Scanner(System.in); //Uses standard input: $java Zipper < inputFile.inp
        int caseNum = 0;

        while(sc.hasNext())
        {
            /* long start = System.nanoTime(); */
            boolean isValid;
            caseNum++;

            String s1 = sc.next();
            if (s1.equals("."))
            {
                /* long end = System.nanoTime();
                System.out.println("Runtime (ms): " + (end - start)); */
                return;
            }
            String s2 = sc.next();
            String s3 = sc.next();

            /* Debugging printing, prints case number and input read in.
            System.out.println("Case " + caseNum);
            System.out.println("S1: " + s1 + " S2: " + s2 + " S3: " + s3);
            System.out.println();*/

            boolean[][] arr = new boolean [s1.length()+1][s2.length()+1]; // Initialize new array

            isValid = check(s1, s2, s3, 0, 0, arr);

            if (isValid)
            {
                System.out.println("Case " + caseNum + ": yes");
            }
            else
            {
                System.out.println("Case " + caseNum + ": no");
            }
        }
        return;
    }

    public static boolean check (String s1, String s2, String s3, int p1, int p2, boolean[][] arr)
    {

        if (s1.length() + s2.length() != s3.length()) //If s3 length is not equal to s1.len + s2.len, not a possible interleaving
        {
            return false;
        }

        //Fill array
        for (int i = s1.length(); i > -1; i--)
        {
            for (int j = s2.length(); j > -1; j--)
            {
                if (i == s1.length() && j == s2.length()) //Base case
                {
                    arr[i][j] = true;
                }
                else if (i == s1.length()) //First iteration through j loop
                {
                    if (s2.charAt(j) == s3.charAt(j+i))
                    {
                        arr[i][j] = true;
                    }
                    else
                    {
                        arr[i][j] = false;
                    }
                }
                else if (j == s2.length()) //First step of all iterations after first i
                {
                    if (s1.charAt(i) == s3.charAt(i+j))
                    {
                        arr[i][j] = true;
                    }
                    else
                    {
                        arr[i][j] = false;
                    }
                }
                else if (s1.charAt(i) == s3.charAt(i+j) && s2.charAt(j) == s3.charAt(j+i)) //Both match
                {
                    arr[i][j] = arr[i+1][j] || arr[i][j+1];
                }
                else if (s1.charAt(i) == s3.charAt(i+j)) //s1 match
                {
                    arr[i][j] = arr[i+1][j];
                }
                else if (s2.charAt(j) == s3.charAt(i+j)) //s2 match
                {
                    arr[i][j] = arr[i][j+1];
                }
                else //Neither match
                {
                    arr[i][j] = false;
                }
            }
        }

        //Debugging: Prints entire memoized array
        /*for (int i = 0; i <= s2.length(); i++)
        {
            for (int j = 0; j <= s1.length(); j++)
            {
                System.out.format("%-8s", arr[j][i]);
            }
            System.out.println();
        }
        System.out.println();*/

        return arr[0][0];
    }
}
