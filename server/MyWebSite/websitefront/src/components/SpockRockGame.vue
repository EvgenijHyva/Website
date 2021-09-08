<template>
    <section>
        <div class="game-container">
            <div class="header">
                <h1>Rock-Paper-Scissors-Lizard-Spock</h1>
            </div>
            <div class="player-container" id="player">
                <h2>You - <span id="playerScore">{{playerScoreNumber}}</span>
                    <span class="choice" id="playerChoice"> {{playerChoice}}
                    </span>
                    <span id="small-container" >
                        <i class="far" 
                            :class="{ 'fa-hand-paper': playerChoice === 'paper', 
                                    'fa-hand-rock': playerChoice === 'rock',
                                    'fa-hand-scissors': playerChoice === 'scissors',
                                    'fa-hand-lizard': playerChoice === 'lizard',
                                    'fa-hand-spock': playerChoice === 'spock'}" 
                        id="small"></i>
                    </span>
                </h2>
                <i class="far fa-hand-rock" title="Rock" id="playerRock" @click="startGame" data-choice="rock" ref="player_rock"></i>
                <i class="far fa-hand-paper" title="Paper" id="playerPaper" @click="startGame" data-choice="paper" ref="player_paper"></i>
                <i class="far fa-hand-scissors " title="Scissors" id="playerScissors" @click="startGame" data-choice="scissors" ref="player_scissors"></i>
                <i class="far fa-hand-lizard" title="Lizard" id="playerLizard" @click="startGame" data-choice="lizard" ref="player_lizard"></i>
                <i class="far fa-hand-spock" title="Spock" id="playerSpock" @click="startGame" data-choice="spock" ref="player_spock"></i>
            </div>

            <div class="player-container" id="computer">
                <h2>Computer - <span id="computerScore">{{computerScoreNumber}}</span>
                    <span class="choice" id="computerChoice"> {{computerChoice}}     
                    </span>
                    <span id="small-container" >
                         <span id="small-container" >
                            <i class="far" 
                            :class="{ 'fa-hand-paper': computerChoice === 'paper', 
                                    'fa-hand-rock': computerChoice === 'rock',
                                    'fa-hand-scissors': computerChoice === 'scissors',
                                    'fa-hand-lizard': computerChoice === 'lizard',
                                    'fa-hand-spock': computerChoice === 'spock'}" 
                            id="small"></i>
                        </span>
                    </span>
                </h2>
                <i class="far fa-hand-rock" title="Rock" id="computerRock" ref="computer_rock"></i>
                <i class="far fa-hand-paper" title="Paper" id="computerPaper" ref="computer_paper"></i>
                <i class="far fa-hand-scissors" title="Scissors" id="computerScissors" ref="computer_scissors"></i>
                <i class="far fa-hand-lizard" title="Lizard" id="computerLizard" ref="computer_lizard"></i>
                <i class="far fa-hand-spock" title="Spock" id="computerSpock" ref="computer_spock"></i>
            </div>
            <!-- Reset Icon -->
            <i class="fas fa-sync-alt reset-icon" id="reset-icon" title="Reset" @click="resetAll"></i>
            <!-- Results-text -->
            <div class="result-container">
                <h3 class="result-text" id="resultText">{{resultText}}</h3>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: "SpockRockGame",
    data() {
        return {
            choices : {
                rock: { name: 'rock', defeats: ['scissors', 'lizard'] },
                paper: { name: 'paper', defeats: ['rock', 'spock'] },
                scissors: { name: 'scissors', defeats: ['paper', 'lizard'] },
                lizard: { name: 'lizard', defeats: ['paper', 'spock'] },
                spock: { name: 'spock', defeats: ['scissors', 'rock'] },
            },
            computerChoices: ["rock", "paper", "scissors", "lizard", "spock"],
            playerScoreNumber: 0,
            computerScoreNumber: 0,
            resultText: "Press a Choice Icon!",
            playerChoice : "--- Choices:",
            computerChoice: "--- Choices:",
        }
    },
    methods: {
        resetAll() {
            this.playerChoice = "--- Choices:",
            this.computerChoice= "--- Choices:",
            this.playerScoreNumber = 0
            this.computerScoreNumber = 0
            this.resultText = "Press a Choice Icon!"

            this.resetSelected()
        },
        startGame(iconEvent) {
            this.resetSelected()
            this.playerChoice = iconEvent.target.dataset.choice;
            let computerChoiceNum = Math.floor(Math.random() * this.computerChoices.length) 
            computerChoiceNum < this.computerChoices.length ? computerChoiceNum : 4
            this.computerChoice = this.computerChoices[computerChoiceNum]

            this.getWinner();

            this.$refs["player_" + this.playerChoice].classList.add("selected");
            this.$refs["computer_" + this.computerChoice].classList.add("selected");
            
        },
        getWinner() {
            if (this.playerChoice === this.computerChoice)
                this.resultText = `It's a tie. ${this.playerChoice} = ${this.computerChoice}`
            else {
                const choice = this.choices[this.playerChoice]
                if (choice.defeats.indexOf(this.computerChoice) > -1) {
                    this.playerScoreNumber++;
                    this.resultText = `You Won! "${this.playerChoice}" defeat "${this.computerChoice}"`
                } else {
                    this.computerScoreNumber++;      
                    this.resultText = `You Lost! "${this.computerChoice}" defeat "${this.playerChoice}"`
                }
            }
            localStorage.setItem("RPSLS", JSON.stringify({
                playerScoreNumber: this.playerScoreNumber,
                computerScoreNumber : this.computerScoreNumber,
                playerChoice : this.playerChoice,
                computerChoice : this.computerChoice
            }))
        },
        resetSelected() {
            for (let el in this.$refs) {
                this.$refs[el].classList.remove("selected")
            }
            localStorage.removeItem("RPSLS")
        },
    },
    mounted () {
      if (localStorage.RPSLS) {
          let storedData = JSON.parse(localStorage.RPSLS)
            this.playerScoreNumber = storedData.playerScoreNumber
            this.computerScoreNumber = storedData.computerScoreNumber
            this.playerChoice = storedData.playerChoice
            this.computerChoice = storedData.computerChoice
        }
    }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Reggae+One&family=Mountains+of+Christmas&family=Texturina&family=Orbitron&family=Source+Code+Pro:ital@1&display=swap');

.game-container {
  font-family: Texturina, 'Reggae One', "Source Code Pro", sans-serif ;
  border: 1px solid var(--header);
  width: 530px;
  height: 600px;
  background-color: var(--Spock-rock-game-primary-color);
  border-radius: 5px;
  box-shadow: 5px 15px 10px 5px var(--container-shadow-color);
  margin-top: 10vh;
  box-sizing: border-box;
}

.header {
  background: var(--header);
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
  font-family: Texturina;
  color: var(--Spock-rock-game-primary-color);
  font-size: 30px;
}

.player-container {
  margin: 30px 50px 50px 50px;
}

h2 {
  margin-bottom: 20px;
  color: var(--score-info);
}

.far {
  font-size: 50px;
  margin-right: 40px;
  User-select: none;
  text-shadow: 5px 7px 10px #775c43;;
}
.choice {
  text-transform: capitalize;
}

#player .far, 
#player .choice {
  color: var(--header);
  cursor: pointer;
}
#player .far:hover {
  filter: brightness(var(--mode-brightness));
}
#player .far:last-of-type,
#computer .far:last-of-type {
  margin-right: 0;
}

#computer .far,
#computer .choice {
  color: var(--computer-select-color);
}
#computer:hover {
  cursor:not-allowed;
}

#small-container {
  position: relative;
}

#small {
  transform: scale(0.5);
  position: absolute;
  bottom: -7px;
  color: green;
}
.fa-hand-rock:hover,.fa-hand-paper:hover,
.fa-hand-scissors:hover, .fa-hand-spock:hover {
    animation: rotate 3s;
}
.fa-hand-lizard:hover {
    animation: rotateY-axis 2s;
}

@keyframes rotateY-axis {
    0% {
        transform: rotateY(0deg);
    }
    50% {
        transform:rotateY(180deg)
    }
    100% {
        transform: rotateY(0deg);
    }
}

@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }   
    50% {
        transform: rotate(90deg);
    }
    100% {
        transform: rotate(0deg);
    }
}


#reset-icon:hover{
  animation: spin 1s
}

@keyframes spin {
  from{
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.selected {
  box-sizing: border-box;
  color: var(--selected-icon) !important;
  border-radius: 50px;
  font-weight: bold;
  filter: brightness(1.3);
}

.reset-icon {
  font-size: 30px;
  cursor: pointer;
}

.result-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.result-text {
  text-shadow: 5px 5px 7px #4848d2;
  font-size: 25px;
  margin: unset;
  margin-top: 20px;
}

/* Media Query: Large Smartphone (Vertical) */
@media screen and (max-width: 600px) {
  .game-container {
    width: 95vw;
    height: 580px;
  }

  h1 {
    font-size: 24px;
  }

  .player-container {
    margin: 50px 0 25px 25px;
  }

  .far {
    margin-right: 20px;
  }

  .reset-icon {
    margin-top: 25px;
    margin-left: 25px;
  }
  .result-text {
    font-size: 20px;
  }
}

/* Media Query: iPhone (Vertical) */
@media screen and (max-width: 376px) {
  .game-container {
    height: 550px;
  }

  h1 {
    font-size: 22px;
  }

  .player-container {
    margin: 43px 0 25px 20px;
  }

  .far {
    font-size: 43px;
  }

  .reset-icon {
    margin-top: 15px;
  }

  .result-container {
    margin: 0 20px;
  }
  .result-text {
    font-size: 20px;
  }
}

</style>