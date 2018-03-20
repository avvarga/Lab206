function squares (arr){
    if(arr.length===0){
        return "Your array is empty!";
    }
    else{
        for(var i=0; i<arr.length; i++){
            arr[i]=arr[i]*arr[i];
        }
        return arr;
    }
}
console.log(squares([2,-4,6]));

// function greaterthany (arr,y){
//     var sum=0;
//     if(arr.length===0){
//         return "Your array is empty!";
//     }
//     else{
//         for(var i=0; i<arr.length; i++){
//             if(arr[i]>y){
//                 sum++;
//             }
//         }
//         return sum;
//     }
// }
// console.log(greaterthany([2,4,6],1));