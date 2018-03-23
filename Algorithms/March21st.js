// Swap Pairs
// given [1,2,3,4] --> [2,1,4,3]
// or [1,2,3] --> [2,1,3]

// function swapPairs(arr){
//     var limit = arr.length;
//     if (arr.length%2 === 1) {
//         var limit = arr.length-1;
//     }
//     for (var i=0; i<limit; i+=2){
//         temp = arr[i];
//         arr[i]=arr[i+1];
//         arr[i+1] = temp;
//     }
//     console.log(arr); 
// }
// swapPairs([1,2,3,4,5]);




// Remove Duplicates
// given a SORTED array
// [1,2,2,2,3,3,4]
// [1,2,3,4]

// function removeDuplicates(arr){
//     var new_arr=[arr[0]];
//     for(var i=1; i<arr.length; i++){
//         if (arr[i]>arr[i-1]){
//             new_arr.push(arr[i]);
//         }
//     }
//     console.log(new_arr);
// }
// removeDuplicates([1,2,2,2,3,3,4,4,4,5,5,6,7,,8,8,8]);

// Option 2 of remove duplicates
function removeDuplicates(arr){
    for (var i=0; i<arr.length; i++){
        if (arr[i]==arr[i+1]){
            for (var count = i; count<arr.length; count++){
                arr[count]=arr[count+1];
            }
            i--;
            arr.pop();
        }
    }
    console.log(arr);
}
removeDuplicates([1,2,2,2,3,3,4,4,4,5,5,6,7,8,8,8]);