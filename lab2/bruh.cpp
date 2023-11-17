// Online C++ compiler to run C++ program online
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream ifs{"Details.txt"};
    string s;
    string l;
    vector<string> content();
    while((getline(ifs, l))){
    stringstream line(l);
    int i = 0;
    while(getline(line, s, ',')){
        content.push_back(s);
    }
    }
    for(auto row: content){
        for(auto element: row){
            cout<<element<<endl;
        }
    }
    return 0;
}