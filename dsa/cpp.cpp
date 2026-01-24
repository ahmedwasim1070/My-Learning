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

// Pair Sum Problem Sorted array
// Brute Force approch
// #include <iostream>
// #include <vector>
// using namespace std;
// vector<int> pairSum(vector<int> nums, int target)
// {
//     vector<int> ans;
//     int n = nums.size();
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = i + 1; j < n; j++)
//         {
//             if (nums[i] + nums[j] == target)
//             {
//                 ans.push_back(i);
//                 ans.push_back(j);
//                 return ans;
//             }
//         }
//     }
//     return ans;
// }
// int main()
// {
//     vector<int> nums = {2, 7, 11, 15};
//     int target = 9;
//     vector<int> ans = pairSum(nums, target);
//     cout << ans[0] << "," << ans[1] << endl;
//     return 0;
// }
// More Optimized way only on sorted array
// #include <iostream>
// #include <vector>
// using namespace std;
// vector<int> pairSum(vector<int> nums, int target)
// {
//     vector<int> ans;
//     int i = 0, j = nums.size();
//     while (i < j)
//     {
//         int sum = nums[i] + nums[j];
//         if (sum > target)
//         {
//             j--;
//         }
//         else if (sum < target)
//         {
//             i++;
//         }
//         else
//         {
//             ans.push_back(i);
//             ans.push_back(j);
//             return ans;
//         }
//     }
//     return ans;
// }
// int main()
// {
//     vector<int> nums = {2, 7, 11, 15};
//     int target = 9;
//     vector<int> ans = pairSum(nums, target);
//     cout << ans[0] << "," << ans[1] << endl;
//     return 0;
// }

// Majority Element Problem
// Brute Force Technique
// #include <iostream>
// #include <vector>
// using namespace std;
// int majority(vector<int> nums)
// {
//     for(int val: nums){
//         int freq=0;
//         for(int el: nums){
//             if(el==val){
//                 freq++;
//             }
//         }
//         if(freq>nums.size()/2){
//             return val;
//         }
//     }
//     return -1;
// }
// int main()
// {
//     vector<int> nums = {1, 1, 2, 2, 1};
//     cout<<majority(nums)<<" ";
//     return 0;
// }
// Little More Optimized Approch
// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;
// int majorityEl(vector<int> nums){
//     sort(nums.begin(),nums.end());
//     int freq=1,ans=nums[0];
//     for(int i=1;i<nums.size();i++){
//         if(nums[i]==nums[i-1]){
//             freq++;
//         }else{
//             freq=1;
//             ans=nums[i];
//         }
//         if(freq>nums.size()/2){
//             return ans;
//         }
//     }
//     return ans;
// }
// int main(){
//     vector<int> nums={1,1,2,2,1};
//     cout<<majorityEl(nums)<<" ";
//     return 0;
// }
// Most Optimized Approch Moore's voting algorith
// Basically It States that the majority number frequency will always be greater then the
// #include <iostream>
// #include <vector>
// using namespace std;
// int majorityEl(vector<int> nums){
//     int freq=0,ans=0;
//     for(int i=0;i<nums.size();i++){
//         if(freq==0){
//             ans=nums[i];
//         }
//         if(ans==nums[i]){
//             freq++;
//         }else{
//             freq--;
//         }
//     }
//     return ans;
// }
// int main(){
//     vector<int> nums={1,2,2,2,1};
//     cout<<majorityEl(nums)<<" ";
//     return 0;
// }

// Compute x^n
// in log n
// #include <iostream>
// using namespace std;
// int main()
// {
//     double x = 2.00;
//     long binForm = 10;
//     if (binForm < 0)
//     {
//         x = 1 / x;
//         binForm = -binForm;
//     }
//     double ans = 1;
//     while (binForm > 0)
//     {
//         if (binForm % 2 == 1)
//         {
//             ans *= x;
//         }
//         x *= x;
//         binForm /= 2;
//     }
//     cout << ans;
//     return ans;
// }

// Buy and Sell Stock
// #include <iostream>
// #include <vector>
// int main()
// {
//     std::vector<int> price = {7, 1, 5, 3, 5, 4};
//     int maxProfit = 0, bestBuy = price[0];
//     for (int i = 0; i < price.size(); i++)
//     {
//         if (price[i] > bestBuy)
//         {
//             maxProfit = std::max(maxProfit, price[i] - bestBuy);
//         }
//         bestBuy = std::min(bestBuy, price[i]);
//     }
//     std::cout << maxProfit << " " << '\n';
//     return maxProfit;
// }

// Container with most water
// Brute force approch
// #include <iostream>
// #include <vector>
// int main()
// {
//     std::vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
//     int maxVal = 0;
//     for (int i = 0; i < height.size(); i++)
//     {
//         for (int j = i + 1; j < height.size(); j++)
//         {
//             int w = j - i;
//             int ht = std::min(height[i], height[j]);
//             int area = w * ht;
//             maxVal = std::max(maxVal, area);
//         }
//     }
//     std::cout << maxVal;
//     return maxVal;
// }
// Two Pointer Approch
// #include <iostream>
// #include <vector>
// int main()
// {
//     std::vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
//     int maxVal = 0;
//     int lp = 0, rp = height.size();
//     while (lp < rp)
//     {
//         int w = rp - lp;
//         int ht = std::min(height[lp], height[rp]);
//         maxVal = std::max(maxVal, w * ht);
//         height[lp] < height[rp] ? lp++ : rp--;
//     }
//     std::cout << maxVal;
//     return maxVal;
// }

// Product of Array except itself
// Brute Force
// #include <iostream>
// #include <vector>
// std::vector<int> productOfArray(std::vector<int> nums)
// {
//     std::vector<int> ans(nums.size(), 1);
//     for (int i = 0; i < nums.size(); i++)
//     {
//         for (int j = 0; j < nums.size(); j++)
//         {
//             if (i != j)
//             {
//                 ans[i] *= nums[j];
//             }
//         }
//     }
//     return ans;
// }
// int main()
// {
//     std::vector<int> nums = {1, 2, 3, 4};
//     std::vector<int> ans = productOfArray(nums);
//     std::cout << ans[0] << std::endl;
//     return 0;
// }
// Optimal way
// #include <iostream>
// #include <vector>
// std::vector<int> productOfArray(std::vector<int> nums)
// {
//     std::vector<int> ans(nums.size(), 1);
//     for (int i = 1; i < nums.size(); i++)
//     {
//         ans[i] = ans[i - 1] * nums[i - 1];
//     }
//     int suffix = 1;
//     for (int i = nums.size() - 2; i >= 0; i--)
//     {
//         suffix *= nums[i + 1];
//         ans[i] *= suffix;
//     }
//     return ans;
// }
// int main()
// {
//     std::vector<int> nums = {1, 2, 3, 4};
//     std::vector<int> ans = productOfArray(nums);
//     std::cout << ans[0] << std::endl;
//     return 0;
// }

// Binary Search
// With Loop
// #include <iostream>
// #include <vector>
// using namespace std;
// int binarySearch(vector<int> arr, int target)
// {
//     int start = 0, end = arr.size() - 1;
//     while (start <= end)
//     {
//         // int mid = (start + end) / 2;        // can cause overflow SO
//         int mid = start + (end - start) / 2; // always use this to prevent overflow!
//         if (target > arr[mid])
//         {
//             start = mid + 1;
//         }
//         else if (target < arr[mid])
//         {
//             end = mid - 1;
//         }
//         else
//         {
//             return mid;
//         }
//     }
//     return -1;
// }
// int main()
// {
//     vector<int> arr1 = {-1, 0, 3, 6, 10, 23};
//     int target = 6;
//     cout << binarySearch(arr1, target) << endl;
//     return 0;
// }
// Recursion
// #include <iostream>
// #include <vector>
// using namespace std;
// int binarySearch(vector<int> arr, int target, int start, int end)
// {
//     if (start <= end)
//     {
//         int mid = start + (end - start) / 2;
//         if (target < arr[mid])
//         {
//             return binarySearch(arr, target, start, mid - 1);
//         }
//         else if (target > arr[mid])
//         {
//             return binarySearch(arr, target, mid + 1, end);
//         }
//         else
//         {
//             return mid;
//         }
//     }
//     return -1;
// }
// int main()
// {
//     vector<int> arr = {-1, 0, 3, 8, 11, 32};
//     int target = 32;
//     cout << binarySearch(arr, target, 0, arr.size() - 1);
//     return 0;
// }

// Bubble Sort
// #include <iostream>
// using namespace std;
// void bubbleSort(int arr[], int size)
// {
//     bool isSwapped;
//     for (int i = 0; i < size - 1; i++)
//     {
//         isSwapped = false;
//         for (int j = 0; j < size - 1; j++)
//         {
//             if (arr[j] > arr[j + 1])
//             {
//                 swap(arr[j], arr[j + 1]);
//                 isSwapped = true;
//             }
//         }
//         if (!isSwapped)
//         {
//             break;
//         }
//     }
// }
// int main()
// {
//     int size = 5;
//     int arr[size] = {17, 12, 18, 11, 15};
//     bubbleSort(arr, size);
//     for (int i = 0; i < size; i++)
//         cout << arr[i] << " ";
//     cout << endl;
// }

// Selection Sort
// #include <iostream>
// using namespace std;
// void selectionSort(int arr[], int size)
// {
//     for (int i = 0; i < size - 1; i++)
//     {
//         int minIdx = i;
//         for (int j = i + 1; j < size - 1; j++)
//         {
//             if (arr[j] < arr[minIdx])
//             {
//                 minIdx = j;
//             }
//         }
//         swap(arr[i], arr[minIdx]);
//     }
// }
// int main()
// {
//     int size = 5;
//     int arr[size] = {17, 12, 18, 11, 15};
//     selectionSort(arr, size);
//     for (int i = 0; i < size; i++)
//         cout << arr[i] << " ";
//     cout << endl;
// }

// Insertion Sort
// #include <iostream>
// using namespace std;
// void insertionSort(int arr[], int size)
// {
//     for (int i = 1; i < size; i++)
//     {
//         int key = arr[i];
//         int j = i - 1;
//         while (j >= 0 && arr[j] > key)
//         {
//             arr[j + 1] = arr[j];
//             j--;
//         }
//         arr[j + 1] = key;
//     }
// }
// int main()
// {
//     int size = 5;
//     int arr[size] = {17, 12, 18, 11, 15};
//     insertionSort(arr, size);
//     for (int i = 0; i < size; i++)
//         cout << arr[i] << " ";
//     cout << endl;
// }

// Quick Sort
// #include <iostream>
// using namespace std;
// int partition(int arr[], int low, int high)
// {
//     int pivot = arr[high];
//     int i = low - 1;
//     for (int j = low; j < high; j++)
//     {
//         if (arr[j] < pivot)
//         {
//             i++;
//             swap(arr[i], arr[j]);
//         }
//     }
//     swap(arr[i + 1], arr[high]);
//     return i + 1;
// }
// void quickSort(int arr[], int low, int high)
// {
//     if (low < high)
//     {
//         int pivotIdx = partition(arr, low, high);
//         quickSort(arr, low, pivotIdx - 1);
//         quickSort(arr, pivotIdx + 1, high);
//     }
// }
// int main()
// {
//     int size = 5;
//     int arr[size] = {17, 12, 18, 11, 15};
//     quickSort(arr, 0, size - 1);
//     for (int i = 0; i < size; i++)
//         cout << arr[i] << " ";
//     cout << endl;
// }

// LinkedList
// #include <iostream>
// using namespace std;
// class LinkedList
// {
// private:
//     struct Node
//     {
//         int data;
//         Node *next;
//     };
//     Node *head;

// public:
//     LinkedList() : head(nullptr) {}
//     LinkedList(int data) : head(nullptr)
//     {
//         Node *newNode;
//         newNode->data = data;
//         newNode = nullptr;
//     }
//     void insertAtEnd(int data)
//     {
//         Node *newNode = new Node{data, nullptr};
//         if (head == nullptr)
//         {
//             head = newNode;
//         }
//         else
//         {
//             Node *temp = head;
//             while (temp->next != nullptr)
//             {
//                 temp = temp->next;
//             }
//             temp->next = newNode;
//         }
//     }
// };
// int main()
// {
//     LinkedList l1(100);
//     l1.insertAtEnd(200);
// }

// Tower Of Hanoi
// #include <iostream>
// using namespace std;
// void hanoi(int n, char src, char aux, char dest)
// {
//     if (n == 1)
//     {
//         cout << "Move plate from : " << src << " To " << dest << endl;
//     }
//     else
//     {
//         hanoi(n - 1, src, dest, aux);
//         cout << "Move plate from : " << src << " TO " << dest << endl;
//         hanoi(n - 1, aux, src, dest);
//     }
// }
// int main()
// {
//     hanoi(3, 'A', 'B', 'C');
// }
