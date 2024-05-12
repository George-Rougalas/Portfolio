package Zoo_Project;
import java.util.Scanner;

public class Zoo {

    public static void Show_Animals(String document){//it takes a copy of Animals.txt as a parameter
        int Index = document.indexOf("code:");//it searches for the first instance of "code:" and saves its position in "Index"
        if (Index == -1)//if "code:" is not in the document that means the document is empty
            System.out.println("Zoo is empty");
        int Mid_ex, End_ex;//"Index", "Mid_ex" and "End_ex" will contain the Indexes needed to find the name and code of every animal
        String code,name;//these variables simply save the parts of the document we want to print in every loop
        System.out.println("The animals currently on the zoo are :");
        while (Index != -1){//this will loop until all animals in the document have been printed
            Mid_ex = document.indexOf("name:", Index);//"Mid_ex" saves the Index of "name:" of the animal that is going to be printed
            End_ex = document.indexOf("class:", Index);//"End_ex" saves the Index of "class:" of the animal that is going to be printed
            code = document.substring(Index + 5, Mid_ex - 1);// it uses the Indexes to find the specific line in the document and
            name = document.substring(Mid_ex + 5, End_ex - 1);// trim it to save on the variables (name,code) only what it has to print
            System.out.println("-" + name +"(" + code + ")");
            Index = document.indexOf("code:", Index + 1);//it looks for the next instance of "code:" and thus the animal that is going to be printed
        }//it stops the loop if it isn't found
    }

    public static String Add_Animal(){
        String NewAnimal = "";//"NewAnimal" will be returned after it contains
        Scanner user = new Scanner(System.in);
        System.out.println("Enter the code for the new animal");
        NewAnimal = NewAnimal + "code:" + user.nextLine() + "\n";
        System.out.println("Enter the animal's name");
        NewAnimal = NewAnimal + "name:" + user.nextLine() + "\n";
        System.out.println("Enter the animal's class");
        NewAnimal = NewAnimal + "class:" + user.nextLine() + "\n";
        System.out.println("Enter the animal's average weight");
        NewAnimal = NewAnimal + "weight:" + user.nextLine() + "\n";
        System.out.println("Enter the animal's average lifespan");
        NewAnimal = NewAnimal + "lifespan:" + user.nextLine() + "\n@\n";//"@" is added to signal the end of the animal's name
        return NewAnimal;//it returns "NewAnimal" to be added to Animals.txt
    }

    public static int Search_Name(String document) {
        Scanner user = new Scanner(System.in);
        System.out.println("Enter the name of what you are looking for:");
        String name = user.nextLine();//here the user inputs the name of the animal they're looking for
        int Index = document.indexOf("name:" + name + "\n");//if the name exists its position will be kept in this variable
        while (Index == -1){//if the name doesn't exist it will loop until it is given one that exists in the document
            System.out.println("name is not in the list, try again:");
            name = user.nextLine();
            Index = document.indexOf("name:" + name + "\n");
        }
        int Start = document.lastIndexOf("code:", Index);//"Start" holds the position of the string "code:" that belongs to the same animal as the requested name
        int End = document.indexOf("@", Index);//"End" holds the position of the end of the animal's data
        System.out.println("You have selected\n" + document.substring(Start, End-1));//this displays the animal's data to the user
        return Start;//returns the position of the start of the animal's data
    }

    public static int Search_Code(String document){
        Scanner user = new Scanner(System.in);
        System.out.println("Enter the code of what you are looking for:");
        String code = user.nextLine();//here the user inputs the dode of the animal they're looking for
        int Start = document.indexOf("code:" + code + "\n");//if the code exists its position will be kept in this variable
        while (Start == -1){//if the code doesn't exist it will loop until it is given one that exists in the document
            System.out.println("Code is not existent, try again:");
            code = user.nextLine();
            Start = document.indexOf("code:" + code + "\n");
        }
        int End = document.indexOf("@", Start);//"End" holds the position of the end of the animal's data
        System.out.println("You have selected\n" + document.substring(Start, End-1));//this displays the animal's data to the user
        return Start;//returns the position of the start of the animal's data
    }


    public static String Delete_Animal(int Start, String document) {//in the parameters are the document and the Start position of the string that has to be deleted
        int End = document.indexOf("@", Start);//"End" holds the end position of the string that has to be deleted
        String new_doc = document.substring(0, Start);//it makes a new string that has all the data up to the point of the "Start"
        new_doc = new_doc + document.substring(End + 2);//it also adds all the data after the point of "End"
        return new_doc;//and now it is a copy of the document without the data we wanted to delete
    }

    public static String Edit_Animal(int Start, String document) {
        String[] values = {"code:", "name:", "class:", "weight:", "lifespan:", "@"};
        //this array contains the common strings that are used to identify the data of every animal
        int[] value_position = {Start, 0, 0, 0, 0, 0};//this array WILL hold the positions the common strings above have within the "document"
        String new_doc = document.substring(0, Start);//it makes a new string that has all the data up to the point of the "Start"
        Scanner answer = new Scanner(System.in);
        int choice;// the "choice" variable and the "answer" object are used to take input from the user
        String temp;//temporary value that holds the user's edit
        for (int i = 0; i < 5; i++) {//in this loop the user edits the animal's data
            value_position[i+1] = document.indexOf(values[i+1], Start);//saves the position of the next data area
            String current_item = document.substring(value_position[i], value_position[i + 1]);
            //saves the data that can be edited in this loop, by taking the part of the string between two data areas
            System.out.println("Area " + (i+1) + " is " + current_item + "Press '1' to change it, press any other number to continue:");
            choice = answer.nextInt();
            if (choice == 1) {//if the user wants to edit
                System.out.println("Input the new " + values[i]);
                temp = answer.next();//the data they want to edit is stored here
                new_doc = new_doc + values[i] + temp + "\n";//and it is added to "new_doc" with the matching data type
            } else {//if the user does not want to edit
                new_doc = new_doc + current_item;//simply adds the data into "new_doc"
            }
        }
        new_doc = new_doc + document.substring(value_position[5]);//adds to "new_doc" all the data after the data that was edited
        return new_doc;//returns an edited copy of the document
    }
}