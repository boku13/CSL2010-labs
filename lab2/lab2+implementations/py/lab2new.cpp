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
	    Node* set_next(Node* value){
	    	next = value;
	    }
	    StudentRecord* set_element(StudentRecord* student){
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
    // Implement LinkedList members here
    public:
        void add_student(StudentRecord student){

        }

        void delete_student(string studentName){
            
        }
};

void read_input_file(string file_path){


    return;        
}

vector<StudentRecord> students;
vector<LinkedList> EntityArray;

int main(){
    std::ifstream file{"Details.txt"};
    

    return 0;
    }