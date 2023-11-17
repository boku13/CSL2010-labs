#include <bits/stdc++.h>
using namespace std;


class StudentRecord{
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

class Node{
	private:
		Node* next; 
		StudentRecord* element;
	public:
	    Node* get_next() {
	        return nullptr; 
	    }
	    StudentRecord* get_element() {
	        return nullptr; 
	    }
	    void set_next(Node* value){
	    	next = value;
	    }
	    void set_element(StudentRecord* student){
	    	element = student;
	    }
};

class Entity {
private:
    string name;
    Node* iterator;

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
    Node* head;
    Node* tail;

public:
    LinkedList(){
        head = nullptr;
        tail = nullptr;
    }
    
    void add_student(StudentRecord student){
        // Node nodeobj;
        // Node* newNode = &nodeobj;
        // StudentRecord* element = &student;
        // nodeobj.set_element(element);

        Node* newnode = new Node();
        StudentRecord* element = &student;
        newnode->set_element(element);
        
        if(head==nullptr){
            head = newnode;
            tail = newnode;
            set_iterator(head);
        }
        else{
            tail->set_next(newnode);
            tail = newnode;
        }
    }

    void delete_student(string studentName){

        if(head==nullptr){
            cout<<"List Empty."<<endl;
        }
        Node* temp = head;
        Node* temp_prev = head;
        StudentRecord* element = temp->get_element();
        while(temp->get_next() != NULL){
            if(element->get_studentName() != studentName){
                temp->set_next(temp->get_next());
                temp_prev->set_next(temp);
                break;
            }
            temp_prev->set_next(temp);
            temp->set_next(temp->get_next());
            element = temp->get_element();
        }

        //edge case to be considered.
        
        // if(temp->get_next()==NULL){
        //         ;
        //     }
    }
};

vector<StudentRecord> students;
vector<LinkedList> EntityArray;

void read_input_file(string file_path){
    ifstream file{ file_path };

    string line;
    string word;
    vector<vector<string>> content;
    vector<string> row;

    while(getline(file, line)){
        stringstream str(line);
        while(getline(str, word, ',')){
            row.push_back(word);
        }
        content.push_back(row);
    }
    
    for(int i = 0; i<content.size(); i++){
            // cout<<content[i][j]<<endl;
            StudentRecord studentrecord;
            studentrecord.set_studentName(content[i][0]);
            studentrecord.set_rollNumber(content[i][1]);
            students.push_back(studentrecord);        

        for(int j = 2; j < content[i].size(); j++){
            string s = content[i][j];
            string temp;
            string entity_name;
            remove_copy(s.begin(), s.end(), back_inserter(temp), '[');
            remove_copy(temp.begin(), temp.end(), back_inserter(entity_name), ']');
            // cout<<s<<endl;
            for (auto i : EntityArray) {
            if (i.get_name() == entity_name) {
                i.add_student(studentrecord);
                break;
            }
            else{
                LinkedList entity;
                entity.add_student(studentrecord);
                EntityArray.push_back(entity);
            }
            }
        }
    } 

    return;  
}

