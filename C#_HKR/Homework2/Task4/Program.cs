using System;

class Program
{
    static void Main(string[] args)
    {
        double worldPopulation = 6.5e9; // 6.5 billion
        double growthRate = 0.014; // 1.4%
        double targetPopulation = 1e10; // 10 billion

        int year = 0;
        while (worldPopulation < targetPopulation)
        {
            worldPopulation *= (1 + growthRate); // Calculate population growth
            year++;
        }

        Console.WriteLine($"The year when the world population exceeds 10 billion is: {DateTime.Now.Year + year}");
    }
}

