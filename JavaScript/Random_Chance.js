function slots (quarter){
    while (quarter>0) {
        if (Math.floor(Math.random()*100)==5) 
        {
            temp=50 + Math.floor(Math.random()*50);
            quarter=quarter + temp;
            console.log("You won", temp, "quarters!");
            console.log("You now have:", quarter, "quarters!");
            console.log("Thank you for playing!");
            return(quarter);
        } 
        else {
            quarter--;
            console.log("Nope! Keep trying!");
            console.log(quarter,"quarters remaining!");
        }
    }
    return(quarter);
}

slots(100);