document.querySelector(".higherAdmin").addEventListener("click", function () {
    window.open("/adminLevels/administrative", "_self")
})

document.querySelector(".lecturer").addEventListener("click", function () {
    window.open("/adminLevels/lecturer", "_self")
})
document.querySelector(".back").addEventListener("click", function(){
    window.history.back();
})