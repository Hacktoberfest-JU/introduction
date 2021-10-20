import java.io.*;

class GFG {


	public static void main(String[] args)
	{
		
		int arr[] = { 3, 5, 9, 2, 8, 10, 11 };

		int val = 17;

		System.out.println(isPairSum(arr, arr.length, val));
	}

	
	private static int isPairSum(int A[], int N, int X)
	{
		
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				
				if (i == j)

		
					continue;

				if (A[i] + A[j] == X)
					return 1;

				if (A[i] + A[j] > X)

				
					break;
			}
		}

		
		return 0;
	}
}
