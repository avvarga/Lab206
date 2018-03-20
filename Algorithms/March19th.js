function pushFront(arr,x){
    for (var i=arr.length; i>0; i--){
        arr[i]=arr[i-1];
    }
    arr[0]=x;
    console.log(arr);
}
pushFront([2,3,4],1);

// function popFront(arr){
//   var x= arr[0];
//   for(var i=0; i<arr.length-1; i++){
//     arr[i]=arr[i+1];
//   }
//   arr[arr.length-1]=x;
//   console.log(arr.pop());
// }
// popFront([1,2,3,4]);