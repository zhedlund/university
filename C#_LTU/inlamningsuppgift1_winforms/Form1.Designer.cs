﻿namespace inlamningsuppgift1_winforms
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.buttonBerakna = new System.Windows.Forms.Button();
            this.buttonAvsluta = new System.Windows.Forms.Button();
            this.textBoxBetalt = new System.Windows.Forms.TextBox();
            this.textBoxPris = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // buttonBerakna
            // 
            this.buttonBerakna.Location = new System.Drawing.Point(365, 214);
            this.buttonBerakna.Name = "buttonBerakna";
            this.buttonBerakna.Size = new System.Drawing.Size(75, 23);
            this.buttonBerakna.TabIndex = 0;
            this.buttonBerakna.Text = "Beräkna";
            this.buttonBerakna.UseVisualStyleBackColor = true;
            this.buttonBerakna.Click += new System.EventHandler(this.buttonBerakna_Click);
            // 
            // buttonAvsluta
            // 
            this.buttonAvsluta.Location = new System.Drawing.Point(365, 257);
            this.buttonAvsluta.Name = "buttonAvsluta";
            this.buttonAvsluta.Size = new System.Drawing.Size(75, 23);
            this.buttonAvsluta.TabIndex = 1;
            this.buttonAvsluta.Text = "Avsluta";
            this.buttonAvsluta.UseVisualStyleBackColor = true;
            this.buttonAvsluta.Click += new System.EventHandler(this.buttonAvsluta_Click);
            // 
            // textBoxBetalt
            // 
            this.textBoxBetalt.Location = new System.Drawing.Point(365, 182);
            this.textBoxBetalt.Name = "textBoxBetalt";
            this.textBoxBetalt.Size = new System.Drawing.Size(100, 20);
            this.textBoxBetalt.TabIndex = 2;
            // 
            // textBoxPris
            // 
            this.textBoxPris.Location = new System.Drawing.Point(365, 139);
            this.textBoxPris.Name = "textBoxPris";
            this.textBoxPris.Size = new System.Drawing.Size(100, 20);
            this.textBoxPris.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(365, 120);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Ange pris:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(365, 166);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(37, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Betalt:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBoxPris);
            this.Controls.Add(this.textBoxBetalt);
            this.Controls.Add(this.buttonAvsluta);
            this.Controls.Add(this.buttonBerakna);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonBerakna;
        private System.Windows.Forms.Button buttonAvsluta;
        private System.Windows.Forms.TextBox textBoxBetalt;
        private System.Windows.Forms.TextBox textBoxPris;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
    }
}

