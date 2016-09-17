using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

public class EvenTree
{  
    private static Dictionary<long, List<long>> dicEdges = new Dictionary<long, List<long>>();
    private static long N;

    private static long NumberEdges = 0;

    static long FindEdges(long v, long prev)
    {

        long val = 1;
        for (var i = 0; i < dicEdges[v].Count; i++)
        {
            var cur = dicEdges[v][i];
            if (prev != cur)
            {
                val += FindEdges(cur, v);
            }
        }

        if (val % 2 == 0)
        {
            NumberEdges++;
            return 0;
        }
        else
        {
            return val;
        }
    }

    static void Main(String[] args)
    {
        int index = 0;

        string tmp = Console.ReadLine();
        //string tmp = args[index]; 
        string[] split = tmp.Split(new Char[] { ' ', '\t', '\n' });

        N = Convert.ToInt64(split[0].Trim());
        var M = Convert.ToInt64(split[1].Trim());

        index++;


        for (int i = 0; i < M; i++)
        {
            tmp = Console.ReadLine();
            //tmp = args[index]; 
            index++;

            split = tmp.Split(new Char[] { ' ', '\t', '\n' });

            var a = Convert.ToInt64(split[0].Trim());
            var b = Convert.ToInt64(split[1].Trim());
            if (!dicEdges.ContainsKey(a))
            {
                dicEdges.Add(a, new List<long>());
            }
            if (!dicEdges.ContainsKey(b))
            {
                dicEdges.Add(b, new List<long>());
            }
            dicEdges[a].Add(b);
            dicEdges[b].Add(a);
        }
        FindEdges(1, -1);

        string res = (NumberEdges - 1).ToString();
        Console.WriteLine(res);
    }
}