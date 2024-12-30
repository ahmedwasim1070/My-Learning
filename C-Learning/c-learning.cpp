// #include <iostream>
// int main()
// {
//     int num = 12;
//     char letter = 'a';
//     int newLetter = letter;
//     float PI = 3.14;
//     bool isTrue = true;
//     double bigNum = 200.99;
//     int newBigNum = (int)bigNum;
//     std::cout << num << letter << PI << isTrue << bigNum << newBigNum;
//     return 0;
// }

// #include <iostream>
// int main()
// {
//     int a;
//     std::cout << "Enter :";
//     std::cin >> a;
//     std::cout << a;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a, b;

//     cout << "Enter A :";
//     cin >> a;

//     cout << " Enter B : ";
//     cin >> b;

//     cout << a + b;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int a;
//     cout << "Enter Number a = \n";
//     cin >> a;
//     if (a >= 18)
//     {
//         cout << "You are Eligible to vote ";
//     }
//     else
//     {
//         cout << "You are Ineligible to vote";
//     }
// }

#include <iostream>
using namespace std;
int main()
{
    int a;
    cout << "Enter Your Number = ";
    cin >> a;

    if (a % 2 == 0)
    {
        cout << a << "\n Is Even Number";
    }
    else
    {
        cout << a << "\n Is odd Number";
    }
}