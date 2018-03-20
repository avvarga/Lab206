function negatives(arr){
    for(var i=0; i<arr.length; i++){
        if(arr[i]<0){
            arr[i]=0;
        }
    }
    return arr;
}
// negatives([-5,-4,5,8,-3]);


function minmaxavg(arr){
    var min =arr[0];
    var max =arr[0];
    var sum =0;
    var avg;
    for (var i=0; i<arr.length; i++){
        if (arr[i]<min){
            min=arr[i];
        }
        if (arr[i]>max){
            max=arr[i];
        }
        sum=sum+arr[i];
    }
    avg=sum/arr.length;
    // console.log([min,max,avg]);
    console.log("The minimum, maximum and average amounts of the values from [" +arr+ "] are:");
    console.log("Minimum:"+min);
    console.log("Maximum:"+max);
    console.log("Average:"+avg);
}
minmaxavg([3,4,5]);

