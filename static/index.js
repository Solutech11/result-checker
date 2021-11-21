console.log("eweee")
var studentpage = document.querySelector(".student"),
leturerpage = document.querySelector(".lecturer");

studentpage.addEventListener("click", function () {
    window.open("/studentlogin","_self")
})

leturerpage.addEventListener("click", function () {
    window.open("/adminLevels", "_self")
})