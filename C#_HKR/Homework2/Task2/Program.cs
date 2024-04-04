using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter an integer:");
        if (int.TryParse(Console.ReadLine(), out int radius) && radius > 0) // Check if input is a positive integer
        {
            CalculateSphereVolumes(radius);
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a positive integer.");
        }
    }

    static void CalculateSphereVolumes(int maxRadius)
    {
        for (int r = 1; r <= maxRadius; r++) // Loop through all radii from 1 to maxRadius
        {
            double volume = CalculateSphereVolume(r);
            Console.WriteLine($"Sphere's volume with radius {r} is {volume:F2}");
        }
    }

    static double CalculateSphereVolume(int radius)
    {
        return (4.0 / 3.0) * Math.PI * Math.Pow(radius, 3); // Calculate and return the sphere volume
    }
}

