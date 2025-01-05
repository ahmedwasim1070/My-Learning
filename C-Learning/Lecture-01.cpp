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
// ^ XOR
// <<
// >>

// Arrays
// dataType varaibleName[arraySize];
// int arr[10];
// int arr[]={1,2,3};

// Reverse an Array Problem
// #include <iostream>
// using namespace std;
// void reverseString(int arr[], int end)
// {
//     int start = 0;
//     while (start < end)
//     {
//         swap(arr[start], arr[end]);
//         start++;
//         end--;
//     }
// }
// int main()
// {
//     int size = 6;
//     int arr[size] = {10, 20, 30, 40, 50, 60};
//     reverseString(arr, size - 1);
//     for (int j = 0; j <= size - 1; j++)
//     {
//         cout << j << ":" << arr[j] << endl;
//     }
//     return 0;
// }

// Vector Syntax
// It is imported for STL
// Vector is a data strutures i c++ but it is very much like arrays but the only difference they are dynamic means they do  not have any fixed size like in array you need to give size each time you define it.
// Example
// #include <iostream>
// #include <vector>
// using namespace std;
// int main()
// {
//     vector<int> vec = {1, 2, 3};
//     cout << vec[2];
//     return 0;
// }
// Another way to right vector
// #include <iostream>
// #include <vector>
// using namespace std;
// int main()
// {
//     vector<int> vec(3, 0); // where (3,0) = (sizeOfVector,valueAtEachIndex)
//     cout << vec[0];
//     return 0;
// }
// You can even use for Each loop on vector
// #include <iostream>
// #include <vector>
// using namespace std;
// int main()
// {
//     vector<int> vec(3, 0); // where (3,0) = (sizeOfVector,valueAtEachIndex)
//     for (int val : vec)
//     {
//         cout << val << endl;
//     }
//     return 0;
// }

// There are many built in function for vector
// size vec.size() return the size of the array
// push vec.push_back() appends value at the end
// pop vec.pop_back() deletst the last value of the vector
// front vec.front() prints the first element of the vector
// back vec.back() prints the last element of the vector
// at vec.at(idx) return the value of vector at the given index

// Static vs Dynamic allocation
// Static
// In Static the size of the array is declared at the time of the compilation
// Static type is executed in the stack in the part of the memory
// Dynamic
// While in dynamic size is declared at the runtime
// Dynamic type is executed in heap part of the memory
// when a new element is pushed in the vector a new copy of the vector  is created with two times bigger size and new element is placed now

// Kadane's Algorithm
// Subarray
// The countinouse part of an array is called subarray
// Mathametically:
// n*(n-1)/2  where n is number of arrays also know as size of an array
// Code for the finding the Subarray
// #include <iostream>
// using namespace std;
// int main()
// {
//     int n = 5;
//     int arr[5] = {1, 2, 3, 4, 5};
//     for (int start = 0; start < n; start++)
//     {
//         for (int end = start; end < n; end++)
//         {
//             for (int i = start; i <= end; i++)
//             {
//                 cout << arr[i];
//             }
//             cout << " ";
//         }
//         cout << endl;
//     }
// }
// Problem Maximum arrays sum
// #include <iostream> //Time coplexity n^2
// using namespace std;
// int main()
// {
//     int n = 7;
//     int arr[7] = {3,
//                   -4,
//                   5,
//                   4,
//                   -1,
//                   7,
//                   -8};
//     int maxSum = INT_MIN;
//     for (int start = 0; start < n; start++)
//     {
//         int currSum = 0;
//         for (int end = start; end < n; end++)
//         {
//             currSum += arr[end];
//             maxSum = max(currSum, maxSum);
//         }
//     }
// }
// Using :
// Kadane's Algorithm
// #include <iostream> // Linear Time Complexity
// using namespace std;
// int main()
// {
//     int n = 7;
//     int arr[n] = {3, -4, 5, 4, -1, 7, 8};
//     int maxSum = INT_MIN, crrSum = 0;
//     for (int val : arr)
//     {
//         crrSum += val;
//         maxSum = max(crrSum, maxSum);
//         if (crrSum < 0)
//         {
//             crrSum = 0;
//         }
//     }
//     cout << maxSum << " ";
//     return 0;
// }