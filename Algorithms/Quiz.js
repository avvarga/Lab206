// Print 1-255
function print1to255(){
    for (var i=1; i<256; i++){
        console.log(i);
    }
}
// print1to255();

// Print Odds 1-255
function printOdds1to255(){
    for (var i=1; i<256; i+=2){
        console.log(i);
    }
}
// printOdds1to255();

// Print Ints and Sum 0-255
function printandSum0to255(){
    var sum=0;
    for (var i=1; i<256; i++){
        sum +=i;
        console.log(i+', sum: '+sum);
    }
}
// printandSum0to255();

// Iterate and Print Array
function iterateAndPrint(arr){
    for (var i=0; i<arr.length; i++){
        console.log(arr[i]);
    }
}
// iterateAndPrint([1,2,3,4,5]);

// Find and Print Max
function findPrintMax(arr){
    var max = arr[0]
    for (var i=0; i<arr.length; i++){
        if (max<arr[i]){
            max=arr[i];
        }
    }
    console.log(max);
}
// findPrintMax([1,25,3,4,5]);

// Get and Print Average
function findPrintAvg(arr){
    var avg = 0
    for (var i=0; i<arr.length; i++){
        avg+=arr[i];    
    }
    avg=avg/arr.length;
    console.log(avg);
}
// findPrintAvg ([1,2,3,4,5]);

// Array with Odds
function arrayWithOdds(){
    var arr = [];
    for (var i=1; i<256; i+=2){
        arr.push(i);
    }
    console.log(arr);
}
// arrayWithOdds();

// Square the Values
function squareTheValues(arr){
    for (var i=0; i<arr.length; i++){
        arr[i]*=arr[i];    
    }
    console.log(arr);
}
// squareTheValues([1,2,3,4,5]);

// Greater than Y
function greaterThanY(arr,y){
    var count =0;
    for (var i=0; i<arr.length; i++){
        if (arr[i]>y){
            count++;
            console.log(arr[i]+' is greater than '+y+'. So far, '+count+' numbers are greater than it.')
        }
    }
}
// greaterThanY([1,2,3,4,5],3);

// Zero Out Negatives
function zeroOutNegatives (arr){
    for (var i=0; i<arr.length; i++){
        if (arr[i]<0){
            arr[i]=0;
        }
    }
    console.log(arr);
}
// zeroOutNegatives([-1,2,-3,4,-5]);

// Max, Min, Average
function maxMinAvg(arr){
    var min = arr[0];
    var max = arr[0];
    var avg = 0;
    for (var i=0; i<arr.length; i++){
        avg+=arr[i];
        if (arr[i]<min) {
            min = arr[i];
            
        }
        else if (arr [i]>max){
            max = arr[i];
        }
    }
    avg = avg/arr.length;
    console.log('Max: '+max);
    console.log('Min: '+min);
    console.log('Avg: '+avg);
}
// maxMinAvg([1,2,3,4,5]);

// Shift Array Values
function shiftArrayValues(arr){
    for (var i=0; i<arr.length; i++){
        arr[i] = arr[i+1];
    }
    arr[arr.length-1] = 0;
    console.log(arr);
}
// shiftArrayValues([1,2,3,4,5]);

// Swap String for Negatives
function stringOutNegatives (arr){
    for (var i=0; i<arr.length; i++){
        if (arr[i]<0){
            arr[i]='Dojo';
        }
    }
    console.log(arr);
}
// stringOutNegatives([-1,2,-3,4,-5]);
