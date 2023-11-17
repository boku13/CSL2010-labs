#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <iterator>
#include <vector>
#include <string>
#include <assert.h>
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

vector<StudentRecord> students;

class Node{
	private:
		Node* next; 
		StudentRecord* element;
	public:
        
	    Node* get_next() {
	        return next; 
	    }
	    StudentRecord* get_element() {
	        return element; 
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
public:
    void add_student(StudentRecord &student){

        // students.push_back(student);

        Node* newnode = new Node;
        StudentRecord* newrecord = new StudentRecord;
        *newrecord = student;
        
        newnode->set_element(newrecord);
        newnode->set_next(NULL);
        
        if(head==nullptr){
            head = newnode;
        }
        else{
        Node* temp = head;
        while(temp->get_next() != nullptr){
            temp = temp->get_next();
        }
        temp->set_next(newnode);
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
                temp_prev->set_next(temp->get_next());
                break;
            }
            temp_prev = temp;
            temp = temp->get_next();
            element = temp->get_element();
        }

        //edge case to be considered.
        
        // if(temp->get_next()==NULL){
        //         ;
        //     }
    }

    void printLL(){
        while(head!=NULL){
            Node* node;
            string s = node->get_element()->get_studentName();
            cout<<s<<endl;
            head = head->get_next();
        }
    }

};

vector<LinkedList> EntityArray;

void read_input_file(string file_path){
    ifstream file{ file_path };

    if (!file.is_open()) {
        cerr << "Failed to open file." << endl;
    }

    string line;
    string word;
    vector<vector<string>> content;
    vector<string> row;

    while(getline(file, line)){
        stringstream str(line);
        row.clear();
        while(getline(str, word, ',')){
            string temp;
            string processed_word;
             remove_copy(word.begin(), word.end(), back_inserter(temp), '[');
             remove_copy(temp.begin(), temp.end(), back_inserter(processed_word), ']');
            row.push_back(processed_word);
        }
        content.push_back(row);
    }

    // for(auto row : content){
    //     for(auto element : row){
    //         cout<<element<<endl;
    //     }
    // }
    
    for(unsigned i = 0; i < content.size(); i++){
            StudentRecord studentrecord;
            studentrecord.set_studentName(content[i][0]);
            studentrecord.set_rollNumber(content[i][1]); 
            students.push_back(studentrecord);      

        // entity = ""
        // for entity_name in line[2:]:
        //     exists = 0
        //     for i in EntityArray:
        //         if i.name == entity_name:
        //             entity = i         
        //             exists = 1
        //             break
            
        //     if not exists:
        //         entity = LinkedList()
        //         entity.name = entity_name
            
        //     entity.add_student(student)
        //     EntityArray.append(entity)
        for(unsigned j = 2; j < content[i].size(); j++){
            string entity_name = content[i][j];
            bool exists = false;

            LinkedList i;
            for (auto& e : EntityArray) {
            if (e.get_name() == entity_name) {
                i = e;
                exists = true;
                break;
            }
            }
            if(!exists){
                LinkedList entity;
                entity.set_name(entity_name);
                entity.set_iterator(NULL);
                EntityArray.push_back(entity);
                EntityArray[EntityArray.size() - 1].add_student(studentrecord);
            }
        }
    } 
};

int main(){
    read_input_file("Details.txt");
    for(auto i : EntityArray){
        cout<<i.get_name()<<endl;
        i.printLL();
    }
    return 0;
}
