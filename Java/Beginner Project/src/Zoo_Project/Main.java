package Zoo_Project;

import Zoo_Project.Zoo;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String text_file;//this is used to take a copy of Animals.txt for Reading and Editing
        int selected_item;//this is used to hold the position of the animal the user searches for
        File AniRead = new File("Animals.txt");
        Scanner screen = new Scanner(System.in);
        int choice;// the "choice" variable and the "screen" object are used to take input from the user
        do {
            System.out.println("Select a function:\n(1)Show the animals in the zoo\n(2)Add an animal to the zoo\n(3)Search for an animal by Name \n(4)Search for an animal by Code");
            choice = screen.nextInt();
            switch (choice) {//I use "switch" instead of "if" to make the code look more clear with less "{}"
                case 1://Προβολή όλων των διαθέσιμων ζώων του ζωολογικού κήπου
                    try {//here I try to read the contents of Animals.txt into "text_file"
                        Scanner FileReader = new Scanner(AniRead);
                        text_file = "";
                        while (FileReader.hasNextLine())//this makes a copy of Animals.txt on "text_file"
                            text_file = text_file + FileReader.nextLine() + "\n";
                        FileReader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("An error occurred.");
                        e.printStackTrace();
                        break;
                    }
                    Zoo.Show_Animals(text_file);//if the try{...} executes i call the "Show_Animals" method
                    break;
                case 2://Προσθήκη νέου ζώου
                    try {
                        FileWriter AniWrite = new FileWriter("Animals.txt", true);//"true" ensures that nothing in the document is overwritten
                        AniWrite.write(Zoo.Add_Animal());
                        AniWrite.close();
                        System.out.println("Animal was successfully added to the list.");
                    } catch (IOException e) {
                        System.out.println("An error occurred.");
                        e.printStackTrace();
                    }
                    break;
                case 3://searching by name or by code requires a lot of the same code, so I put them together here
                case 4:
                    try {
                        Scanner FileReader = new Scanner(AniRead);
                        text_file = "";
                        while (FileReader.hasNextLine())//this makes a copy of Animals.txt on "text_file"
                            text_file = text_file + FileReader.nextLine() + "\n";
                        FileReader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("An error occurred.");
                        e.printStackTrace();
                        break;
                    }
                    if (text_file.equals("")){//here it checks that the document is not empty and stops the search if it is
                        System.out.println("There are no animals in the zoo");
                        break;
                    }
                    else if (choice == 3)//here is the one line of code that needs to change depending on what you want to search
                        selected_item = Zoo.Search_Name(text_file);
                    else
                        selected_item = Zoo.Search_Code(text_file);
                    System.out.println("would you like to Edit(1) or Delete(0) ?");
                    choice = screen.nextInt();
                    if (choice == 0) {//this is the code for deleting the animal
                        try {
                            FileWriter AniWrite = new FileWriter("Animals.txt");//this "Filewriter" object will not append, meaning it will replace the text of the document
                            AniWrite.write(Zoo.Delete_Animal(selected_item, text_file));//replaces the contents of Animals.txt with the copy
                            AniWrite.close();
                            System.out.println("Animal was deleted from the list.");
                        } catch (IOException e) {
                            System.out.println("An error occurred.");
                            e.printStackTrace();
                        }
                    } else if (choice == 1) {//this is the code for editing the animal
                        try {
                            FileWriter AniWrite = new FileWriter("Animals.txt");//this "Filewriter" object will not append, meaning it will replace the text of the document
                            AniWrite.write(Zoo.Edit_Animal(selected_item, text_file));//replaces the contents of Animals.txt with the copy
                            AniWrite.close();
                            System.out.println("Successfully edited the list.");
                        } catch (IOException e) {
                            System.out.println("An error occurred.");
                            e.printStackTrace();
                        }
                    }
                    break;
            }
            System.out.println("Press '0' to finish, press any other number to continue:");
            choice = screen.nextInt();//checks whether the user wants to stop the program
        } while (choice != 0);
    }
}