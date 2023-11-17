#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <fstream>
#include <sstream>
#include <map>
#include <math.h>
using namespace std;

class PhoneRecord {
private:
    string name;
    string organisation;
    vector<string> phoneNumbers;

public:
    // Constructor
    PhoneRecord(const string& n, const string& org, const vector<string> &numbers)
        : name(n), organisation(org), phoneNumbers(numbers) {}

    // Getter methods
    string getName() const 
    {
        return name;
    }

    string getOrganisation() const 
    {
        return organisation;
    }

    vector<string> getPhoneNumbers() const 
    {
        return phoneNumbers;
    }
};

class HashTableRecord {
private:
    int key;
    PhoneRecord* element; // Pointer to PhoneRecord
    HashTableRecord* next;

public:
    // Constructor
    HashTableRecord(int k, PhoneRecord* rec)
        : key(k), element(rec), next(nullptr) {}

    // Getter methods
    int getKey() const 
    {
        return key;
    }

    PhoneRecord* getRecord() const 
    {
        return element;
    }

    HashTableRecord* getNext() const {
        return next;
    }

    void setNext(HashTableRecord* nxt) {
        next = nxt;
    }
};

class PhoneBook {
private:
    static const int HASH_TABLE_SIZE = 263;
    HashTableRecord* hashTable[HASH_TABLE_SIZE];

public:
    // Constructor
    PhoneBook() {
        for (int i = 0; i < HASH_TABLE_SIZE; ++i) 
        {
            hashTable[i] = nullptr;
        }
    }

    // Add your own implementation for hashing
    long long computeHash(const string& str)
    {
        int hash=0; 
        int hashfinal=0;
        
        for(int i=0; i<str.length(); i++)
        {
        	int d= int(str[i]);
            
        	hash= hash + ((d*((int)pow(263,i)))%1000000007);
            cout<<i<<":"<<hash<<endl;
		}
		hashfinal= hash%263;
		return abs(hashfinal);
	}
    

    // Add your own implementation for adding a contact
    void addContact(const PhoneRecord* record)
    {
	string str=record->getName();
 	string s;
    stringstream ss(str);
    // declaring vector to store the string after split
    vector<string> v;
    while (getline(ss, s, ' '))
	{
       v.push_back(s);
    }
   
    HashTableRecord *head=NULL;

    for(int i=0; i<v.size(); i++){
     int h= (int)computeHash(v[i]);
    	HashTableRecord *h1= new HashTableRecord(h, (PhoneRecord*)record);
	    if(hashTable)
        {
        h1->setNext(hashTable[h]);
        hashTable[h]= h1;
        }
    }
	}

    // Add your own implementation for deleting a contact
    bool deleteContact(const string* searchName)
    {
    int deleted = 0;
    vector<PhoneRecord*> d = fetchContacts(searchName);
        string word;
        stringstream ss(*searchName);
        while(getline(ss, word, ' ')){
            int key = computeHash(word);
            HashTableRecord* head = hashTable[key];
            HashTableRecord* prev = NULL;
            while(head!=NULL){
                if(head->getRecord() == d[0]){
                    if(prev==NULL){
                        hashTable[key] = head->getNext();
                        delete head;
                        deleted++;
                    }
                    else{
                        prev->setNext(head->getNext());
                        delete head;
                        deleted++;
                    }
                }
                prev = head;
                head = head->getNext();
            }
        }
        if(deleted>0){
            return true;
        }
        else
        {
            return false;
        }
    }

    // Add your own implementation for fetching contacts
    vector<PhoneRecord*> fetchContacts(const string* query)
    {
        vector<PhoneRecord*> v;
        map<PhoneRecord*, int> freq;

        stringstream ss(*query); 
        string substring;

        while(getline(ss, substring, ' '))
        {
           
            int key = computeHash(substring);
            HashTableRecord* iter = hashTable[key];
            
            while(iter)
            {
                if(iter->getRecord()->getName().find(substring) != string :: npos)
                {
                    if(freq.find(iter->getRecord()) !=freq.end())
                    {
                        freq[iter->getRecord()]++;
                    }
                    else freq[iter->getRecord()] = 1;
                }
                iter = iter->getNext();
            }
        }
        vector<pair<PhoneRecord*, int>> pairVector(freq.begin(), freq.end());
         sort(pairVector.begin(), pairVector.end(), [](const pair<PhoneRecord*, int> &a, const pair<PhoneRecord*, int> &b) 
         {
            return a.second > b.second;
        }); 
        for(auto &i: pairVector)
        {
            v.push_back(i.first);
        }
        return v;
    }

    // Add your own implementation for counting records pointing to a contact
    int countRecordsPointingTo(const PhoneRecord* record) 
    {
        int count = 0;
        stringstream ss(record->getName());
        string substring;
        while(getline(ss, substring, ' '))
        {
            int key = computeHash(substring);

            HashTableRecord* head = hashTable[key];
            while(head!=NULL && head->getRecord() != record)
            {
                head = head->getNext();
            }
            if(head)
            {
                count++;
            }
        }
        return count;
    }

    // Add your own implementation for reading records from a file
    void readRecordsFromFile(const string &filename)
    {
    ifstream file{filename};
    string line;
    vector<string> row;
     while (getline(file, line)) 
    {
        row.clear();
        stringstream ss(line);
        string word;
        while (getline(ss, word, ',')) 
        {
    
            row.push_back(word);
        }
        vector<string> numbers;
        for(int i=1; i<row.size()-1; i++)
        {
            numbers.push_back(row[i]);
        }

        PhoneRecord *ph = new PhoneRecord(row[0], row[row.size()-1], numbers);
        addContact(ph); 

        //ph.getName()= row[0];
        //ph.getOrganisation()=row[1];

    }
    }

    // Destructor
    ~PhoneBook()
    {
        for (int i = 0; i < HASH_TABLE_SIZE; ++i) 
        {
            HashTableRecord* current = hashTable[i];
            while (current!=NULL) {
                HashTableRecord* temp = current;
                current = current->getNext();
                delete temp;
            }
    }
    }
};
