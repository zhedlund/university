using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Celsius\tFahrenheit");
        for (int celsius = -30; celsius <= 50; celsius += 5) // Loop through all celsius values
        {
            double fahrenheit = CelsiusToFahrenheit(celsius);
            Console.WriteLine($"{celsius}\t{fahrenheit}");
        }
    }

    static double CelsiusToFahrenheit(int celsius)
    {
        return (9.0 / 5.0) * celsius + 32; // Convert Celsius to Fahrenheit
    }
}

