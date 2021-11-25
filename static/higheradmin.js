var loginpage= document.querySelector(".loginpage")
var mesage = document.querySelector(".message"),
    login =document.querySelector(".login"),
    main = document.querySelector(".main");
    
function brand () {
    console.log(67);
    if (mesage == "Done"){
        console.log("jeje");
        login.style.display ="none";
        main.style.display= 'unset';
        i=400;
    }
}

// console.N


// document.querySelector(".addStudent").addEventListener("click", function(){
//     window.open("/adminLevels/administrative/add", "_self")
// })

document.querySelector(".back").addEventListener("click", function(){
    window.history.back();
})

var studentBTn = document.querySelector(".student"),
    lecturerBtn= document.querySelector(".staff"),
    state = "Student"