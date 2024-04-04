using System;

class Program
{
    static void Main(string[] args)
    {
        int min = int.MaxValue; // Initialize min to intmax value, that way any number entered will be less than it
        int number;

        Console.WriteLine("Enter a series of integers. Enter 0 to finish:");

        do
        {
            Console.Write("Enter an integer: ");
            number = int.Parse(Console.ReadLine());

            if (number != 0 && number < min) // Check if number is less than min
            {
                min = number; // If it is, assign number to min
            }

        } while (number != 0);

        Console.WriteLine($"The minimum number entered is: {min}");
    }
}

