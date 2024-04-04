using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Number\tSquare\tCube");
        for (int i = 1; i <= 10; i++)
        {
            int square = i * i;
            int cube = i * i * i;
            Console.WriteLine($"{i}\t{square}\t{cube}");
        }
    }
}

