using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter an integer and press Enter key:");
        int int1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter an integer and press Enter key:");
        int int2 = int.Parse(Console.ReadLine());
        Console.WriteLine($"The sum of the two integers is {Add(int1, int2)}");

        Console.WriteLine("Enter a float number and press Enter key:");
        double float1 = double.Parse(Console.ReadLine());
        Console.WriteLine("Enter a float number and press Enter key:");
        double float2 = double.Parse(Console.ReadLine());
        Console.WriteLine($"The sum of the two float numbers is {Add(float1, float2)}");

        Console.WriteLine("Enter the first name and press Enter key:");
        string firstName = Console.ReadLine();
        Console.WriteLine("Enter the last name and press Enter key:");
        string lastName = Console.ReadLine();
        Console.WriteLine($"Your name is {Add(firstName, lastName)}");

        Console.WriteLine("Enter the real part of the first complex number and press Enter key:");
        int real1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the imaginary part of the first complex number and press Enter key:");
        int imag1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the real part of the second complex number and press Enter key:");
        int real2 = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the imaginary part of the second complex number and press Enter key:");
        int imag2 = int.Parse(Console.ReadLine());
        Console.WriteLine($"The sum of the two complex numbers is {Add(real1, imag1, real2, imag2)}");
    }

    // Method to add two integers
    static int Add(int a, int b)
    {
        return a + b;
    }

    // Overloaded method to add two floats
    static double Add(double a, double b)
    {
        return a + b;
    }

    // Overloaded method to concatenate two names
    static string Add(string firstName, string lastName)
    {
        return $"{firstName} {lastName}";
    }

    // Overloaded method to add two complex numbers
    static string Add(int real1, int imag1, int real2, int imag2)
    {
        int sumReal = real1 + real2;
        int sumImag = imag1 + imag2;
        return $"{sumReal} + i{sumImag}";
    }
}
