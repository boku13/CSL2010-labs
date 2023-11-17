#include <bits/stdc++.h>
using namespace std;

class StudentRecord
{
private:
    string studentName;
    string rollNumber;

public:
    string get_studentName()
    {
        return studentName;
    }
    void set_studentName(string Name)
    {
        studentName = Name;
    }
    string get_rollNumber()
    {
        return rollNumber;
    }
    void set_rollNumber(string rollnum)
    {
        rollNumber = rollnum;
    }
};

class Node
{
private:
    Node *next;
    StudentRecord *element;

public:
    Node *get_next()
    {
        return next;
    }
    StudentRecord *get_element()
    {
        return element;
    }

    void set_next(Node *value)
    {
        next = value;
    }
    void set_element(StudentRecord *student)
    {
        element = student;
    }
};

class Entity
{
private:
    string name;
    Node *iterator;

public:
    string get_name()
    {
        return name;
    }
    void set_name(string Name)
    {
        name = Name;
    }
    Node *get_iterator()
    {
        return iterator;
    }
    void set_iterator(Node *iter)
    {
        iterator = iter;
    }
};

class LinkedList : public Entity
{
public:
    void add_student(StudentRecord student)
    {
        Node *head = get_iterator();
        bool mask = false;

        while (head != NULL)
        {
            if (head->get_element()->get_rollNumber() == student.get_rollNumber())
            {
                mask = true;
                break;
            }
            head = head->get_next();
        }

        if (!mask)
        {
            Node *newNode = new Node;
            StudentRecord *studentCopy = new StudentRecord;
            *studentCopy = student;

            newNode->set_element(studentCopy);
            newNode->set_next(NULL);

            if (get_iterator() != NULL)
            {
                newNode->set_next(get_iterator());
                set_iterator(newNode);
            }
            else
            {
                set_iterator(newNode);
            }
        }
    }
    void delete_student(string studentName)
    {
        int n = 1;
        Node *currentNode = get_iterator();
        bool found = false;

        while (currentNode != NULL)
        {
            if (currentNode->get_element()->get_studentName() == studentName)
            {
                found = true;
                break;
            }
            currentNode = currentNode->get_next();
            n++;
        }

        if (found)
        {
            if (n == 1)
            {
                set_iterator(currentNode->get_next());
                return;
            }
            currentNode = currentNode->get_next();
            Node *previousNode = get_iterator();
            for (int i = 0; i < n   - 2; i++)
            {
                previousNode = previousNode->get_next();
            }
            previousNode->set_next(currentNode);
        }
    }
};
vector<StudentRecord> students;
vector<LinkedList> EntityArray;
vector<string> myEntityList;

void read_input_file(string file_path)
{

    fstream fin;
    fin.open(file_path, ios::in);
    string line;
    while (getline(fin, line))
    {
        myEntityList.clear();
        stringstream s(line);
        string Name, rollNumber;
        getline(s, Name, ',');
        getline(s, rollNumber, ',');
        StudentRecord S1;
        S1.set_studentName(Name);
        S1.set_rollNumber(rollNumber);
        int if_exists = 0;
        for (int j = 0; j < students.size(); j++)
        {
            if (students[j].get_rollNumber() == S1.get_rollNumber())
            {
                if_exists = 1;
            }
        }
        if (!if_exists)
        {
            students.push_back(S1);
        }
        // department
        string department;
        getline(s, department, ',');
        myEntityList.push_back(department);

        // courses
        string temp;
        while (getline(s, temp, ','))
        {
            if (temp.front() == '[')
            {
                temp.erase(0, 1);
                myEntityList.push_back(temp);
            }
            else if (temp.back() == ']')
            {
                temp.pop_back();
                myEntityList.push_back(temp);
                break;
            }
            else
            {
                myEntityList.push_back(temp);
            }
        }

        // hostel
        string hostel;
        getline(s, hostel, ',');
        myEntityList.push_back(hostel);

        // clubs
        while (getline(s, temp, ','))
        {
            if (temp.front() == '[' && temp.back() == ']')
            {
                temp.erase(0, 1);
                temp.pop_back();
                myEntityList.push_back(temp);
                break;
            }
            if (temp.front() == '[')
            {
                temp.erase(0, 1);
                myEntityList.push_back(temp);
            }
            if (temp.back() == ']')
            {
                temp.pop_back();
                myEntityList.push_back(temp);
                break;
            }
            else
            {
                myEntityList.push_back(temp);
            }
        }
        // for(int s=0;s<myEntityList.size();s++){
        //     cout << myEntityList[s] << " " ;
        // }
        // cout << endl << "iteration over" << endl;
        for (int i = 0; i < myEntityList.size(); i++)
        {
            int flag = 1;
            int m;
            for (m = 0; m < EntityArray.size(); m++)
            {
                if (EntityArray[m].get_name() == myEntityList[i])
                {
                    EntityArray[m].add_student(S1);
                    flag = 0;
                    break;
                }
            }
            if (flag)
            {
                LinkedList list1;
                list1.set_name(myEntityList[i]);
                list1.set_iterator(NULL);
                EntityArray.push_back(list1);
                EntityArray[EntityArray.size() - 1].add_student(S1);
            }
        }
        // for(int s=0;s<EntityArray.size();s++){
        //     cout << EntityArray[s].get_name() << " " ;
        // }
        // cout << endl << "iteration over" << endl;
    }
    fin.close();
}