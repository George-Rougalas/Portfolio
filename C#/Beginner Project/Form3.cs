using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Aaaingment_1
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }
        private void Form3_Load(object sender, EventArgs e)
        {//here the labels change according with the high scores
            Label[] la = { label2, label3, label4, label5, label6, label7, label8, label9, label10, label11 };
            int i = 0;
            foreach (string line in System.IO.File.ReadLines("top_scores.txt"))
            {
                la[i++].Text = i + ") " + line;
            }
        }
        private void label5_Click(object sender, EventArgs e)
        {
            //aciidentally made
        }
    }
}
