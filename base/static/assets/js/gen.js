$(document).ready(function () {
    promptForm = document.querySelector("[prompt]")
    input = document.querySelector(".prompt")
    output = document.querySelector(".text-output")

    promptForm.addEventListener("submit", (e) => {
        e.preventDefault();
        input.disabled = true
        fetch("/gen/"+ model +"?prompt="+input.value)
        .then(res => res.json())
        .then(data => {
            output.innerHTML = data
            input.disabled = false
        })
    })
});