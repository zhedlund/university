using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace inlamningsuppgift1_winforms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void buttonBerakna_Click(object sender, EventArgs e)
        {
            // Kontrollera om texten är korrekt innan konvertering till heltal
            if (!int.TryParse(textBoxPris.Text, out int pris) || !int.TryParse(textBoxBetalt.Text, out int betalt))
            {
                MessageBox.Show("Felaktigt angivna värden.");
                return;
            }

            // Kontrollera om betalat belopp är tillräckligt
            if (betalt < pris)
            {
                MessageBox.Show("Betalat för lite. Köpet kunde ej genomföras.");
                return;
            }

            // Beräkna växeln
            int vaxel = betalt - pris;

            // Skapa en sträng för att visa växeln i MessageBox
            string vaxelText = "Växel tillbaka:\n";

            int[] valorer = { 500, 200, 100, 50, 20, 10, 5, 1 };
            string[] valortexter = { "femhundralapp", "tvåhundralapp", "hundralapp", "femtiolapp", "tjuga", "tia", "femma", "enkrona" };

            for (int i = 0; i < valorer.Length; i++)
            {
                int antalAvValorer = vaxel / valorer[i];
                vaxel %= valorer[i];

                if (antalAvValorer > 0)
                {
                    string valortext = valortexter[i];
                    if (antalAvValorer > 1)
                    {
                        valortext = valortext.Substring(0, valortext.Length - 1) + "or";
                    }
                    vaxelText += $"{antalAvValorer} {valortext}\n";
                }
            }

            // Visa växeln i en MessageBox
            MessageBox.Show(vaxelText, "Växelberäkning", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void buttonAvsluta_Click(object sender, EventArgs e)
        {
            Application.Exit(); // Avslutar applikationen när knappen Avsluta klickas
        }
    }
}
