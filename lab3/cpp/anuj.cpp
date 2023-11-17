#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <fstream>
#include <sstream>
#include <map>
#include<math.h>

using namespace std;

class PhoneRecord {
private:
    string name;
    string organisation;
    vector<string> phoneNumbers;

public:
    // Constructor
    PhoneRecord(const string& n, const string& org, const vector<string>& numbers)
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
 long long pOWER(long long x,long long i)

{
    long long mul=1;
    for(int k=0;k<=i;k++)
{ 
    mul=mul*x;

};
return mul;

}

    // Add your own implementation for hashing
    long long computeHash(const string& str) {
    int l = str.size();
    int x = 263;
    int p = 1000000007;
    long long sum = 0;
    

    for (int i = 0; i < l; i++) {
        long long z=pOWER(x,i);
        sum = (sum + (str[i] * z) % p) ;
       
    }
     sum=sum%x;
    return sum; 
}

// Add your own implementation for adding a contact
   void addContact(const PhoneRecord* record) {
    if (record == nullptr) {
        cout << "Invalid contact record." << endl;
        return;
    }

    
    string Name = record->getName();
    istringstream iss(Name);
    vector<string> words;
    string word;
    while (iss >> word) {
        words.push_back(word);
    }

    for (const string& w : words) {
        int i = computeHash(w);

        if (hashTable[i] == nullptr) {
            // If the slot is empty, create a new record and assign it to the slot.
            HashTableRecord* temp = new HashTableRecord(i, record);

            hashTable[i] = temp;
            cout<< temp->getKey()<<endl;
        } else {
            // If the slot is occupied, find the last record in the linked list and add the new record to the end.
            HashTableRecord* temp = hashTable[i];
            while (temp->getNext() != nullptr) {
                temp = temp->getNext();
                
            }
            temp->setNext(new HashTableRecord(i, record));
        }
    }
}


    // Add your own implementation for deleting a contact
    bool deleteContact(const string* searchName);

    // Add your own implementation for fetching contacts
    vector<PhoneRecord*> fetchContacts(const string* query)
    {

    };

    // Add your own implementation for counting records pointing to a contact
    int countRecordsPointingTo(const PhoneRecord* record) const;

    // Add your own implementation for reading records from a file
    void readRecordsFromFile(const string filename)
    {
        
    ifstream fin;
    fin.open(filename, ios::in);
    string line;
    
    
    if (!fin.is_open())
    {
        cerr << "Error opening file." << std::endl;
        return;
    }
     

        
       while (getline(fin, line))
{
    stringstream s(line);
    string Name, first_Name, Second_Name, Surname, organisation, phone_number1, phone_number2;
    Surname="0";
    getline(s, Name, ',');
    
    stringstream S(Name);
    getline(S, first_Name, ' ');
    getline(S, Second_Name, ' ');
    getline(S, Surname, ',');
    
    vector<string> phone_num;
    getline(s, phone_number1, ',');
    phone_num.push_back(phone_number1);
    getline(s, phone_number2, ',');
    
    if(isdigit(phone_number2[0] ))
    {  phone_num.push_back(phone_number2);
       getline(s, organisation, ','); 
    }
    else
    {
         organisation=phone_number2;
         phone_number2="lol";
    }

    

    
     PhoneRecord temp1(Name,organisation,phone_num);
     PhoneBook phone;
     phone.addContact(&temp1);
     
              
    
//     PhoneRecord temp2(Second_Name,organisation,phone_num);
    
//    if(!isdigit(Surname[0]))
//    {
    
//      PhoneRecord temp3(Surname,organisation,phone_num);
    
//    }

    
}
    
};
};


int main() {
    PhoneBook phoneBook;
    phoneBook.readRecordsFromFile("D:/IIt jodhpu/IC/c++ And DSA/dsa revision/details.txt"); 
//    vector<PhoneRecord*> fetchedContacts = phoneBook.fetchContacts(new std::string("Rahul Kumar Mishra"));

   
   

    return 0;
}