using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Inlamningsuppgift2
{
    class Säljare
    {
        public string Namn { get; set; }
        public string Personnummer { get; set; }
        public string Distrikt { get; set; }
        public int SåldaArtiklar { get; set; }

        public int Nivå
        {
            get
            {
                if (SåldaArtiklar > 199)
                    return 4;
                else if (SåldaArtiklar >= 100 && SåldaArtiklar <= 199)
                    return 3;
                else if (SåldaArtiklar >= 50 && SåldaArtiklar <= 99)
                    return 2;
                else
                    return 1;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Säljare> säljare = new List<Säljare>();

            Console.Write("Ange antalet säljare: ");
            int antalSäljare = int.Parse(Console.ReadLine());

            for (int i = 0; i < antalSäljare; i++)
            {
                Console.WriteLine($"\nSäljare {i + 1}:");
                Säljare säljareInfo = new Säljare();

                Console.Write("Namn: ");
                säljareInfo.Namn = Console.ReadLine();

                Console.Write("Personnummer: ");
                säljareInfo.Personnummer = Console.ReadLine();

                Console.Write("Distrikt: ");
                säljareInfo.Distrikt = Console.ReadLine();

                Console.Write("Antal sålda artiklar: ");
                säljareInfo.SåldaArtiklar = int.Parse(Console.ReadLine());

                säljare.Add(säljareInfo);
            }

            // Sortera säljare efter nivå
            säljare = säljare.OrderByDescending(s => s.Nivå).ToList();

            // Skriv sammanfattning till konsol
            Console.WriteLine("\nNamn\tPersnr\tDistrikt\tAntal");

            var nivåer = säljare.GroupBy(s => s.Nivå);
            foreach (var nivå in nivåer)
            {
                foreach (var säljareInfo in nivå)
                {
                    Console.WriteLine($"{säljareInfo.Namn}\t{säljareInfo.Personnummer}\t{säljareInfo.Distrikt}\t{säljareInfo.SåldaArtiklar}");
                }
                Console.WriteLine($"{AntalSäljare(nivå.Count())} nådde nivå {nivå.Key}: {NivåBeskrivning(nivå.Key)}\n");
            }

            // Skriv sammanfattning till fil
            using (StreamWriter skrivare = new StreamWriter("sammanfattning.txt"))
            {
                skrivare.WriteLine("Namn\tPersnr\tDistrikt\tAntal");
                foreach (var nivå in nivåer)
                {
                    foreach (var säljareInfo in nivå)
                    {
                        skrivare.WriteLine($"{säljareInfo.Namn}\t{säljareInfo.Personnummer}\t{säljareInfo.Distrikt}\t{säljareInfo.SåldaArtiklar}");
                    }
                    skrivare.WriteLine($"{AntalSäljare(nivå.Count())} nådde nivå {nivå.Key}: {NivåBeskrivning(nivå.Key)}\n");
                }
            }

            Console.WriteLine("Sammanfattning skriven till säljare_sammanfattning.txt");
        }

        static string AntalSäljare(int antal)
        {
            return antal == 1 ? "1 säljare" : $"{antal} säljare";
        }

        static string NivåBeskrivning(int nivå)
        {
            switch (nivå)
            {
                case 4:
                    return "> 199";
                case 3:
                    return "100-199";
                case 2:
                    return "50-99";
                case 1:
                    return "< 50";
                default:
                    return "Okänd";
            }
        }
    }
}


