let home_para = document.getElementById("home-paragraph");
let submit_btn = document.getElementById("submit-btn");
let submit_btn_check = document.getElementById("submit-btn-check");
let submit_btn_spinner = document.getElementById("submit-btn-spinner");
let home_checking_block = document.getElementById("home-checking-block");
let home_results_block = document.getElementById("home-results-block");

window.onload = function() { 
    // submit_btn_spinner.style.display = "none"
}

function generateRandomValue() {
    return Math.random();
} 

function roundToTwoDecimalPlaces(number) {
    return Number(number.toFixed(2));
}

let onClickCheck = () =>{

    submit_btn.disabled = true;
    submit_btn_check.style.display = "none"
    home_para.style.display = "none";
    submit_btn_spinner.style.display = "block"
    home_checking_block.style.display = "block";

    let link = document.getElementById("search").value;

    fetch('https://jsonplaceholder.typicode.com/comments?postId=1')
        .then(response => response.json())
        .then(data => {
            console.log(link);

            const randomValue = generateRandomValue();
            let percentage = Math.round(roundToTwoDecimalPlaces(randomValue) * 100);

            if( percentage <= 25 ){
                home_results_block.style.color = "#a22b0a";
            }else if( percentage <= 50 ){
                home_results_block.style.color = "#c06607";
            }else if( percentage <= 75 ){
                home_results_block.style.color = "#f6ce08";
            }else{
                home_results_block.style.color = "#0aa263";
            }

            home_results_block.textContent = percentage + "%"

            document.getElementById("search").value = ""
            submit_btn.disabled = false;
            submit_btn_check.style.display = "block"
            submit_btn_spinner.style.display = "none"
            home_checking_block.style.display = "none";
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            submit_btn.disabled = false;
            submit_btn_check.style.display = "block"
            home_para.style.display = "block";
            submit_btn_spinner.style.display = "none"
            home_checking_block.style.display = "none";
        });
}
