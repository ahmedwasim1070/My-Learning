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