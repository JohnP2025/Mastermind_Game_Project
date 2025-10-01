
window.addEventListener("load", newGame); //Creates event listener triggered by loading page and calls newGame method

function newGame(){
    const gameState = { //initialize local memory so browser window can associate guesses with correct game settings and id
        gameId: null,
        finished: false,
        colors: null
    };

    fetch("/new_game", { //call Flask's new_game method
        method: "POST", 
        headers: {
            "Content-Type": "application/json"
        },
    })
    .then(response => response.json()) //process response as JSON
    .then(data => {
        console.log("Server response:", data);
        gameState.finished = data.finished;
        gameState.gameId = data.data.game_id;
        gameState.colors = data.data.colors;
        document.getElementById("game_id").textContent = gameState.gameId //TODO: Address inconsistent variable naming convention
        document.getElementById("remaining-guesses").textContent = "Remaining guesses: " + (data.data.maxGuesses);
        
        
        const lenColors = gameState.colors.length;

        const seqLength = data.data.sequence_length;

        const submitButton = document.getElementById("submit-button")
        const form = document.getElementById("input-form")

        for(let i=0; i<seqLength; i++){ //dynamically inserts dropdowns based on sequence length and color options
            let dropdownContainer = document.createElement("div")
            form.insertBefore(dropdownContainer, submitButton); //insert dropdown container
            dropdownContainer.setAttribute("class", "dropdown-container");
            
            let label = document.createElement("label");
            let select = document.createElement("select");
            

            dropdownContainer.appendChild(label);
            dropdownContainer.appendChild(select);


            select.setAttribute("id", "color"+(i+1));
            select.setAttribute("name", "color"+(i+1));
            label.setAttribute("for", "color"+(i+1));
            label.textContent = "Color " + (i+1) + ":";

            for(let j=0;j<lenColors; j++){ //inserts options for each dropdown
                let option = document.createElement("option");
                select.appendChild(option);
                option.setAttribute("value", gameState.colors[j]);
                option.setAttribute("class", gameState.colors[j]);
                option.textContent = gameState.colors[j];
            }

            select.addEventListener("change", function() { //event listener to change background colors of dropdowns
                const selectedOption = this.options[this.selectedIndex];
                const selectedColor = selectedOption.getAttribute("class");

                if (selectedColor == "Pink"){
                    this.style.backgroundColor = "deeppink";
                    this.style.color = "black";
                }
                else if (selectedColor == "Orange"){
                    this.style.backgroundColor = "darkorange";
                    this.style.color = "black";
                }
                else if (selectedColor == "Yellow") {
                    this.style.backgroundColor = "gold";
                    this.style.color = "black";
                }
                else if (selectedColor == "Green") {
                    this.style.backgroundColor = "forestgreen";
                    this.style.color = "white"; 
                }
                else if (selectedColor == "Cyan"){
                    this.style.backgroundColor = "aquamarine";
                    this.style.color = "black";
                }
                else if (selectedColor == "Indigo"){
                    this.style.backgroundColor = "indigo";
                    this.style.color = "white";
                }
                else {
                    this.style.backgroundColor = selectedColor.toLowerCase();
                    this.style.color = "black";
                }
            })

            const initialSelectedOption = select.options[select.selectedIndex];
            const initialColor = initialSelectedOption.getAttribute("class");

            //Could repeat if statements later, but just initializing to Pink for now
            if (initialColor == "Pink"){
                    select.style.backgroundColor = "deeppink";
            } 

            let br = document.createElement("br");
            form.insertBefore(br, submitButton);

        }

        document.getElementById("submit-button").addEventListener("click", (event) => { //event listener on submit button to call checkGuess
            event.preventDefault(); //prevents page from reloading when submit button is clicked
            checkGuess(gameState.gameId, seqLength);
        })
    });
    
}

function checkGuess(game_id, seq_length){

    let guessColors = [];
    
    for(let i=0; i<seq_length; i++){
        guessColors[i] = document.getElementById("color"+(i+1)).value;
    }    

    fetch("/guess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            game_id: game_id,
            guess: guessColors
        })
    })
    .then(response => response.json())
    .then(data => {
            console.log("Server response:", data);
            rightPos = data.data.rightPos;
            wrongPos = data.data.wrongPos;
            guessUpdate = "Your guess had " + rightPos + " elements placed correctly and " + wrongPos + " elements placed incorrectly.";
            document.getElementById("guess-info").textContent = guessUpdate;
            document.getElementById("remaining-guesses").textContent = "Remaining guesses: " + (data.data.maxGuesses - data.data.guesses);

            if(data.data.finished){ //disable submit button and retrieve sequence after game is finished
                document.getElementById("submit-button").disabled = true
                game_seq = data.data.sequence
                seq_reveal = "Game is over. The correct sequence was: ";
                for( let i=0; i<game_seq.length-1; i++){
                    seq_reveal += game_seq[i] + ", ";
                }
                seq_reveal += game_seq[game_seq.length-1]


                document.getElementById("status").textContent = seq_reveal;
            }
            
    });

}

function outputGuess(){ //currently unused, used for testing/debugging

    let guessVal1 = document.getElementById("color1").value;
    let guessVal2 = document.getElementById("color2").value;
    let guessVal3 = document.getElementById("color3").value;
    let guessVal4 = document.getElementById("color4").value;

    
    message = "You guessed: " + guessVal1 + " " + guessVal2 + " " + guessVal3 + " " + guessVal4;
    document.getElementById("status").textContent = message;
}

