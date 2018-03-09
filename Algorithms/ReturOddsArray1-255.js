function returnOddsArray1To255 (){
    var arr = [];
    for(var i=1; i<256; i+=2){
    // for(var i=1; i<256; i++){
    //     if(i%2!=0){
    //         arr.push(i);
    //     }
        arr.push(i);
    }
    return arr;
}
console.log(returnOddsArray1To255());