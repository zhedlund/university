using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter the size of the square (2-9):");
        if (int.TryParse(Console.ReadLine(), out int size) && size >= 2 && size <= 9)
        {
            DrawSquare(size);
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a number between 2 and 9.");
        }
    }

    static void DrawSquare(int size)
    {
        for (int i = 0; i < size; i++) // Loop through all rows
        {
            for (int j = 0; j < size; j++) // Loop through all columns
            {
                Console.Write("*");
            }
            Console.WriteLine();
        }
    }
}

