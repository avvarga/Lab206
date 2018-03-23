// Min to Front
// given [4,2,1,3,5] --> [1,4,2,3,5]

function mintoFront(arr){
    var min = arr[0];
    var location = 0;
    for (var i=0; i<arr.length; i++){
        if (arr[i]<min){
            min = arr[i]
            location = i;
        }
    }
    for (var count=location; count>0; count--){
        arr[count]=arr[count-1];
    }
    arr[0]=min;
    console.log(arr);
}
// mintoFront([4,2,7,3,5,1]);


//Reverse
// given [5,4,3,2,1] --> [1,2,3,4,5]

function reverse(arr){
    var limit = Math.floor(arr.length/2);
    for (var i=0; i<limit; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    console.log(arr);
}
reverse([6,5,4,3,2,1]);