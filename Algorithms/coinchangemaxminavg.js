// function coinChangeObject(num){
//     var coins = {
//         quarters:0,
//         dimes:0,
//         nickels:0,
//         pennies:0
//         };
//     coins.quarters = Math.floor(num/25);
//     num%=25;
//     coins.dimes = Math.floor(num/10);
//     num%=10;
//     coins.nickels = Math.floor(num/5);
//     num%=5;
//     coins.pennies = num;
//     return coins;
// }
// console.log(coinChangeObject(134));


function maxMinAvg (arr){
    var result = {max:arr[0],
        min:arr[0],
        avg:0};
    for (var i=0; i<arr.length; i++){
        if (result.max<arr[i]){
            result.max=arr[i];
        }
        else if(result.min>arr[i]){
            result.min=arr[i];
        }
        result.avg+=arr[i];
    }
    result.avg/=arr.length;
    return result;
}
console.log(maxMinAvg([1,2,5,7]));