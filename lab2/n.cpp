// #include <bits/stdc++.h>
// #include <iostream>
// #include <fstream>
// #include <vector>
// #include <sstream>
// #include <algorithm>

// using namespace std;

// class StudentRecord {
// private:
//     string studentName;
//     string rollNumber;

// public:
//     string get_studentName() {
//         return studentName;
//     }
//     void set_studentName(string Name) {
//         studentName = Name;
//     }
//     string get_rollNumber() {
//         return rollNumber;
//     }
//     void set_rollNumber(string rollnum) {
//         rollNumber = rollnum;
//     }
// };

// class Node {
// private:
//     Node* next;
//     StudentRecord *element;

// public:
//     Node() {
//         next = NULL;
//     }
//     Node* get_next() {
//         return next;
//     }
//     StudentRecord* get_element() {
//         return element;
//     }

//     void set_next(Node* value) {
//         next = value;
//     }
//     void set_element(StudentRecord *student) {
//         element = student;
//     }
// };

// class Entity {
// private:
//     string name;
//     Node* iterator = NULL;

// public:
//     string get_name() {
//         return name;
//     }
//     void set_name(string Name) {
//         name = Name;
//     }
//     Node* get_iterator() {
//         return iterator;
//     }
//     void set_iterator(Node* iter) {
//         iterator = iter;
//     }
// };

// class LinkedList : public Entity {
// public:
//     Node* head = NULL;
//     Node* tail = NULL;

//     LinkedList() 
//     {
//         //handling test case construction. 
//     }

//     LinkedList(string n) 
//     {
//         set_name(n);
//     }

//     void add_student(StudentRecord &student) 
//     {
//         Node* n = new Node;
//         StudentRecord* pass = &student;
//         n->set_element(pass);
//         if (head == NULL) 
//         {
//             head = n;
//             tail = head;
//             set_iterator(head);
//         }
//         else 
//         {
//             tail->set_next(n);
//             tail = tail->get_next();
//         }
//     }

//     void delete_student(string studentName) 
//     {
//         Node* temp = this->get_iterator();
//         if (temp->get_element()->get_studentName() == studentName) 
//         {
//             this->set_iterator(temp->get_next());
//             return;
//         }
//         while (temp->get_next() != NULL) 
//         {
//             if (temp->get_next()->get_element()->get_studentName() == studentName) 
//             {
//                 Node* t1 = temp->get_next()->get_next();
//                 temp->set_next(t1);
//                 break;
//             }
//             temp = temp->get_next();
//         }
//     }
// };

// vector<StudentRecord> students;
// vector<LinkedList> EntityArray;

// void read_input_file(string file_path) 
// {
//     ifstream file{file_path};
//     string line;
//     vector<string> row;
//     LinkedList cse("CSE"), ai("AI"), ee("EE"), es("ES"), dsa("DSA"), prml("PRML"), sna("SNA"), maths("Maths"), g1("G1"), g2("G2"), g3("G3"), g4("G4"), g5("G5"), g6("G6"), music("Music"), prog("Programming"), robo("Robotics"), toast("Toastmasters"), dance("Dance");

//     while (getline(file, line)) 
//     {
//         row.clear();
//         stringstream ss(line);
//         string word;
//         while (getline(ss, word, ',')) 
//         {
//             string temp;
//             string processed_word;
//              remove_copy(word.begin(), word.end(), back_inserter(temp), '[');
//              remove_copy(temp.begin(), temp.end(), back_inserter(processed_word), ']');
//             row.push_back(processed_word);
//         }
//         StudentRecord *s = new StudentRecord;
//         s->set_rollNumber(row[1]);
//         s->set_studentName(row[0]);
//         students.push_back(*s);

//         vector<LinkedList*> entities = {&cse, &ai, &ee, &es, &dsa, &prml, &sna, &maths, &g1, &g2, &g3, &g4, &g5, &g6, &music, &prog, &robo, &toast, &dance};

//         for (LinkedList* entity : entities) 
//         {
//             if (find(row.begin(), row.end(), entity->get_name()) != row.end()) 
//             {
//                 entity->add_student(*s);
//             }
//         }
//     }
//     EntityArray = {cse, ai, ee, es, dsa, prml, sna, maths, g1, g2, g3, g4, g5, g6, music, prog, robo, toast, dance};
// }

#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

class StudentRecord {
private:
    string studentName;
    string rollNumber;

public:
    string get_studentName() {
        return studentName;
    }
    void set_studentName(string Name) {
        studentName = Name;
    }
    string get_rollNumber() {
        return rollNumber;
    }
    void set_rollNumber(string rollnum) {
        rollNumber = rollnum;
    }
};

class Node {
private:
    Node *next;
    StudentRecord *element;

public:
    Node() {
        next = NULL;
    }
    Node* get_next() {
        return next;
    }
    StudentRecord* get_element() {
        return element;
    }

    void set_next(Node* value) {
        next = value;
    }
    void set_element(StudentRecord *student) {
        element = student;
    }
};

class Entity {
private:
    string name;
    Node* iterator = NULL;

public:
    string get_name() {
        return name;
    }
    void set_name(string Name) {
        name = Name;
    }
    Node* get_iterator() {
        return iterator;
    }
    void set_iterator(Node* iter) {
        iterator = iter;
    }
};

class LinkedList : public Entity {
public:
    Node* head = NULL;
    Node* tail = NULL;

    LinkedList() 
    {
        //handling test case construction. 
    }

    LinkedList(string n) 
    {
        set_name(n);
    }

    void add_student(StudentRecord &student) 
    {
        Node* n1=new Node;
        StudentRecord* pass=&student;
        n1->set_element(pass);
        if (head==NULL) 
        {
            head=n1;
            tail=head;
            set_iterator(head);
        }
        else 
        {
            tail->set_next(n1);
            tail=tail->get_next();
        }
    }

    void delete_student(string studentName) 
    {
        Node* temp = this->get_iterator();
        if (temp->get_element()->get_studentName()==studentName) 
        {
            this->set_iterator(temp->get_next());
            return;
        }
        while (temp->get_next() != NULL) 
        {
            if (temp->get_next()->get_element()->get_studentName()==studentName) 
            {
                Node* t1 = temp->get_next()->get_next();
                temp->set_next(t1);
                break;
            }
            temp = temp->get_next();
        }
    }
};

vector<StudentRecord> students;
vector<LinkedList> EntityArray;

void read_input_file(string file_path) 
{
    ifstream file{file_path};
    string line;
    vector<string> row;
    LinkedList cse("CSE"), ai("AI"), ee("EE"), es("ES"), dsa("DSA"), prml("PRML"), sna("SNA"), maths("Maths"), g1("G1"), g2("G2"), g3("G3"), g4("G4"), g5("G5"), g6("G6"), music("Music"), prog("Programming"), robo("Robotics"), toast("Toastmasters"), dance("Dance");

    while (getline(file, line)) 
    {
        row.clear();
        stringstream ss(line);
        string word;
        while (getline(ss, word, ',')) 
        {
            string temp;
            string processed_word;
             remove_copy(word.begin(), word.end(), back_inserter(temp), '[');
             remove_copy(temp.begin(), temp.end(), back_inserter(processed_word), ']');
            row.push_back(processed_word);
        }
        StudentRecord *s=new StudentRecord;
        s->set_rollNumber(row[1]);
        s->set_studentName(row[0]);
        students.push_back(*s);

        vector<LinkedList*> entities = {&cse, &ai, &ee, &es, &dsa, &prml, &sna, &maths, &g1, &g2, &g3, &g4, &g5, &g6, &music, &prog, &robo, &toast, &dance};

        for (LinkedList* entity : entities) 
        {
            if (find(row.begin(), row.end(), entity->get_name()) != row.end()) 
            {
                entity->add_student(*s);
            }
        }
    }
    EntityArray = {cse, ai, ee, es, dsa, prml, sna, maths, g1, g2, g3, g4, g5, g6, music, prog, robo, toast, dance};
}