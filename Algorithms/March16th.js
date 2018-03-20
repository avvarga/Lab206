function rotateLeft(arr){
    var temp =arr[0];
    for(var i=0; i<arr.length; i++){
        arr[i]=arr[i+1];
    }
    arr[arr.length-1]=temp;
    return arr; 
}
// console.log(rotateLeft([1,2,3,4,5]));

function reverseArray(arr){
    var newarr = [];
    for(var i=0; i<arr.length; i++){
        newarr[i]=arr[arr.length-1-i];
    }
    return newarr;
}
console.log(reverseArray([1,2,3,4,5]));