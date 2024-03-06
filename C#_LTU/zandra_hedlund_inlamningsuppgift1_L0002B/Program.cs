using System;

class Program
{
    static void Main(string[] args)
    {
        // Läs in pris och betalt belopp
        Console.Write("Ange pris: ");
        int pris = Convert.ToInt32(Console.ReadLine());
        Console.Write("Betalt: ");
        int betalt = Convert.ToInt32(Console.ReadLine());

        if (betalt < pris)
        {
            Console.WriteLine("Betalat för lite, köpet kunde inte genomföras.");
            return ;
        }
        int vaxel = betalt - pris;
        Console.WriteLine("Växel tillbaka:");

        // Definierar valörer och motsvarande textrepresentation
        int[] valorer = { 500, 200, 100, 50, 20, 10, 5, 1 };
        string[] valortexter = { "femhundralapp", "tvåhundralapp", "hundralapp", "femtiolapp", "tjuga", "tia", "femma", "enkrona" };

        // Loopa igenom varje valör för att beräkna och skriva ut växeln
        for (int i = 0; i < valorer.Length; i++)
        {
            // Beräkna antalet av den aktuella valören i växeln
            int antalAvValorer = vaxel / valorer[i];
            vaxel %= valorer[i]; // Uppdatera växeln efter att ha tagit bort den aktuella valören

            // Skriv ut aktuell valör
            if (antalAvValorer > 0)
            {
                string valortext = valortexter[i];
                if (antalAvValorer > 1)
                {
                    // Tar bort sista bokstaven och lägger till "or" för plural
                    valortext = valortext.Substring(0, valortext.Length - 1) + "or";
                }
                Console.WriteLine($"{antalAvValorer} {valortext}");
            }
        }
    }
}
