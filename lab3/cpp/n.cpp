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

    // Add your own implementation for hashing
    long long computeHash(const string& str){
        int ans = 0, pow = 1;
        for(char ch: str){
            ans += ((int(ch) * pow) % 1000000007);
            pow *= 263;
        }
        return abs(ans%263);
    }

    // Add your own implementation for adding a contact
    void addContact(PhoneRecord* record){
        // firstly, separating each word from the name of the given record
        stringstream ss(record->getName());     
        string substring;
        while(getline(ss, substring, ' ')){
            // computing hash value first then adding record to that particular key(hash value)
            int key = computeHash(substring);   
            HashTableRecord* newRecord = new HashTableRecord(key, record);
            if(hashTable) newRecord->setNext(hashTable[key]);
            hashTable[key] = newRecord;
        }
    }

    // Add your own implementation for fetching contacts
    vector<PhoneRecord*> fetchContacts(const string* query){
        // creating map to keep count of every phone record
        vector<PhoneRecord*> ans;
        map<PhoneRecord*, int> countFrequency;

        stringstream ss(*query);  // separating each word from the given string
        string substring;

        while(getline(ss, substring, ' ')){
            // firstly computing hash value
            int key = computeHash(substring);
            HashTableRecord* iter = hashTable[key];
            // then iterating over the whole linked list to get every record whose name contain that particular word
            // as well as keeping count of that record because it can come in any hash value (as there are many hashtableRecord 
            // which is pointing to the same record)
            while(iter){
                if(iter->getRecord()->getName().find(substring) != string :: npos){
                    if(countFrequency.find(iter->getRecord()) != countFrequency.end()){
                        countFrequency[iter->getRecord()]++;
                    }
                    else countFrequency[iter->getRecord()] = 1;
                }
                iter = iter->getNext();
            }
        }
        vector<pair<PhoneRecord*, int>> pairVector(countFrequency.begin(), countFrequency.end());

        // now putting mapped value to the vector so that we can apply sort method
         sort(pairVector.begin(), pairVector.end(), [](const pair<PhoneRecord*, int> &a, const pair<PhoneRecord*, int> &b) {
            return a.second > b.second;
        });
        // after getting sorted records in descending order we take its first value to the our ans (as to keep up with the return type)
        for(auto& i: pairVector){
            ans.push_back(i.first);
        }

        return ans;
    }

    // Add your own implementation for deleting a contact
    bool deleteContact(const string* searchName){
        vector<PhoneRecord*> deletionNeeded = fetchContacts(searchName);
        bool returnValue = false;
        // here we are deleting fetch contacts first PhoneRecord
        stringstream ss(deletionNeeded[0]->getName());
        string substring;
        // approach is to first took out every word from the given phoneRecord's name 
        // and then compute its hash value iterate over that key then delete those records whose name matches with our given phoneRecord's name 
        // then we repeat this approach for every word
        while(getline(ss, substring, ' ')){
            long long key = computeHash(substring);
            
            HashTableRecord* iter = hashTable[key];
            HashTableRecord* prevIter = nullptr;
            while(iter && iter->getRecord()->getName() != deletionNeeded[0]->getName()){
                prevIter = iter;
                iter = iter->getNext();
            }
            if(prevIter && iter){
                prevIter->setNext(iter->getNext());
                delete iter;
                returnValue = true;
            }
            else if(prevIter == nullptr){
                hashTable[key] = iter->getNext();
                delete iter;
                returnValue = true;
            }
        }
        return returnValue;
    }

    // Add your own implementation for counting records pointing to a contact
    int countRecordsPointingTo(const PhoneRecord* record) {
        int count = 0;
        stringstream ss(record->getName());
        string substring;

        // going through each word
        while(ss.good()){
            getline(ss, substring, ' ');
            int key = computeHash(substring);

            // computing hash value of each word then finding record in each of the key.
            HashTableRecord* iter = hashTable[key];
            while(iter && iter->getRecord() != record){
                iter = iter->getNext();
            }
            if(iter) count++;
        }

        return count;
    }

    // Add your own implementation for reading records from a file
    void readRecordsFromFile(const string& filename){
        ifstream in;
        in.open(filename);

        // reading file
        if(in.is_open()){
            string input, substring;
            string name, org;
            vector<string> phoneNo;
            int i, j = 1;

            // creating instances of each line in the given details.txt file 
            // then adding it to the PhoneBook instance
            while(getline(in, input)){
                stringstream ss(input);
                i = 0;

                while(getline(ss, substring, ',')){
                    if(i == 0) name = substring;
                    else if(substring[0] >= '0' && substring[0] <= '9') phoneNo.push_back(substring);
                    else org = substring; 
                    i++;
                }
                
                PhoneRecord* record = new PhoneRecord(name, org, phoneNo);
                addContact(record);
                phoneNo.clear();
            }
            in.close();
        } else {
            cout << "Failed to open the file ";
        }
    }
        
    // Destructor
    ~PhoneBook(){
        // when we delete a phoneBook instance then we need to dealloacte all the memory that we have created in heap 
        // so that there won't be any memory leak
        for (int i = 0; i < HASH_TABLE_SIZE; ++i) {
            HashTableRecord* current = hashTable[i];
            while (current) {
                HashTableRecord* temp = current;
                current = current->getNext();
                delete temp;
            }
        }
    }
};