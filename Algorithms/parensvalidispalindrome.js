// ParensValid
// given "(())()" --> valid, "(()()))" --> invalid, ")()()" --> invalid

// function parensValid(str){
//     var count=0;
//     for(var i=0;i<str.length;i++){
//         if(str[i]=="("){
//             count++;
//         }
//         else if(str[i]==")"){
//             count--;
//         }
//     }
//     if(count==0 && str[0]!=')' && str[str.length-1]!='('){
//         return true;
//     }
//     else{
//         return false;
//     }
// }
// console.log(parensValid("((test))"));


// // IsPalindrome
// // given "racecar" --> valid, "Todd" --> invalid


function isPalindrome (str){
    var reverseStr="";
    for (i=str.length-1; i>=0; i--){
        reverseStr += str[i];
    }
    if (reverseStr == str){
        return true;
    }
    return false;
}
console.log(isPalindrome('racecar'));

function palindrome (str){
    for (var i=0; i<str.length/2;i++){
        if (str[i]!=str[str.length-1-i]){
            return false;
        }
    }
    return true;
}
console.log(palindrome('los parentesis!!'));