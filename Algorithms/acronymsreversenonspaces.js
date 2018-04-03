// Acronyms
// given: "Esteban does it different" --> return: "EDID"

function acronyms (str){
    var new_str = str[0];
    for (i=1; i<str.length; i++){
        if (str[i-1] == " " && str[i] != " "){
            new_str += str[i];
        }
    }
    return new_str.toUpperCase();
}
console.log(acronyms("Esteban does   it different"));

// Reverse
// given "hello, world" --> return "dlrow ,olleh"

function reverse(str){
    var new_str='';
    for(var i=str.length-1;i>=0;i--){
        new_str+=str[i];
    }
    return new_str;
}
console.log(reverse('Hello, world'));



// non-spaces
// given "hello, world" --> return 11
function nonSpaces(str){
    var count=0;
    for (var i=0; i<str.length; i++){
        if (str[i] != " "){
            count++;
        }
    }
    return count;
}
// console.log(nonSpaces("hello, world"));