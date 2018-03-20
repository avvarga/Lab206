// Insert an element in a specified location
// given: [1,2,3],1,4 --> [1,4,2,3]
// function insertAt (arr, index, value){
//     if (index>=0 && index<=arr.length) {
//         for(var i=arr.length; i>index; i--){
//             arr[i] = arr[i-1];
//         }
//         arr[index] = value;
//         console.log(arr);
//     } else {
//         console.log("Invalid index, please choose a number between 0 and", arr.length)
//     }
// }
// insertAt([1,2,3],1,4);


// Remove an element from a specified location
// given [1,2,3],1 --> return 2 ---> [1,3]
function removeAt (arr,index){
    var number = arr[index];
    for(var i=index; i<arr.length; i++){
        arr[i]=arr[i+1];
    }
    arr[arr.length-1]=number;
    return arr.pop()
}
console.log(removeAt([1,2,3],1));