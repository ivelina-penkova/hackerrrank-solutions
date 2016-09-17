using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class AngryProfessor
{

    static void Main(String[] args)
    {
        int t = Convert.ToInt32(Console.ReadLine());
        for (int a0 = 0; a0 < t; a0++)
        {
            string[] temp = Console.ReadLine().Split();
            int N = int.Parse(temp[0]);
            int K = int.Parse(temp[1]);
            string[] arr_temp = Console.ReadLine().Split();
            int[] arr = new int[N];
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = int.Parse(arr_temp[i]);
            }

            int presentStudents = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] <= 0)
                {
                    presentStudents++;
                }
            }

            if (presentStudents >= K)
            {
                Console.WriteLine("NO");
            }
            else
            {
                Console.WriteLine("YES");
            }
        }

    }
}
