using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Media;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.AxHost;

namespace Aaaingment_1
{
    public partial class Form2 : Form
    {
        List<PictureBox> bullets = new List<PictureBox>();
        List<PictureBox> bombs = new List<PictureBox>();
        Random r;
        SoundPlayer s, s1;
        int enemyLoc = 448;//this variable holds the X coordinates of the enemy's next location
        int game_time = 60;//the game's time 
        int game_score = 0;//the game's score
        public Form2()
        {
            InitializeComponent();
        }
        private void Form2_Load(object sender, EventArgs e)
        {
            r = new Random();
            s = new SoundPlayer("Images/laser_shot.wav");//player sound
            s1 = new SoundPlayer("Images/cannon.wav");//enemy sound
        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //accidently made this, can't remove it
        }
        private void pictureBox2_Click(object sender, EventArgs e)
        {
            //accidently made this, can't remove it
        }
        private void Form2_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode.ToString().Equals("Left") && pictureBox1.Location.X > 1)
            {
                pictureBox1.Location = new Point(pictureBox1.Location.X - 20, pictureBox1.Location.Y);
            }
            else if (e.KeyCode.ToString().Equals("Right") && pictureBox1.Location.X < 801)
            {
                pictureBox1.Location = new Point(pictureBox1.Location.X + 20, pictureBox1.Location.Y);
            }
            else if (e.KeyCode.ToString().Equals("Up") && pictureBox1.Location.Y > 175)
            {
                pictureBox1.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y - 20);
            }
            else if (e.KeyCode.ToString().Equals("Down") && pictureBox1.Location.Y < 500)
            {
                pictureBox1.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + 20);
            }
            else if (e.KeyCode.ToString().Equals("Space"))
            {
                createBullet(pictureBox1.Location.X);
                if(label5.Text == "Press [SPACE] to start")
                    timer2.Enabled = true;//this starts the game, only for the fisrt press of [SPACE]
                label5.Text = "";
            }
        }
        private void createBullet(int startX)
        {
            PictureBox p = new PictureBox();
            p.ImageLocation = "Images/Bullet.png";
            p.Location = new Point(startX + 5, pictureBox1.Location.Y - 50);
            p.Size = new Size(50, 60);
            p.SizeMode = PictureBoxSizeMode.StretchImage;
            Controls.Add(p);
            bullets.Add(p);
            s.Play();
        }    
        private void timer1_Tick(object sender, EventArgs e)
        {
            foreach (PictureBox p in bullets)
            {
                if (p.ImageLocation == "Images/BAM.png")
                {//if the missile exploded, it is removed from the game
                    p.Hide();
                }
                else if (p.Location.Y < 125 && p.Location.Y > 0 && p.Location.X - 25 < pictureBox2.Location.X && pictureBox2.Location.X < p.Location.X + 25)
                {//detonates the missile and adds 10 points, if it hits the enemy
                    p.ImageLocation = "Images/BAM.png";
                    ChangeScore(10);
                }
                else
                {//moves the missile up
                    p.Location = new Point(p.Location.X, p.Location.Y - 10);
                }
            }
            if (enemyLoc > pictureBox2.Location.X)
            {//moves the enemy towards itsnext location
                pictureBox2.Location = new Point(pictureBox2.Location.X + 7, pictureBox2.Location.Y);
            }
            else if(enemyLoc < pictureBox1.Location.X)
            {//moves the enemy towards its next location
                pictureBox2.Location = new Point(pictureBox2.Location.X - 7, pictureBox2.Location.Y);
            }
            foreach (PictureBox b in bombs)
            {
                if (b.ImageLocation == "Images/BAM.png")
                {//if the bomb exploded, it is removed from the game
                    b.Hide();
                }
                else if (b.Location.Y > pictureBox1.Location.Y)
                {//if the bomb is at the same Y axis as the player it detonates
                    DetonateBomb(b);
                }
                else
                {//moves the bomb up
                    b.Location = new Point(b.Location.X, b.Location.Y + 5);

                }
            }
        }
        private void timer2_Tick(object sender, EventArgs e)
        {
            label1.Text = game_time--.ToString();//time goes down
            if (enemyLoc - 25 < pictureBox2.Location.X && pictureBox2.Location.X < enemyLoc + 25)
            {// if the enemy reached its next location it chooses anw location and throws a bomb
                enemyLoc = r.Next(Width - pictureBox2.Width);
                ThrowBomb(pictureBox2.Location.X);
            }
            if (game_time == -1)
            {//when the game is over
                button1.Show();
                button1.Width = 245;
                button1.Height = 56;
                label5.Text = "Time Is Over!!!";
                SaveScore();
                timer1.Enabled = false;
                timer2.Enabled = false;
            }
        }
        private void ChangeScore(int change)
        {//changes the score, never bellow 0
            game_score = game_score + change;
            if (game_score < 0) { game_score = 0; }
            label3.Text = game_score.ToString();
        }
        private void ThrowBomb(int start)
        {//makes a bomb
            PictureBox b = new PictureBox();
            b.ImageLocation = "Images/bomb.png";
            b.Location = new Point(start + 5, pictureBox2.Location.Y + 120);
            b.Size = new Size(45, 45);
            b.SizeMode = PictureBoxSizeMode.StretchImage;
            Controls.Add(b);
            bombs.Add(b);
            s1.Play();
        }
        private void DetonateBomb(PictureBox bomb)
        {//here the picturebox is edited to become an explosion
            bomb.Location = new Point(bomb.Location.X - 75, bomb.Location.Y - 75);//the location changes to adjust to the explosions bigger size
            bomb.ImageLocation = "Images/BAM.png";
            bomb.Size = new Size(200, 200);
            int startX = pictureBox1.Location.X;   //these will give the area covered by the spaceship
            int endX = startX + pictureBox1.Size.Width;
            int startY = pictureBox1.Location.Y;
            int endY = startY + pictureBox1.Size.Height;
            if (  ((bomb.Location.X < startX && startX < bomb.Location.X + 200) || (bomb.Location.X < endX && endX < bomb.Location.X + 200)) && ((bomb.Location.Y < startY && startY < bomb.Location.Y + 200) || (bomb.Location.Y < endY && endY < bomb.Location.Y + 200))  )
            {//this condition is True when the area of the spaceship and explosion overlap
                ChangeScore(-25);
            }
        }
        private void SaveScore()
        {       
            int score_size = 1;//at least one score(the current one)
            foreach (string line in System.IO.File.ReadLines("top_scores.txt"))
            {//score increases for every sore on the leaderboard
                score_size++;
            } 
            int[] score = new int[score_size];//int score holds all the scores
            int i= 0;
            foreach (string line in System.IO.File.ReadLines("top_scores.txt"))
            {//int score is given all the scores
                score[i++] = Int32.Parse(line);
            }
            score[i] = game_score;
            Array.Sort(score);// int score[] is sorted by ascending order
            string text = "";
            for(int j = i; j > -1; j--)
            {//here string text will be the contents we will put in top_scores.txt
                text = text + score[j] + Environment.NewLine;
                if (i == 10 && j == 1)//max 10
                    break;
            }
            File.WriteAllText("top_scores.txt", text);
        }
        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
