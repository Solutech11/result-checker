document.querySelector(".backs").addEventListener('click',function () {
    window.history.back()
})

document.querySelector(".home").addEventListener('click',function () {
    window.open("/","_self", "true")
})