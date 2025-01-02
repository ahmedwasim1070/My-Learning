// First C++ program :
// #include <iostream>
// using namespace std;
// int main()
// {
//     cout<<"Hello World!";
//     return 0;
// }
// Or
// #include <iostream>
// int main()
// {
//     std::cout << "Hello World!";
//     return 0;
// }

// Executable CMD for cpp code:
// g++ filename.cpp -o outputfilename.cpp
// ./outputfilename.exe

// Variables Data Types
// Primitive Data Types:
// int (4 Bytes)
// char (1 Byte)
// float (4 Bytes)
// bool (1 Byte)
// double (8 Bytes) >=13!
// You can make your data types bigger by using these infront of the data type
// long
// short
// long long
// signed
// unsigned

// Type Casting
// From Small data type to big data type is straight forward
// But from big to small we use it like that also know as EXPLICIT TYPE CASTING
// double price =100.99;
// int newPrice=(int)price;
// where paranthesis int will be the small data type that you want to convert

// Taking input
// int age;
// cin >> age;

// Problem
// cout << (5/2) ; //2 answer
// The answer shold be 2.5 but it will be 2 because both the input is int
// To fix this we use EXPLICIT Type Casting
// cout << (5/float(2)); // 2.5 answer
//

// Problem making Star cap
// #include <iostream>
// using namespace std;
// int main()
// {
//     int n = 4;
//     int temp = n;
//     for (int i = 0; i < n; i++)
//     {
//         temp--;
//         for (int j = 0; j < temp; j++)
//         {
//             cout << " ";
//         }
//         cout << "*";
//         for (int j = 0; j <= i * 2 - 2; j++)
//         {
//             cout << " ";
//         }
//         if (i >= 1)
//         {
//             cout << "*";
//         }
//         cout << endl;
//     }
// }

// Bitwise Operator
// &
// |
// ^
// <<
// >>

// Arrays
// dataType varaibleName[arraySize];
// int arr[10];
// int arr[]={1,2,3};

// Reverse an Array Problem
#include <iostream>
using namespace std;
void reverseString(int arr[], int end)
{
    int start = 0;
    while (start < end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}
int main()
{
    int size = 6;
    int arr[size] = {10, 20, 30, 40, 50, 60};
    reverseString(arr, size - 1);
    for (int j = 0; j <= size - 1; j++)
    {
        cout << j << ":" << arr[j] << endl;
    }
    return 0;
}