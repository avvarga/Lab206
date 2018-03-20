function swapValues (arr){
    for(var i=0; i<arr.length-1; i++){
        arr[i]=arr[i+1];
    }
    arr[arr.length-1]=0;
    // console.log(arr);
}
swapValues([1,2,3,4,5]);


function numberToString(arr){
    for(var i=0; i<arr.length; i++){
        if(arr[i]<0){
            arr[i]="Dojo";
        }
    }
    // console.log(arr);
}
numberToString([-1,-2,4]);

function swap(arr){
    var temp =arr[0];
    arr[0]=arr[arr.length-1];
    arr[arr.length-1]=temp;
    return arr;
}
console.log(swap([1,2,3,4,5]));