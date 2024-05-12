using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.Common;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.AxHost;

namespace Battleship
{

    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        Navy player, enemy;
        bool done = false;
        int time = 0;
        DataSave data1 = new DataSave();
        private void Form2_Load(object sender, EventArgs e)
        {
            player = new Navy("Your");
            CreateGrid(label1.Location.X, label1.Location.Y, player);
            player.PlaceBoats(false);//creates boats for the object to SINK
            enemy = new Navy("The opponent's");
            CreateGrid(label3.Location.X, label3.Location.Y, enemy);
            enemy.PlaceBoats(true);//creates boats for the object to SINK, and displays them
            richTextBox1.Text = "Game is ready to start select a box and press FIRE!!! to play";
            data1.Create();
        }
        public void CreateGrid(int startX, int startY, Navy obj)
        {//originaly was called twice but cut during development
         //originally in the Navy class
            Button p = new Button();
            obj.spaces.Add(p);//so the array starts at 1 and matches the grid
            int column = 0, row = -1;
            for (int j = startY; j < startY + 40 * 10; j += 40)
            {
                row += 1;
                for (int i = startX; i < startX + 40 * 10; i += 40)
                {
                    column += 1; 
                    Button b = new Button();
                    b.Click += new EventHandler(GivePosition);
                    b.Location = new Point(i, j);
                    b.Size = new Size(35, 35);
                    b.Text = TranslateRow(row) + column.ToString();
                    //b.TextAlign = ContentAlignment.MiddleCenter; ;
                    //b.Font = new Font("Arial", 12, FontStyle.Bold);
                    Controls.Add(b);
                    obj.spaces.Add(b);//Fills 1-100
                }
                column = 0;
            }
        }
        public void GivePosition(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            if (!(btn.Text == ""))
            {
                textBox1.Text = btn.Text;
            }
        }
        public char TranslateRow(int x)
        {//a smart person would do: (ascii value of A) - 1 + (ascii value of x) //maybe next year...
            char y;
            if (x == 0)
                y = 'A';
            else if (x == 1)
                y = 'B';
            else if (x == 2)
                y = 'C';
            else if (x == 3)
                y = 'D';
            else if (x == 4)
                y = 'E';
            else if (x == 5)
                y = 'F';
            else if (x == 6)
                y = 'G';
            else if (x == 7)
                y = 'H';
            else if (x == 8)
                y = 'I';
            else
                y = 'J';
            return y;
        }
        public int TranslateRow(string y)
        {
            int x;
            if (y == "A")
                x = 0;
            else if (y == "B")
                x = 10;
            else if (y == "C")
                x = 20;
            else if (y == "D")
                x = 30;
            else if (y == "E")
                x = 40;
            else if (y == "F")
                x = 50;
            else if (y == "G")
                x = 60;
            else if (y == "H")
                x = 70;
            else if (y == "I")
                x = 80;
            else
                x = 90;
            return x;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (!done)
            {
                timer1.Enabled = true;
                FireTheCannons(textBox1.Text, player, enemy);
                if (player.NavyIsGone())
                {
                    GameOver(player);
                    done = true;
                }
                Random r = new Random();
                int x;
                do
                {
                    x = r.Next(1, 101);
                } while (enemy.hitSpaces[x]);
                if (!done)
                {
                    FireTheCannons2(textBox1.Text, enemy, player, x);
                    if (enemy.NavyIsGone())
                    {
                        GameOver(enemy);
                        done = true;
                    }
                }
            }
        }
        public void FireTheCannons(String gridPosition, Navy shooter, Navy opponent)
        {
            if (gridPosition == "")
            {
                richTextBox1.Text = "Please select a position\n" + richTextBox1.Text;
            }
            else
            {
                string t = gridPosition.Substring(1);
                int box = int.Parse(t);
                t = gridPosition.Substring(0, 1);
                box += TranslateRow(t);
                if (shooter.hitSpaces[box])
                {//useless?
                    richTextBox1.Text = "That space has been hit already\n\n" + richTextBox1.Text;
                }
                else
                {
                    richTextBox1.Text = shooter.HitBoatAt(box, opponent) + "\n\n" + richTextBox1.Text;
                    shooter.spaces[box].Click -= new EventHandler(GivePosition);
                    shooter.hitSpaces[box] = true;
                }
            }
        }
        public void FireTheCannons2(String gridPosition, Navy shooter, Navy opponent, int box)
        {
            if ( !(gridPosition == "") )
                {
                    richTextBox1.Text = shooter.HitBoatAt(box, opponent) + "\n" + richTextBox1.Text;
                    shooter.spaces[box].Click -= new EventHandler(GivePosition);
                    shooter.hitSpaces[box] = true;
                }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            time += 1;
            label6.Text= time.ToString();
        }
        public void ClearGrid(Navy obj)
        {
            for(int i = 1; i < 101; i++)
            {
                obj.spaces[i].Visible = false;
            }
        }
        public void GameOver(Navy obj)
        {
            timer1.Enabled = false;
            label6.Font = new Font("Arial", 32);
            label2.Visible = false;
            button1.Enabled = false;
            bool winner = true;
            richTextBox1.Text = "The Game Is Over\n\n" + richTextBox1.Text; 
            if(obj == enemy)
            {
                winner = false;
            }
            if(winner)
            {
                label4.Text = "YOU WON!!!";
                data1.Insert(1, 0, time);                
            }
            else
            {
                data1.Insert(0, 1, time);
            }
            label4.Visible = true;
            ClearGrid(player);
            ClearGrid(enemy);
            button2.Visible = true; 
            button3.Visible = true;
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Wins  -  Loses");
            Form2 f2 = new Form2();
            f2.Show();
            Close();
        }
    }
    public class Navy
    {
        public Random r;
        public List<Button> spaces = new List<Button>();
        public bool[] hitSpaces;
        public Ships carrier, torpido, warship, submarine;
        public String pronoun;
        public Navy(string s)
        {
            pronoun = s;
            hitSpaces = new bool[101];
        }
        public void PlaceBoats(bool showBoats)
        {
            bool[] occupied = new bool[101];
            r = new Random();
            bool test;
            int orientation = r.Next(0, 2);
            int position;
            //aircraft carrier, 5 squares
            carrier = new Ships(5, "aircraft carrier");
            if (orientation == 0)
            {//κάθετο
                position = r.Next(1, 61);
                for (int i1 = position; i1 < position + 50; i1 += 10)
                {
                    carrier.shipSpace[i1] = true;
                    occupied[i1] = true;
                }
            }
            else
            {//οριζόντιο
                position = r.Next(0, 10) * 10;
                position += r.Next(1, 7);
                for (int i1 = position; i1 < position + 5; i1++)
                {
                    carrier.shipSpace[i1] = true;
                    occupied[i1] = true;

                }
            }
            //anti-torpido boat, 4 squares
            torpido = new Ships(4, "anti-torpido boat");
            orientation = r.Next(0, 2);
            if (orientation == 0)
            {//κάθετο
                do
                {
                    position = r.Next(1, 71);
                    test = false;
                    for (int i2 = position; i2 < position + 40; i2 += 10)
                    {
                        if (occupied[i2])
                            test = true;
                    }
                } while (test);
                for (int i3 = position; i3 < position + 40; i3 += 10)
                {
                    torpido.shipSpace[i3] = true;
                    occupied[i3] = true;
                }
            }
            else
            {//οριζόντιο
                do
                {
                    position = r.Next(0, 10) * 10;
                    position += r.Next(1, 8);
                    test = false;
                    for (int i4 = position; i4 < position + 4; i4++)
                    {
                        if (occupied[i4])
                            test = true;
                    }
                } while (test);
                for (int i4 = position; i4 < position + 4; i4++)
                {
                    torpido.shipSpace[i4] = true;
                    occupied[i4] = true;
                }
            }
            //warship, 3 squares
            warship = new Ships(3, "warship");
            orientation = r.Next(0, 2);
            if (orientation == 0)
            {//κάθετο
                do
                {
                    position = r.Next(1, 81);
                    test = false;
                    for (int i5 = position; i5 < position + 30; i5 += 10)
                    {
                        if (occupied[i5])
                            test = true;
                    }
                } while (test);
                for (int i5 = position; i5 < position + 30; i5 += 10)
                {
                    warship.shipSpace[i5] = true;
                    occupied[i5] = true;
                }
            }
            else
            {//οριζόντιο
                do
                {
                    position = r.Next(0, 10) * 10;
                    position += r.Next(1, 9);
                    test = false;
                    for (int i6 = position; i6 < position + 3; i6++)
                    {
                        if (occupied[i6])
                            test = true;
                    }
                } while (test);
                for (int i6 = position; i6 < position + 3; i6++)
                {
                    warship.shipSpace[i6] = true;
                    occupied[i6] = true;
                }
            }
            //submarine, 2 squares
            submarine = new Ships(2, "submarine");
            orientation = r.Next(0, 2);
            if (orientation == 0)
            {//κάθετο
                do
                {
                    position = r.Next(1, 91);
                    test = false;
                    for (int i7 = position; i7 < position + 20; i7 += 10)
                    {
                        if (occupied[i7])
                            test = true;
                    }
                } while (test);
                for (int i7 = position; i7 < position + 20; i7 += 10)
                {
                    submarine.shipSpace[i7] = true;
                    occupied[i7] = true;
                }
            }
            else
            {//οριζόντιο
                do
                {
                    position = r.Next(0, 10) * 10;
                    position += r.Next(1, 10);
                    test = false;
                    for (int i8 = position; i8 < position + 2; i8++)
                    {
                        if (occupied[i8])
                            test = true;
                    }
                } while (test);
                for (int i8 = position; i8 < position + 2; i8++)
                {
                    submarine.shipSpace[i8] = true;
                    occupied[i8] = true;
                }
            }
            if (showBoats)
            {
                for(int j = 1; j < 101; j++)
                {
                    if (occupied[j])
                    {
                        spaces[j].BackColor= Color.Navy;
                    }
                }
            }
        }
        public string HitBoatAt(int box, Navy opponent)
        {
            Ships target;
            bool destruction = false;
            if (carrier.shipSpace[box])
            {
                target = carrier;
            }
            else if (torpido.shipSpace[box])
            {
                target = torpido;
            }
            else if (warship.shipSpace[box])
            {
                target = warship;
            }
            else if (submarine.shipSpace[box])
            {
                target = submarine;
            }
            else
            {
                spaces[box].BackColor = Color.LightGreen;
                spaces[box].Text = "-";
                return pronoun + " shot missed...";
            }
            target.shipSpace[box] = false;
            destruction = target.DidShipSunk();
            spaces[box].BackColor = Color.Red;
            spaces[box].Text = "X";
            if (destruction)
            {
                return opponent.pronoun + " " + target.name + " was sunk!";
            }
            return opponent.pronoun + " " + target.name + " was hit!";
        }
        public bool NavyIsGone()
        {
            if(carrier.sunk && torpido.sunk && warship.sunk && submarine.sunk)
            {
                return true;
            }
            return false;
        }
    }
    public class Ships
    {
        private int size;
        public string name;
        public bool[] shipSpace;
        public bool sunk;

        public Ships(int x, string y)
        {
            size = x;
            name = y;
            shipSpace = new bool[101];
            sunk = false;
        }
        public bool DidShipSunk()
        {
            for (int i = 0; i < shipSpace.Length; i++)
            {
                if (shipSpace[i])
                {
                    return false;
                }
            }
            sunk = true;
            return true;
        }
    }
}