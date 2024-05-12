using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Battleship
{
    public partial class Form3 : Form
    {

        public Form3()
        {
            InitializeComponent();

        }

        private void Form3_Load(object sender, EventArgs e)
        {
            DataSave data1 = new DataSave();
            int wins = 0;
            int loses = 0;
            int averageTime = 0;
            int bestTime = 0;
            data1.Sum(ref wins, ref loses, ref averageTime, ref bestTime);
            //MessageBox.Show(Convert.ToString(wins),Convert.ToString(loses));
            label2.Text=wins.ToString();
            label3.Text=loses.ToString();
            label5.Text=averageTime.ToString();
            label7.Text=bestTime.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }


    }
}
