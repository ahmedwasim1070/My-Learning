// console.log("Hello Nigga!")
// Different Types of varaibles in Javascript
// fullName="ahmed"
// age=19
// state=true
// a=null
// b=undefined
// You can assign variable like above in many simple cases but in js we use keyword var,let and const

// VAR
// Variable can be re-declared updated and are global scoped
// LET
// Let cannot be re-declared but can be updated. A blcok scope variable.
// Const
// Const cannot be re-declared and also cannot be updated you always have to declare and assign value from the begning and block scope varaible


// Data types in JS
// Primitive Data types 
// Numbers,string,bigint,Bolean,Null,Undefined,Symbol
// let x=10;
// let fullName="ahmed";
// let num=BigInt(123231)
// let empty=null
// let bol=true
// let symbol=symbol("hello!")
// Non Primitive Data types
// Objects,functions,arrays
// Objects 
// You can define objects with let and const
// const student={
//     fullName : "Muhammad Ahmad",
//     age: 20,
//     class: 1
// }
// In order to update 
// student["fullName"]="Ali"
// console.log(student.fullName)
// You can add string to a number
// One good thing about js is unitiy operators
// a++ means it is increamented by one on next step and ++a means it is increamented by one on this step
// a--
// One more advance thing is that you have triple === it also compare the types to!
// if statment 
// Syntax
// if (condition){
//   Statment
// }
// if else statment
// Syntax
// if (condition){
//    statment 
// }else if (condition2) {
//    statment
// }else{
//    statment
// }
// Ternary Operatro it is little similar as clever if
// condition ? statment : statment 2
// example
// age>18?"adult":"kid"
// Switch statment
// Syntax
// switch (paramenter){
//     case "hello":
//         console.log("parameter was: hello")
//     case "world":
//         console.log("parameter was: world")
//     default:
//         console.log("nothing")
// }

// Practice 
// let res=prompt("Entere a Number :")
// if(res%5===0){
//     console.log(true)
// }else{
//     console.log(false)
// }

// let per=prompt("Enter Your marks :")
// if(per<=100 && per>=90){
//     console.log("A+")
// }else if(per<=90 && per>=80){
//     console.log("A")
// }else{
//     console.log("fail")
// }


// Loops
// for loop
// for(leti=1;i<=5;i++){
//     console.log("You are a nigga!")
// }
// while loop
// let i=1;
// while (i<=5){
//     console.log("i=",i)
// }
// Do while Loop
// The only difference is that it has some condition  if the loop condition gets false some kind of work will be done
// let i=20
// do{
//     console.log("hello nigga!")
//     i++;
// } while(i>=10);
// since the condition was not meated in the while so the statment in do is executed one time 
// for of loops
// it is mostly use in itration
// for(let char in str){
//     statment
// }
// Practice 
// let inp=prompt("Enter the even number")
// while (inp <= 100) {
//     if(inp%2===0){
//         console.log(inp)
//     }
//     inp++;
// }
// let arr=[85,97,44,37,76,60]
// let res=0
// for(let val of arr){
//     res+=val
// }
// console.log(res/arr.length)
// let arr=[250,645,300,900,50]
// for(let i=0;i<arr.length;i++){
//     arr[i]=arr[i]-arr[i]/10
// }
// console.log(arr)
// Push = append
// Functions 
// Syntax 
// function functionName(){
//     // Statment
// }
// Arrow Functions 
// Syntax
// Varaiable functionname=(parameters,.,.)=>{
//        Statement
// }
// function fndVowels(userInp){
//     let res=""
//     for(let char of userInp){
//         if(char==="a" || char==="e" || char==="i" || char==="o" || char==="u"){
//             res=res+char
//         }
//     }
//     console.log(res)
// }
// fndVowels(userInp="ahmed")
// forEach loop
// arr.forEach(function functionname(parameter){
//     statment
// })
// arr.forEach((parameter)=>{
    // Statment
// })
// Default parameters in javascript 
// val , idx , arr
// list=[2,4,6,8,10]
// list.forEach((val)=>{
//     console.log(val*=val)
// })
// or
// list=[2,4,6,8,10]
// let getSqr=(val)=>{
//     console.log(val*val)
// }
// list.forEach(getSqr)
// .map
// marks=[91,12,81,93,92]
// let newArr=marks.filter((val)=>{
//     return val>=90
// })
// let userInp=prompt()
// list=[]
// for(let i=1;i<=userInp;i++){
//     list.push(i)
// }
// let sum=list.reduce((res,val)=>{
//     return res*val;
// })
// console.log(sum)
// class Node{
//     constructor(data=0,next=null){
//         this.data=data;
//         this.next=next;
//     }
// }
// class LinkedList{
//     constructor(head=null){
//         this.head=head;
//         this.n=0;
//     }
//     append(value){
//         const newNode= new Node(value);
//         if(this.head===null){
//             this.head=newNode;
//         }else{
//             let current = this.head;
//             while(current.next!==null){
//                 current=current.next;
//             }
//             current.next=newNode;
//         }
//         this.n++;
//     }
//     traverse(){
//         let current=this.head;
//         let res="";
//         while(current){
//             res+=current.data+'->';
//             current=current.next;
//         }
//         return res+null;
//     }
// }
// const l1= new LinkedList();
// l1.append(1)
// l1.append(2)
// l1.append(3)
// console.log(l1.traverse())

// const binarySearch=(nums,target,low,high)=>{
//     if(low<=high){
//         let mid=Math.floor((low+high)/2);
//         if(nums[mid]===target){
//             return mid;
//         }else if(nums[mid]<target){
//             return binarySearch(nums,target,mid+1,high);
//         }else{
//             return binarySearch(nums,target,low,mid-1);
//         }
//     }else{
//         return -1
//     }
// }
// nums=[1,2,3,4,5,6]
// console.log(binarySearch(nums,2,0,nums.length-1))
// Async Wait


// Trees
class Tree{
    constructor(data,children=null,parent=null){
        this.data=data;
        this.children=[] || children;
        this.parent=null;
    }
    addChild(child){
        let newChild=new Tree(child,parent=this);
        this.children.push(child);
        return newChild;
    }
    toString(){
        return this.children
    }
}
let root=new Tree("Elctronics")
let laptop=new Tree("Laptop")
let mac=laptop.addChild(new Tree("Mac"))
let windows=laptop.addChild(new Tree("Windows"))
let Linux=laptop.addChild(new Tree("Linux"))
root.addChild(laptop)
console.log(root.toString())
// Graphs
// Hash Maps