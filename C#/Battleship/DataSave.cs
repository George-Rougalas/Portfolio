using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    internal class DataSave
    {
        int win;
        int lose;
        int time;
        String connectionString = "Data source=thema1.db;Version=3";
        SQLiteConnection connection;

        public int Win
        {
            get { return win; }
            set { win = value; }
        }

        public int Lose
        {
            get { return lose; }
            set { lose = value; }
        }

        public int Time
        {
            get { return time; }
            set { time = value; }
        }


        public void Create()
        {
            connection = new SQLiteConnection(connectionString);
            connection.Open();
            String createSQL = "Create table if not exists Battle(User_ID integer primary key autoincrement," +
                "Win integer,Lose integer,Time integer)";
            SQLiteCommand command = new SQLiteCommand(createSQL, connection);
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Insert(int win, int lose, int time)
        {
            connection = new SQLiteConnection(connectionString);
            connection.Open();
            String insertSQL = "Insert into Battle(Win,Lose,Time) values('" + win + "','" + lose + "','" + time + "')";
            SQLiteCommand command = new SQLiteCommand(insertSQL, connection);
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Sum(ref int wins,ref int loses, ref int averageTime, ref int bestTime)
        {
            connection = new SQLiteConnection(connectionString);
            connection.Open();
            String selectSQL = "Select * from Battle";
            SQLiteCommand command = new SQLiteCommand(selectSQL, connection);
            SQLiteDataReader reader = command.ExecuteReader();
            //int wins = 0;
            //int loses = 0;
            int i = 0;
            while (reader.Read())
            {
                wins+= reader.GetInt32(1);
                loses+=reader.GetInt32(2);
                averageTime+=reader.GetInt32(3);
                if (i == 0)
                {
                    bestTime=reader.GetInt32(3);
                }
                else
                {
                    if (bestTime > reader.GetInt32(3))
                    {
                        bestTime = reader.GetInt32(3);
                    }
                }
                i++;
            }
            if (i != 0)
            {
                averageTime = averageTime / i;

            }
            //averageTime =averageTime/i;
        }

    }
}
