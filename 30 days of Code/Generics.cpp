

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
ś
template <class T>
void printArray(vector<T> vec){
    for(int i=0;i<vec.size();i++)
        cout<<vec[i]<<endl;
}

