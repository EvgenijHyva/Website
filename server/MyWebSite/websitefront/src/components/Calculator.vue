<template>
    <section>
        <div class="wrapper">
            <div class="calculator">
                <div class="calculator-display">
                    <h1>{{ `${firstValue} ${operatorValue === "*" ? "x" : operatorValue} ${secondValue} ${ result }` }} </h1>
                </div>
                <div class="calculator-buttons">
                    <button value="+" class="operator" @click="selectOperator">+</button>
                    <button value="-" class="operator" @click="selectOperator">-</button>
                    <button value="*" class="operator" @click="selectOperator">x</button>
                    <button value="/" class="operator" @click="selectOperator">÷</button>
                    <button value="7" @click="selectValue">7</button>
                    <button value="8" @click="selectValue">8</button>
                    <button value="9" @click="selectValue">9</button>
                    <button value="4" @click="selectValue">4</button>
                    <button value="5" @click="selectValue">5</button>
                    <button value="6" @click="selectValue">6</button>
                    <button value="1" @click="selectValue">1</button>
                    <button value="2" @click="selectValue">2</button>
                    <button value="3" @click="selectValue">3</button>
                    <button value="." class="decimal" @click="addDecimal">.</button>
                    <button value="0" @click="selectValue">0</button>
                    <button class="clear" id="clear-btn" @click="resetAll" value="clear">C</button>
                    <button class="equal-sign operator" value="=" @click="selectOperator">=</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "Calculator",
    title() {
      return "Simple calculator"
    },
    data() {
        return {
            calcHistory: [],
            calculate: {
                "/": (firstNumber, secondNumber) => Number(firstNumber) / Number(secondNumber),
                "*": (firstNumber, secondNumber) => Number(firstNumber) * Number(secondNumber),
                "+": (firstNumber, secondNumber) => Number(firstNumber) + Number(secondNumber),
                "-": (firstNumber, secondNumber) => Number(firstNumber) - Number(secondNumber),
                "=": (firstNumber, secondNumber) => secondNumber
            },
            firstValue : 0,
            secondValue : "",
            operatorValue : "",
            resultReady : false,
            awaitingNextValue : false,
            result : ""
        }
    },
    methods: {
        reset() {
            this.result = "";
            this.secondValue = "";
            this.resultReady = false;
            this.awaitingNextValue = false;
        },
        resetAll() {
            this.operatorValue = "";
            this.firstValue = 0;
            this.reset();
        },
        selectOperator(e) {
            if (this.firstValue && !this.operatorValue) {
                this.operatorValue = e.target.value;
                this.awaitingNextValue = true;
            }
            else if (this.operatorValue && !this.resultReady && this.secondValue) {
                this.result = this.countResult()
                this.addHistory()
                this.firstValue = ""
                this.secondValue = ""
                this.operatorValue = ""
                this.resultReady = true
            }
            else if (this.resultReady && e.target.value) {
                this.firstValue = this.result
                this.operatorValue = e.target.value
                this.reset()
                this.awaitingNextValue = true
            }
        },
        selectValue(e) {
            if (this.resultReady && !this.firstValue) {
                this.resetAll()
            } 
            if (!this.operatorValue && !this.result) {
                this.firstValue ? this.firstValue += e.target.value : this.firstValue = e.target.value 
                }
            if (this.firstValue && this.operatorValue && !this.resultReady)
                this.secondValue ? this.secondValue += e.target.value : this.secondValue = e.target.value
        },
        addDecimal() {
            if (!`${this.firstValue}`.includes(".") && !this.awaitingNextValue) {
                this.firstValue = `${this.firstValue}.`
            }
            else if (this.awaitingNextValue && !`${this.secondValue}`.includes(".")) {
                this.secondValue = `${this.secondValue}.`
            }
        },
        countResult() {
            this.resultReady = true;
            this.awaitingNextValue = false;
            const result = this.calculate[this.operatorValue](this.firstValue, this.secondValue)
            return result
        },
        addHistory() {
            if (this.firstValue && this.operatorValue && this.secondValue && this.result) {
                let equation = `${this.firstValue} ${this.operatorValue} ${this.secondValue} ${ `${this.result}`.includes(".") ? "≈" : "=" } ${this.result.toFixed(2)}`
                this.calcHistory.push(equation)
            }
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Mate+SC&family=Shadows+Into+Light&family=Mate+SC&family=Stint+Ultra+Condensed&display=swap');

html {
  box-sizing: border-box;
}


h1 {
    color: var(--calculator-display-num-color);
    text-shadow: none;
}

.calculator {
  padding-top: 10px;
  background-position: bottom;
  background-color: var(--calculator-background);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cg fill='%237c699a' fill-opacity='0.4'%3E%3Cpath fill-rule='evenodd' d='M0 0h40v40H0V0zm40 40h40v40H40V40zm0-40h2l-2 2V0zm0 4l4-4h2l-6 6V4zm0 4l8-8h2L40 10V8zm0 4L52 0h2L40 14v-2zm0 4L56 0h2L40 18v-2zm0 4L60 0h2L40 22v-2zm0 4L64 0h2L40 26v-2zm0 4L68 0h2L40 30v-2zm0 4L72 0h2L40 34v-2zm0 4L76 0h2L40 38v-2zm0 4L80 0v2L42 40h-2zm4 0L80 4v2L46 40h-2zm4 0L80 8v2L50 40h-2zm4 0l28-28v2L54 40h-2zm4 0l24-24v2L58 40h-2zm4 0l20-20v2L62 40h-2zm4 0l16-16v2L66 40h-2zm4 0l12-12v2L70 40h-2zm4 0l8-8v2l-6 6h-2zm4 0l4-4v2l-2 2h-2z'/%3E%3C/g%3E%3C/svg%3E");
  width: 400px;
  border-radius: 20px;
  box-shadow: var(--calculator-shadow);
}

.calculator-display {
  background: rgb(17 36 47);
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  border-radius: 10px 10px 5px 5px;
  box-shadow: -3px 5px 9px 1px #424551;
  width: 95%;

}

.calculator-display h1 {
  margin: 0;
  padding: 25px;
  font-size: 45px;
  font-family: 'Mate SC' ,"Lucida Console", sans-serif ;
  font-weight: 100;
  overflow-x: auto;  /* if numbers exceed a display it will hide them*/
  user-select: none;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  height: 10px;
}
::-webkit-scrollbar-track {
  background: #5872ee;/*#d84747;*/
  border-radius: 0px 0px 5px 5px;
}
::-webkit-scrollbar-thumb {
  background:  linear-gradient(to right, #ff4e50, #f9d423); /*#7778af*/
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

/* buttons */

.calculator-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap:10px;
  padding: 10px;
}
.equal-sign {
  background: #b5a24b !important;
  grid-column: -2;
  grid-row: 2 / span 4 ;
}

button {
  background: #c1ac83;
  margin-right: 0;
  height: auto;
  min-width: 50px;
  min-height: 50px;
  font-size: 20px ;
  font-weight: 100;
  font-family: 'Mate SC' ,cursive;
  border: 1px solid #e7377447;
  cursor: pointer;
  border-radius: 5px;
  /*background: #9b9b9b9c; backgroundimage */
  box-shadow: -5px 6px 8px -2px #a40808 ;
  user-select: none;
}
button:hover {
  filter: brightness(1.2);
}
button:active {
  transform: translate(0, 3px);
  box-shadow: 0px 0px 10px 0px #002181;
}
button:focus {
  outline: none;
}
.operator {
  background: #009688;
  color: #24fd0a;
  font-size: 30px;
}
.operator:hover {
  filter: brightness(1.1);
}

.clear {
  background: #f85656;
  color: #200059;
  font-weight: 800;
}
.clear:hover {
  filter: brightness(0.9);
}

@media screen and (max-width:800px) {
  .calculator {
    width: 95vw;
  }
}
</style>