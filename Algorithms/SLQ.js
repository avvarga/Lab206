// function Node(val){ // class definition for Node
//     this.value = val; // value is a property and val is the incoming value we want to set this.value to
//     this.next = null; // next pointer is null as we don't assume the node have a buddy yet
// }
// function SLQueue(){
//     this.head = null; // these point
//     this.tail = null; // -> Node objs

//     this.size=function(){
//         var pointer=this.head;
//         var counter=0;
//         while(pointer){
//             counter++;
//             pointer=pointer.next;
//         }
//         return counter;
//     }

//     this.contains=function(val){
//         var pointer=this.head;
//         while(pointer){
//             if(pointer.value== val){
//                 return true;
//             }
//             pointer=pointer.next;
//         }
//         return false;
//     }

//     this.front=function(){
//         if(!this.head){
//             console.log("The queue is empty")
//         }
//         else{
//             console.log("The first value is: "+this.head.value)
//             return this;
//         }
//     }

//     this.isEmpty=function(){
//         return (!this.head);
//     }

//     this.enQ=function(val){
//         var node=new Node(val);
//         if(!this.head){
//             this.head=node;
//         }
//         else{
//             this.tail.next=node;
//         }
//         this.tail=node;
//         return this;
//     }

//     this.deQ=function(){
//         if(!this.head){
//             console.log("The queue is empty")
//         }
//         else if(this.size()>1){
//             var temp=this.head.value;
//             this.head=this.head.next;
//             return temp;
//         }
//         else{
//             var temp=this.head.value;
//             this.head=null;
//             this.tail=null;
//             return temp;
//         }
        
//     }


//     this.print=function(){
//         var pointer=this.head;
//         console.log('Values in the list: ')
//         while(pointer){
//             console.log(pointer.value)
//             pointer=pointer.next;
//         }
//         return this;
//     }
// }
// var test=new SLQueue();
// // test.size();
// // console.log(test.contains(8));
// // test.front();
// // console.log(test.isEmpty());
// test.enQ('5');
// test.enQ(15);
// test.enQ('45');
// console.log('The removed value is: '+test.deQ());
// test.print();


// Stacks

// function Stack(){
//     this.arr = [];

//     this.push = function (val){
//         this.arr[this.arr.length] = val;
//     }

//     this.pop = function (val){
//         this.arr.length -= 1
//     }

//     this.arr_top = function(){
//         return this.arr[this.arr.length-1]
//     }

//     this.contains = function(val){
//         for (var i = 0; i < this.arr.length; i++){
//             if (this.arr[i] == val){
//                 return true;
//             }
//         }
//         return false;
//     }

//     this.arr_size = function(){
//         return this.arr.length;
//     }

//     this.isEmpty = function(){
//         if (!this.arr.length){
//             return true;
//         }
//         return false;
//     }

//     this.print = function(){
//         console.log('These are the values of the array:')
//         for (var i = 0; i<this.arr.length; i++){
//             console.log (this.arr[i]);
//         }
//         console.log('----------------------------------------')
//     }
// }
test = new Stack();
test.push(1);
test.push(2);
test.push(3);
test.pop();
test.print();
console.log(test.arr_top());
console.log(test.contains(2));
console.log(test.isEmpty());
