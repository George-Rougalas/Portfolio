#include <iostream>
#include <random>
#include <functional>
using namespace std;

class LinearList{
private:
    int MaxSize;
    int *List;
    int length;
public:
    LinearList(int MaxListSize)
    {// Constructor για την λίστα L.
        MaxSize = MaxListSize;
        List = new int[MaxSize];
        length = 0;
    }
    //Deconstructor για την λίστα L.
    ~LinearList() {delete [] List;}
    // Add x στην λίστα L.
    void Add(int x)
    {// Αν δεν υπάρχει χώρος στη λίστα L δεν κάνει Add το x.
        if (length == MaxSize)
            cout << "List is full";
    // Αλλίως προσθέτει το x στη λίστα και αυξάνει το length της λίστας.
        else {
            List[length] = x;
            length++;
        }
    }
    // Πρόσβαση στο k'th στοιχείο της λίστας.
    int Export(int k){return List[k];}

    //Εμφανίζει τη λίστα L.
    void Peak(){
        cout << "[L]";
        for (int i = 0; i < length; i++)
            cout << "-(" << List[i] << ")";
    }
};

class Histogram{
private:
    int MaxSize;
    int *HistoTitle;
    int *HistoList;
    int length;
public:
    Histogram(int MaxListSize)
    {// Constructor για τη λίστα histogram
    // Δημιουργεί μία λίστα για τους αριθμούς που εμφανίζονται στην λίστα L και
    // μία λίστα για το σύνολο τον φορών που εμφανίζονται οι αριθμοί την λίστα L.
        MaxSize = MaxListSize;
        HistoTitle = new int[MaxSize];
        HistoList = new int[MaxSize];
        length = 0;
    }
    //Deconstructor για την histogram.
    ~Histogram() {
        delete [] HistoList;
        delete [] HistoTitle;
    }
    void Input(int x)
    {//Αν είναι η πρώτη εισαγωγή τότε εκτελείται αυτός ο κώδικας για αρχικοποίηση
        if (length == 0) {
            HistoTitle[0] = x;
            HistoList[0] = 1;
            length++;
        }
    //Αν δεν είναι η πρώτη εισαγωγή τότε:
        else{
            for (int i = 0; i < length; i++){
            //Αν ο αριθμός είναι ήδη στη λίστα τότε απλά αυξάνουμε την HistoList κατά 1 και κλείνουμε την συνάρτηση
                if (HistoTitle[i] == x) {
                    HistoList[i]++;
                    break;
                }
            //Αν υπάρχει αριθμός μεγαλύτερος του x τότε το προσθέτουμε στη λίστα αφού μετακινήσουμε
            //όλα τα στοιχεία της histogram, που αντιστοιχούν σε αριθμούς μεγαλύτερους του x, μπροστά
                else if (HistoTitle[i] > x){
                    for (int j = length - 1; j > i-1; j--) {
                        HistoTitle[j + 1] = HistoTitle[j];
                        HistoList[j + 1] = HistoList[j];
                    }
                    HistoTitle[i] = x;
                    HistoList[i] = 1;
                    length++;
                    break;
                }
            //Αν έχουμε φτάσει το τέλος της λίστας και δεν έχουμε εκτελέσει κάποια συνθήκη
            // τότε βάζουμε το x στο τέλος της λίστας
                else if (i == length - 1){
                    HistoTitle[i+1] = x;
                    HistoList[i+1] = 1;
                    length++;
                    break;
                }
            }
        }
    }
    //Εμφανίζει την histogram.
    void Show(){
        cout << "[histogram]";
        for (int i = 0; i < length; i++){
            cout << "=[(" << HistoTitle[i] << ")->(" << HistoList[i] << ")]";
        }
    }
};

int main() {
    //Παίρνουμε το μέγεθος της λίστας L.
    int Lsize;
    cout << "Input size of list 'L'" << endl;
    cin >> Lsize;
    //Αρχικοποιούμε την λίστα L
    LinearList x(Lsize);
    //και την γεμίζουμε με τυχαίους αριθμούς από το 0 εώς το 100
    default_random_engine generator;
    uniform_int_distribution<int> data_element_distribution(0, 100);
    int dice_roll;
    for (int i = 0; i < Lsize ; i++) {
        dice_roll = data_element_distribution(generator);
        x.Add(dice_roll);
    }
    //Αρχικοποιούμε την histogram και της εισχωρούμε τα στοιχεία της λίστας L
    Histogram y(Lsize);
    for (int i = 0; i < Lsize; i++)
        y.Input(x.Export(i));
    //Εμφανίζουμε τα αποτελέσματα
    x.Peak();
    cout << "\n\n";
    y.Show();
    return 0;
}