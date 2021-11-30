var loginpage= document.querySelector(".loginpage")
var mesage = document.querySelector(".message"),
    login =document.querySelector(".login"),
    main = document.querySelector(".main");
    

// console.N


// document.querySelector(".addStudent").addEventListener("click", function(){
//     window.open("/adminLevels/administrative/add", "_self")
// })

document.querySelector(".back").addEventListener("click", function(){
    window.open("/adminLevels/administrative/login", "_self")
})

var studentBTn = document.querySelector(".studentbtn"),
    lecturerBtn= document.querySelector(".staffbtn");
    // state = "Student";




var studentSect= document.querySelector(".studentsect"),
    lecturersect= document.querySelector(".lecturersect")

studentBTn.addEventListener("click", function () {
    lecturersect.style.display='none'
    studentSect.style.display = 'unset'
    studentBTn.style.borderBottom = 'solid 4px blanchedalmond'
    lecturerBtn.style.borderBottom = 'none'

})

lecturerBtn.addEventListener("click", function () {
    lecturersect.style.display='unset'
    studentSect.style.display = 'none'
    lecturerBtn.style.borderBottom = 'solid 4px blanchedalmond'
    studentBTn.style.borderBottom='none'
})

