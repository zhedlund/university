public class Program
{
    public static void Main(string[] args)
    {
        Task1();
        Task2();
        Task3();
        Task4();
        Task5();
        Task6();
        Task7();
        Task8();
    }
    public static void Task1()
    {
        Console.WriteLine("Please enter the first string:");
        string firstString = Console.ReadLine();

        Console.WriteLine("Please enter the second string:");
        string secondString = Console.ReadLine();

        string concatenatedString = firstString + " " + secondString;
        Console.WriteLine("The result is: " + concatenatedString);
        Console.WriteLine();
    }
    public static void Task2()
    {
        Console.WriteLine("Please enter a number:");
        int number = Convert.ToInt32(Console.ReadLine());

        if (number % 2 == 0)
        {
            Console.WriteLine("The number is even");
        }
        else
        {
            Console.WriteLine("The number is odd");
        }
        Console.WriteLine();
    }
    public static void Task3()
    {

        Console.WriteLine("Enter the first number:");
        string firstNumber = Console.ReadLine();
        Console.WriteLine("Enter the second number:");
        string secondNumber = Console.ReadLine();
        Console.WriteLine("Enter the third number:");
        string thirdNumber = Console.ReadLine();

        Console.WriteLine($"{firstNumber}\t{secondNumber}\t{thirdNumber}");
    }
    public static void Task4()
    {
        Console.WriteLine("   ZZZZZZZZZ");
        Console.WriteLine("         ZZ");
        Console.WriteLine("       ZZ");
        Console.WriteLine("     ZZ");
        Console.WriteLine("   ZZZZZZZZZ");
        Console.WriteLine("   H       H");
        Console.WriteLine("   H       H");
        Console.WriteLine("   HHHHHHHHH");
        Console.WriteLine("   H       H");
        Console.WriteLine("   H       H");
    }
    public static void Task5()
    {
        Console.WriteLine("Please enter the first number:");
        int x = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Please enter the second number:");
        int y = Convert.ToInt32(Console.ReadLine());

        int sum = x + y;
        int difference = x - y;
        int product = x * y;
        int division = x / y;
        int remainder = x % y;

        Console.WriteLine($"The sum of {x} and {y} is {sum}");
        Console.WriteLine($"The difference of {x} and {y} is {difference}");
        Console.WriteLine($"The product of {x} and {y} is {product}");
        Console.WriteLine($"The division of {x} by {y} is {division}");
        Console.WriteLine($"The remainder of {x} divided by {y} is {remainder}");
    }
    public static void Task6()
    {
        Console.WriteLine("Please enter the radius of the circle:");
        int radius = Convert.ToInt32(Console.ReadLine());

        float diameter = 2 * radius;
        float circumference = 2 * (float)Math.PI * radius;
        float area = (float)Math.PI * radius * radius;

        Console.WriteLine($"Diameter: {diameter}");
        Console.WriteLine($"Circumference: {circumference}");
        Console.WriteLine($"Area: {area}");
    }
    public static void Task7()
    {
        Console.WriteLine("Please enter a four-digit number:");
        int number = Convert.ToInt32(Console.ReadLine());

        int thousands = number / 1000;
        int hundreds = (number / 100) % 10;
        int tens = (number / 10) % 10;
        int ones = number % 10;

        Console.WriteLine($"{thousands}\t{hundreds}\t{tens}\t{ones}");
    }
    public static void Task8()
    {
        Console.WriteLine("Please enter a number:");
        int number = Convert.ToInt32(Console.ReadLine());

        int square = number * number;
        int cube = number * number * number;

        Console.WriteLine($"number\t square\t cube");
        Console.WriteLine($"{number}\t {square}\t {cube}");
    }
}