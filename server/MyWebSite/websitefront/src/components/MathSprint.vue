<template>
    <section>
        <div class="game-container">
            <div class="header">
                <h1>Math sprint Game</h1>
            </div>
            <!-- Splash Page -->
            <div class="card" id="splash-page" ref="splashPage" >
                <vee-form id="start-form" @submit="createEquations" >
                    <div class="selection-container" >
                        <div class="radio-container" 
                        :class="{'selected-label': equetionsValue === '10'}"
                        @click="selectInput">
                            <label for="value-10">10 questions</label>
                            <vee-field type="radio" id="value-10" name="questions" value="10" />
                        </div>
                        <div class="radio-container" @click="selectInput"
                        :class="{'selected-label': equetionsValue === '25'}"
                        >
                            <label for="value-25">25 questions</label>
                            <vee-field type="radio" id="value-25" name="questions" value="25" />
                        </div>
                        <div class="radio-container" @click="selectInput"
                        :class="{'selected-label': equetionsValue === '50'}">
                            <label for="value-50">50 questions</label>
                            <vee-field type="radio" id="value-50" name="questions" value="50" /> 
                        </div>
                        <div class="radio-container" @click="selectInput"
                        :class="{'selected-label': equetionsValue === '99'}"> 
                            <label for="value-99">99 questions</label>
                            <vee-field type="radio" id="value-99" name="questions" value="99" />
                        </div>
                    </div>
                    <div class="selection-footer">
                        <button class="start" type="submit">Start Round</button>
                    </div>
                </vee-form>
            </div>
            <!-- Countdown Page -->
            <div class="card" id="countdown-page"  ref="countdownPage" hidden >
                <h1 class="countdown"> {{ countdown }} </h1>
            </div>
            <div class="card" id="game-page" hidden ref="gamePage" >
                <!--item container -->
                <div class="height-240"></div>
                <div class="selected-item"></div>
                <div class="item-container" ref="container">
                  <transition-group name="fade" mode="out-in"
                      leave-to-class="animate__animated animate__zoomOutDown">
                    <div class="item" v-for="item in equetions" :key="item">
                        <h1 v-if="item">{{ item.value }}</h1>
                    </div>
                  </transition-group>
                <div class="height-500"></div>
                </div>
                <!-- Right/wrong -->
                <div class="item-footer" @click="selectAnswer">
                    <button class="wrong"  data-answer="false" value="false">Wrong</button>
                    <button class="right" data-answer="true" value="true">Right</button>
                </div>
            </div>
            <div class="card" id="score-page" hidden ref="scorePage" >
                <!-- Score container -->
                <div class="score-container">
                    <h1 class="title">Your Time</h1>
                    <h1 class="final-time"> Final time: {{ finalTime.toFixed(2) }}s</h1>
                    <h1 class="base-time">Time played: {{ timePlayed.toFixed(2) }}s</h1>
                    <h1 class="penalty-time">Pinalty time: {{ penaltyTime.toFixed(2) }}s</h1>
                    <h1 class="title">Answers</h1>
                    <h1 class="base-time">Right answers: {{rightAnswers}} </h1>
                    <h1 class="penalty-time">Wrong answers: {{wrongAnswers}} </h1>
                </div>
                <!-- Play again -->
                <div class="score-footer">
                    <button class="play-again" @click="playAgain" >Play Again</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "MathSprint",
    title() {
      return "Math sprint game"
    },
    data () {
        return {
          answeredEquetions: [],
          equetions : [],
          equetionsValue: 0, // for classes and form
          playerGuesses: [],
          wrongAnswers: 0,
          rightAnswers: 0,
          timePlayed : 0,
          penaltyTime: 0,
          finalTime: 0,
          interval: null,
          isRunning: false,
          countdown: "",
        }
    },
    methods: {
      selectAnswer(event) {
        if (!event.target.value || !this.equetions.length) 
          return
        let answer = event.target.value
        this.answeredEquetions.push(this.equetions.shift())
        this.playerGuesses.push(answer)
      },
      selectInput (event) {
        event.currentTarget.children[1].checked = "true"
        this.equetionsValue = event.currentTarget.children[1].value
      },
      getRandomNumber(number) {
        return Math.floor(Math.random() * Math.floor(number))
      },
      createEquations () {
        if (!this.equetionsValue)
          return
        this.equetions = []
        let correctEquations = this.getRandomNumber(this.equetionsValue)
        let wrongEquations = this.equetionsValue - correctEquations

        for(let i = 0; i < correctEquations; i++) {
          let firstNumber = this.getRandomNumber(29)
          let secondNumber = this.getRandomNumber(10)
          const equationResult = firstNumber * secondNumber;
          const equation = `${firstNumber} x ${secondNumber} = ${equationResult}`
          this.equetions.push({ value: equation, evaluated: "true" })
        }

        for(let i = 0; i < wrongEquations; i++) {
          let firstNumber = this.getRandomNumber(56);
          let secondNumber = this.getRandomNumber(35);
          const equationResult = firstNumber * secondNumber;
          const formatChoice = this.getRandomNumber(4);
          let wrongFormat = {
            0 : `${firstNumber} x ${secondNumber + 1} = ${equationResult}`,
            1 : `${firstNumber} x ${secondNumber} = ${equationResult - 1}`,
            2 : `${firstNumber + 1} x ${secondNumber} = ${equationResult + 10}`,
            3 : `${firstNumber + 4} x ${secondNumber * 2} = ${equationResult + 6}`,
            4 : `${firstNumber + 7} x ${secondNumber % firstNumber} = ${equationResult % firstNumber}`
          }
          const equation = wrongFormat[formatChoice];
          this.equetions.push({ value: equation, evaluated: "false" })
        }
        this.shuffle()
        //console.log()
        this.$refs["splashPage"].hidden = true
        this.$refs["countdownPage"].hidden = false
        this.countdownMethod()
      },
      shuffle() {
        let currentIndex = this.equetions.length
        while (0 !== currentIndex) {
          let randomIndex = Math.round(Math.random() * currentIndex)
          currentIndex--
          let temporaryValue = this.equetions[currentIndex]
          this.equetions[currentIndex] = this.equetions[randomIndex]
          this.equetions[randomIndex] = temporaryValue
        }
      },
      countdownMethod() {
        const countValues = [3, 2, 1, "GO!", ""];
        let i = 0;
        let countdownObjectt = setInterval(() => {
          this.countdown = countValues[i]
          i++;
          if (i === countValues.length) {
            clearInterval(countdownObjectt)
            this.$refs["countdownPage"].hidden = true
            this.$refs["gamePage"].hidden = false
            this.toggleTimer()
          }
        }, 1000);
        
      },
      toggleTimer() {
        if (this.isRunning){
          clearInterval(this.interval);
        } else {
          this.interval = setInterval(this.addTime, 100);
        } 
        this.isRunning = !this.isRunning
      },
      addTime() {
        this.timePlayed += 0.1
      },
      gameOver() {
        this.toggleTimer()
        this.getResults()
        this.$refs["gamePage"].hidden = true
        this.$refs["scorePage"].hidden = false
      },
      getResults() {
        this.playerGuesses.forEach((guess, i )=> {
          if (guess === this.answeredEquetions[i].evaluated) {
            this.rightAnswers++
          } else {
            this.wrongAnswers++
          }
        });
        this.playerGuesses.splice(0, this.playerGuesses.length)
        this.answeredEquetions.splice(0, this.answeredEquetions.length)
        this.getPenaltytime()
        this.getFinalTime()
      },
      getPenaltytime() {
        this.penaltyTime = this.wrongAnswers * 1.1 * (this.wrongAnswers / this.equetionsValue)
      },
      getFinalTime() {
        this.finalTime = this.penaltyTime + this.timePlayed
      },
      playAgain() {
        this.$refs["scorePage"].hidden = true
        this.$refs["splashPage"].hidden = false
        this.wrongAnswers = 0
        this.rightAnswers = 0
        this.timePlayed = 0
      }
    },
   
    watch: {
      "equetions.length": function () {
        if (this.equetions.length === 0) {
          setTimeout(this.gameOver, 1000)
        }
      }
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Oxanium|PT+Mono&display=swap");
.animate__animated {
  animation-duration: 1s;
}

section {
    padding-top: 5vh;
}
.game-container h1 {
    color: #fbff00bd;
    margin: auto;
    font-size: 5vh;
    text-shadow: 1px 2px 2px black;
}
::-webkit-scrollbar {
    width: 0px;
    height: 0;
}
.game-container {
  border: 1px solid black;
  box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.5);
  max-width: 40vw;
  width: 35vw;
  height: var(--screen-width);
  position: relative;
  background: rgba(255, 255, 255, 0.5);
  user-select: none;
  margin: 11vh 0 auto ;
}

.header {
  background: var(--math-primary-color);
  color: white;
  font-family: Oxanium, sans-serif;
  font-size: 5vh;
  text-shadow: 1px 2px 2px black;
  letter-spacing: 2px;
  height: var(--header-screen-width);
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  height: 70vh;
  position: absolute;
  width: 100%;
}
#start-form {
    position: absolute;
    width: 100%;   
    height: 100%; 
}
#countdown-page h1{
    top: 35%;
    position: absolute;
    left: 45%;
}

.selection-container {
  height: 60vh;
  overflow: scroll;
}

/* Splash Page -------------------- */
input[type="radio"] {
  opacity: 0;
  width: 100%;
  cursor: pointer;
  z-index: 2;
}

.radio-container {
  width: 90%;
  cursor: pointer;
  border: 2px solid black;
  border-radius: 5px;
  margin: 2vh auto;
}

label {
  font-size: 30px;
}

.selected-label {
  background: var(--select-color);
  color: white;
  animation: blinking 4s infinite ;
}

@keyframes blinking {
  0% {
    opacity: 0.5;
  }
  25% {
    opacity: 0.7;
    background-color: green;
    color: cornflowerblue;
  }
  50% {
    opacity: 0.5;
  }
  75% {
    opacity: 0.7;
    background-color: rgb(56, 49, 71);
    color:coral;
  }
  100%{
    opacity: 0.5;
  }
  
}

.best-score {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  font-size: 18px;
  max-width: fit-content;
  z-index: 10;
}

.best-score span {
  margin: 0;
}

.best-score-detail-info {
  font-size: 10px;
  text-align: center;
  display: none;
}
.best-score:hover .best-score-detail-info {
  display:inline;
  color: green;
}
.best-score:hover .best-score-value {
  font-size: 15px;
}
.best-score:hover {
  text-align: left;
}


.best-score span:last-child {
  font-size: 24px;
}

.selection-footer {
  height: var(--header-screen-width);

}

/* Game Page -------------------------- */
.height-240 {
  height: 25vh;
  width: 100%;
}

.height-500 {
  height: 30.5vh;
  width: 100%;
}

.item-container {
  height: 37vh;
  overflow-y: scroll;
  position: relative;
  -ms-overflow-style: none;
}

.item-container::-webkit-scrollbar {
  display: none;
}

.item {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  user-select: none;
}
.item h1{
    font-family: PT Mono, sans-serif;
    margin: 1vh 20px 1vh 10px;
    font-size: 4vh;
    color: var(--mode-text);
}

.finished > h1 {
  opacity: 0.5;
}

.selected-item {
    background: var(--select-color);
    height: 6.5vh;
    width: 100%;
    position: absolute;
    z-index: -1;
    top: 25vh;
}

.item-footer,
.selection-footer {
    width: 100%;
    background: rgba(0, 0, 0, 1);
    display: flex;
    justify-content: center;
    align-items: center;
    bottom: -1px;
    position: absolute;
    padding: 15px 0;    
}

button {
  cursor: pointer;

  border-radius: 5px;
  font-size: 25px;
  font-family: Oxanium, sans-serif;
  color: white;
  border: none;
  outline: none;
  margin: auto;
}

button:hover {
  filter: brightness(110%);
}

button:active {
  transform: scale(0.99);
}

.wrong,
.right {
  width: 40%;
}

.wrong {
  background: var(--danger);

}

.right {
  background: var(--success);
}

.start,
.play-again {
  width: 90%;
  background: var(--primary-color);
}

/* Countdown Page ---------------------- */
.countdown {
  font-family: PT Mono,sans-serif;
  text-align: center;
  user-select: none;
  cursor:none;
  animation: numBlincking 5s infinite;
}

@keyframes numBlincking {
  0% {
    transform: scale(2);
    color:red
  }
  15%{
    transform: scale(0.5);
  }
  25% {
    transform: scale(2);
    color: chocolate;
  }
  35%{
    transform: scale(0.5);
  }
  50% {
    transform: scale(2);
    color: rgb(7, 74, 142);
  }
  60%{
    transform: scale(0.5);
  }
  75% {
    transform: scale(2);
    color:green
  }
  100% {
    transform: scale(1.5);
    color: darkgreen;
  }
}

/* Score Page ------------------------- */
.score-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.score-container h1{
    font-family: PT Mono, sans-serif;
    margin: 1vh 20px 1vh 10px;
    font-size: 4vh;
    color: var(--mode-text);
}

.score-footer {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 20px;
    background: black;
    box-sizing: border-box;
    position: absolute;
    bottom: -1px;
}

.title {
  color: var(--title) !important;
}

.final-time {
  font-size: 35px;
  margin: 0;
  color: var(--success) !important;
}

.base-time {
  color: yellowgreen !important;
}

.penalty-time {
  color: var(--danger) !important;
}


/* Media Query: Large Smartphone (Vertical) */
@media screen and (max-width: 500px) {
  .game-container {
    border: none;
  }

  .header {
    font-size: 1.2rem;
  }

  .countdown {
    margin-top: 60%;
  }

  .selection-container {
    top: 100px;
  }

  .radio-container {
    width: 93%;
    margin: 15px;
  }

  label {
    font-size: 1.7rem;
  }

  .best-score {
    font-size: 1rem;
    left: 245px;
  }
}
@media screen and (max-width: 1024px) {
    .game-container{
     margin: auto;
     max-width: 80vw;
     width: 70vw;
  }
}

/* Media Query: iPhone */
@media screen and (max-width: 600px) {
  .game-container{
     margin: auto;
     max-width: 100vw;
     width: 95vw;
  }
  .best-score {
    left: 232px;
  }
  .final-time {
    font-size: 30px;
    font-weight: 800;
  }
  .best-score-detail-info {
    position: absolute;
    bottom: -25px;
    left: -170px;
  }
}

</style>