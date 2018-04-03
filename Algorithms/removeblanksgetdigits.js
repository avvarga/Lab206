// Remove Blanks
// given: " hello, world" --> return "hello,world"
function removeBlanks(str){
    var wordStr="";
    for (var i=0; i<str.length; i++){
        if (str[i] !== " "){
            wordStr += str[i];
        }
    }
    return wordStr;
}
// console.log(removeBlanks(' hello, wor ld'));


// Get Digits
// given "1a2a3b45a" --> return "12345"
function getDigits (str){
    var wordStr="";
    for (var i=0; i<str.length; i++){
        if (isNaN(str[i]) == false){
            wordStr += str[i];
        }
    }
    return parseInt(wordStr);
}
console.log (getDigits("1a2a3b45a"));