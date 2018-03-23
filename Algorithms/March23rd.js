// Rotate
// given [1,2,3,4],2 --> [3,4,1,2]

function rotate(arr,rotation){
    for (var i=0; i<rotation; i++){
        var temp = arr[arr.length-1];
        for (var count=arr.length-1; count>0; count--){
            arr[count] = arr[count-1];
        }
        arr[0] = temp;
    }
    console.log(arr);
}
// rotate([1,2,3,4],2);



// Concat
// given [1,2]["a","b"] --> return [1,2,"a","b"]

// adding arr2 to arr1
function concat(arr1,arr2){
    for (var i=0; i<arr2.length;i++){
        arr1[arr1.length]= arr2[i];
    }
    console.log(arr1);
}
// concat ([1,2],["a","b"]);

// with a new array
function concat(arr1,arr2){
    var new_arr=[];
    for(var i=0;i<arr1.length;i++){
        new_arr[i]=arr1[i];
    }
    for(var i=0;i<arr2.length;i++){
        new_arr[new_arr.length]=arr2[i];
    }
    console.log(new_arr);
 }//return new array
 concat([1,2],["a","b"]);