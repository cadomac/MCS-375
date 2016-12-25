import java.util.*;
import java.io.*;
import java.math.*;

public class BigRoot
{
	public static BigInteger nthRoot(BigInteger n, BigInteger p)
	{
		if (p.compareTo(BigInteger.ZERO) == 0) // nth root of 0 = 0
		{
			return BigInteger.ZERO;
		}

		if (p.compareTo(BigInteger.ZERO) == -1) // Only positive values allowed here
		{
			return BigInteger.valueOf(-1);
		}

		BigInteger one = BigInteger.ONE;
		BigInteger x = one;
		BigInteger y = p;
		BigInteger k = BigInteger.ZERO;

		while(x.compareTo(y) == -1)
		{
			k = ((x.add(y)).divide(BigInteger.valueOf(2))); // Pick a random number somewhere in the middle

			if (k.pow(n.intValue()).compareTo(p) == 0) // Guess was correct
			{
				x = k;
				break;
			}
			if (k.pow(n.intValue()).compareTo(p) == 1) // Guess was too large
			{
				y = k.subtract(one);
			}
			else // Guess was too small
			{
				x = k.add(one);
			}
		}

		if (x.pow(n.intValue()).compareTo(p) == 0) // Check to make sure the value we found is the true root
		{
			return x;
		}
		else // Must have been close, but no cigar
		{
			return BigInteger.valueOf(-1);
		}
		
	}

	public static void main(String[] args)
	{
	    Scanner sc = new Scanner(System.in); //Uses standard input: $java BigRoot < test.inp
        int caseNum = 0;
        while(sc.hasNext())
        {
        	boolean isValid;
            caseNum++;

            BigInteger n = sc.nextBigInteger();

            if (n.compareTo(BigInteger.ZERO) == 0)
            {
            	return;
            }
            
            BigInteger p = sc.nextBigInteger();

            BigInteger solution = nthRoot(n, p);

            if (solution.compareTo(BigInteger.valueOf(-1)) == 0)
            {
            	System.out.printf("Case %d: No solution\n\n", caseNum);
            }
            else
            {
            	System.out.printf("Case %d: %s\n\n", caseNum, solution.toString());
            }
        }
	}
}
