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
            console.logdata
            input.disabled = false
            if (model == "image"){
                document.querySelector("[output]").setAttribute("src", data[0].url)
                document.querySelector("[output1]").setAttribute("src", data[1].url)
                document.querySelector("[output2]").setAttribute("src", data[2].url)
                return
            }
            output.innerHTML = data
        })
    })
});