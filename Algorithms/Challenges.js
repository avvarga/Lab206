//1) print values from 1 to 255
function print1to255(){
    for(var cont=1;cont<=255;cont++){
        console.log(cont);
    }
}
print1to255()
//2) even numbers from 1 to 1000
function even(){
    for(var cont=2;cont<=1000;cont+=2){
        console.log(cont);
        //for(var i=1;i<1001;i++){
        //    if(i%2===0){
        //        console.log(i);
        //    }
        //}

    }
}
even()
//3) add up odd numbers from 1 to 5000 and print the total
function sumOdds(){
    var sum=0;
    for(var cont=1;cont<=5000;cont+=2){
        sum=sum+cont;
    }
    console.log(sum);
}
sumOdds()
