using System;
using System.Collections.Generic;
using System.IO;

class TheMaximumSubarray
{
    static void Main(String[] args)
    {
        int numTests = int.Parse(Console.ReadLine());
        for (int test = 0; test < numTests; test++)
        {
            int numItems = int.Parse(Console.ReadLine());
            int[] items = new int[numItems];
            string[] stringItems = Console.ReadLine().Split(' ');
            for (int item = 0; item < numItems; items[item] = int.Parse(stringItems[item++])) ;

            Console.WriteLine("{0} {1}", MaxContiguous(items), MaxNonContiguous(items));
        }
    }

    static int MaxContiguous(int[] items)
    {
        int max_sum = int.MinValue;
        int current_sum = 0;
        int maxItem = int.MinValue;

        for (int index = 0; index < items.Length; index++)
        {
            int accValue = current_sum + items[index];
            if (accValue > 0)
            {
                current_sum = accValue;
                if (current_sum == 0)
                {
                    current_sum = accValue;
                }
            }
            else
            {
                current_sum = 0;
            }

            if (current_sum > max_sum)
            {
                max_sum = current_sum;
            }

            if (items[index] > maxItem)
            {
                maxItem = items[index];
            }
        }

        return max_sum > 0 ? max_sum : maxItem;
    }

    static int MaxNonContiguous(int[] items)
    {
        int sum = 0;
        int maxItem = int.MinValue;

        for (int index = 0; index < items.Length; index++)
        {
            if (items[index] > 0)
            {
                sum += items[index];
            }

            if (items[index] > maxItem)
            {
                maxItem = items[index];
            }
        }

        return sum > 0 ? sum : maxItem;
    }
}