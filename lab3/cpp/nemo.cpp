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
    string getName() const {
        return name;
    }

    string getOrganisation() const {
        return organisation;
    }

    vector<string> getPhoneNumbers() const {
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
    int getKey() const {
        return key;
    }

    PhoneRecord* getRecord() const {
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
        for (int i = 0; i < HASH_TABLE_SIZE; ++i) {
            hashTable[i] = nullptr;
        }
    }

    // Add your own implementation for hashing
    long long computeHash(const string& str)
    {
    	 long long hash=0; 
        long long hashfinal=0;
        
        for(int i=0; i<str.length(); i++)
        {
        	char d= str[i];
            int d1= d;
        	hash= hash + ((d1*(pow(263,i)))%1000000007);
		}
		hashfinal= hash%263;
		return hashfinal;
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
    	HashTableRecord *h1= new HashTableRecord(h, &record);
	    if(head=NULL)
        {
        hashTable[i]=h1;
        }
    }
	}

    // Add your own implementation for deleting a contact
    bool deleteContact(const string* searchName)
    {

    }

    // Add your own implementation for fetching contacts
    vector<PhoneRecord*> fetchContacts(const string* query)
    {

    }

    // Add your own implementation for counting records pointing to a contact
    int countRecordsPointingTo(const PhoneRecord* record) const
    {

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
        const vector<string> numbers;
        for(int i=2; i<=row.size(); i++)
        {
            numbers.push_back(row[i]);
        }

        PhoneRecord ph = new PhoneRecord(&row[0], &row[1], &numbers);
        
        
        //ph.getName()= row[0];
        //ph.getOrganisation()=row[1];

        



    }

    // Destructor
    ~PhoneBook()
    {

    }
}
};

int main() {
    // Your test cases and program logic can go here.
    return 0;
}