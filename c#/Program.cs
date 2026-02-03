using System;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using System.Linq;
using System.Threading;

namespace MyFirstApp;

class Program
{
    static void Main(string[] args)
    {
        // In C# the data types also very depend upon how you assign that value
        // Data Types
        // int number = 20;
        // Where letter at the end represents the number will be of that specific data type
        // L
        // long secNumber = 1000L;
        // The diff between float and decimal will be float is speed and decimal is precision where float is the round off point value and double is the accurate
        // D
        // double thirdNumber = 12D;
        // F
        // float forthNumber = 12F;
        // M
        // decimal fifthNumber = 1M;
        // Char '' fror character
        // char firstName = 'a';
        // Strings "" for string
        // string secondName = "ahmed";
        // True/False
        // bool isTrue = false;
        // var - use var in very common cases where the variable name can easily represent the thing it is storing
        // var num = 100L;
        // const - makes constant data type 
        // const int inMutable = 12;

        // Operators
        // 
        // number++;
        // ++number;
        // 
        // number += 1;
        // 
        // secondName += firstName;
        // 
        // thirdNumber = number / secNumber;
        //
        // forthNumber = number % secNumber;

        // Data conversion
        // string tempName = "23";
        // int tempNum = Convert.ToInt32(tempName);
        // long tempBigNum = Convert.ToInt64(tempName);

        // int age = 12;
        // If statments & Else
        // if (age <= 18)
        // {
        //     Console.WriteLine("You are A kid Boi");
        // }
        // else if (age > 30)
        // {
        //     Console.WriteLine("You are old Boi.");
        // }
        // else
        // {
        //     Console.WriteLine("You are not a kid boi, get a job.");
        // }
        // Small If
        // string result = (age >= 18) ? "You are mature." : "You are not mature.";
        // Console.WriteLine(result);

        // int day = 0;
        // Switch Statment
        // switch (day)
        // {
        //     case 1:
        //         Console.WriteLine("Monday");
        //         break;
        //     case 2:
        //         Console.WriteLine("Tuesday");
        //         break;
        //     case 3:
        //         Console.WriteLine("Wednesday");
        //         break;
        // }

        // Loops 
        // For
        // for (int i = 0; i < 5; i++)
        // {
        //     Console.WriteLine("Nigga " + i);
        // }
        // While
        // while (day <= 7)
        // {
        //     day++;
        // }
        // string[] names = new string[] { "name", "nigger", "ali" };
        // ForEach 
        // foreach (string name in names)
        // {
        // Console.WriteLine(name);
        // }

        // Parse Function
        // string temp = "12";
        // bool success = int.TryParse(temp, out int res);
        // if (success)
        // {
        //     Console.WriteLine(res);
        // }

        // String Literals in C#
        // string sentence = "He said \"hello\" ";
        // string path = "C:\\Users\\ahmedwasim1070\\Downloads\\temp.pdf";
        // Verbatum String
        // path = @"C:\Users\ahmedwasim1070\Downloads\temp.pdf";
        // sentence = $"He said {path}";

        // String Formating
        // string name = "Ahmed";
        // int age = 21;
        // Console.WriteLine("Hello, My name is {0} and my age is {1}", name, age);
        // Console.WriteLine($"Hello, My name is {name} and my age is {age}");

        // String Concatination
        // string name = "Ahmed";
        // int age = 21;
        // string sentence = String.Concat("My name is ", name, "and the age ", age);
        // Console.WriteLine(sentence);
        // string[] names = new string[] { "Ali", "Ahmad", "Hamza" };
        // Console.WriteLine(string.Concat(names));

        // string.Empty;
        // stringVariableName.Equals(stringVariableName);
        // meessage.ContainsAny("h");
        // string.IsNullOrEmpty(name)
        // Loop in strings
        // string meessage = "hello world";
        // for (int i = 0; i < meessage.Length; i++)
        // {
        //     Console.Write(meessage[i]);
        //     Thread.Sleep(100);
        // }

        // Arrays
        // int[] numbers = new int[3];
        // string[] names = new string[] { "name", "nigger", "ali" };
        // Sorting
        // int[] numbers = new int[] { 1, 2, 3, 4, 5 };
        // Array.Sort(arrayName);
        // Array.Reverse(arrayName);
        // Array.Clear(arrayName, 0, arrayName.Length);
        // Array(arrayName,searchNumber);

        // List (Dynamic Arrays)
        // List<string> cars = new List<string>();
        // cars.Add("Toyota");
        // cars.Remove("Toyota");
        // string myCar = cars[0];
        // int count = cars.Count;

        // Dictionaries
        // Dictionary<string, decimal> prices = new Dictionary<string, decimal>();
        // prices.Add("Oil", 50.5M);
        // prices["Tire"] = 100M; // Add or Update
        // if (prices.ContainsKey("Oil"))
        // {
        //     Console.WriteLine(prices["Oil"]);
        // }
        // Dictionary<int, string> names = new Dictionary<int, string>
        // {
        //     {1,"Ali"},
        //     {2,"Ahmed"},
        //     {3,"Hamza"},
        // };
        // for (int i = 0; i < names.Count; i++)
        // {
        //     KeyValuePair<int, string> item = names.ElementAt(i);
        //     Console.WriteLine($"{item.Key} : {item.Value}");
        // }
        // foreach (KeyValuePair<int, string> items in names)
        // {
        //     Console.WriteLine($"{items.Key} : {items.Value}");
        // }
        // Dictionary<string, string> names = new Dictionary<string, string>
        // {
        //     {"Ahmed","Ali"},
        //     {"Muhammad","Ahmed"},
        //     {"Ali","Hamza"},
        // };
        // Console.WriteLine(names["Muhammad"]); // Can cause Runtime if item not available
        // if (names.TryGetValue("Muhammad", out string name))
        // {
        //     Console.WriteLine(name);
        // }

        // Functions
        // Where the keyword static means accessing the funciton or variable from anywhere !
        // static void HelloWorld()
        // {
        //     Console.WriteLine("Hello World");
        // }

        // Fizz Buzz Excercise
        // bool loopStatus = true;
        // while (loopStatus)
        // {
        //     Console.Write("Enter the number for FizzBizz : ");
        //     string userInput = Console.ReadLine()!;
        //     Console.WriteLine();
        //     if (!int.TryParse(userInput, out int num))
        //     {
        //         Console.WriteLine("Failed To parse as it is invalid");
        //     }
        //     switch (num)
        //     {
        //         case int _ when (num % 3 == 0 && num % 5 == 0):
        //             Console.WriteLine("FizzBuzz");
        //             break;
        //         case int _ when (num % 3 == 0):
        //             Console.WriteLine("Fizz");
        //             break;
        //         case int _ when (num % 5 == 0):
        //             Console.WriteLine("Buzz");
        //             break;
        //         default:
        //             Console.WriteLine("Fizz nor Buzz");
        //             break;
        //     }
        //     Console.Write("Do you wanna play again enter (yes/no) : ");
        //     string userInputStatus = Console.ReadLine()!;
        //     Console.WriteLine();
        //     loopStatus = (userInputStatus == "yes") ? true : false;
        // }
    }
}
