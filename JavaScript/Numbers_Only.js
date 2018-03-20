function newArray(arr){
    var numbersOnly =[];
    for(var i=0; i<arr.length; i++){
        if (typeof arr[i]==="number") {
            numbersOnly.push(arr[i]);        
        }
    }
    return numbersOnly;
}
console.log(newArray([1,"apple",-3,"orange",0.5]));
