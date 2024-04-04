using System;

class Program
{
    static void Main(string[] args)
    {
        string gradeInput;
        while (true)
        {
            Console.WriteLine("Enter your grade ('A' to 'F' or 'Fx') or 'G' to end the program:");
            gradeInput = Console.ReadLine().ToUpper(); // Read the grade input and convert to uppercase
            
            if (gradeInput == "G")
            {
                Console.WriteLine("Program ended.");
                break;
            }

            Console.WriteLine();
            switch (gradeInput)
            {
                case "A":
                    Console.WriteLine("Excellent - outstanding performance with only minor errors");
                    break;
                case "B":
                    Console.WriteLine("Very good - above the average standard but with some errors");
                    break;
                case "C":
                    Console.WriteLine("Good - generally sound work with a number of notable errors");
                    break;
                case "D":
                    Console.WriteLine("Satisfactory - fair but with significant shortcomings");
                    break;
                case "E":
                    Console.WriteLine("Sufficient - performance meets the minimum criteria");
                    break;
                case "F":
                    Console.WriteLine("Fail - considerable further work is required");
                    break;
                case "FX":
                    Console.WriteLine("Fx Fail - some more work required before the credit can be awarded");
                    break;
                default:
                    Console.WriteLine("Invalid grade. Please enter a grade from 'A' to 'F' or 'G' to end the program.");
                    break;
            }
        }
    }
}
