#include <bits/stdc++.h>
using namespace std;

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

int main(){
    cout<<computeHash("Rodriguez")<<endl;
    cout<<computeHash("Akshay")<<endl;
    return 0;
}