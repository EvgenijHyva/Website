<template>
    <section>
        <h1 class="main-title">Drag&drop kanban Board</h1>
    <div class="drag-container">
        <ul class="drag-list">
            <!-- Backlog -->
            <li class="drag-column backlog-column">
                <span class="header">
                    <h1>Backlog</h1>
                </span>
                <!-- Content -->
                <div id="backlog-content" class="custom-scroll" @drop="drop" data-column="Backlog"> 
                    <ul class="drag-item-list" id="backlog-list" data-column="Backlog"
                        :class="{ 'over' : enterColumn==='Backlog'}"
                        @dragover.prevent
                        @dragenter="dragEnter">
                      <transition-group name="Animate_tasks"
                        enter-active-class="animate__animated animate__flipInX"
                        leave-to-class="animate__animated animate__flipOutX">
                        <li class="drag-item" draggable="true" :data-key="key"
                          v-for="item, key in columns['Backlog']" :key="key"
                          @dragstart="drag"
                          @blur="updateItem"
                          :contenteditable="!dragging"
                          title="Edit">
                            {{item}} 
                        </li>
                      </transition-group>
                    </ul>
                </div>
                <div class="add-btn-group" data-column="Backlog">
                    <div class="add-btn" @click="showInputBox" >
                        <span class="plus-sign">+</span>
                        <span>Add Item</span>
                    </div>
                    <div class="add-btn solid" @click="saveAndHideInputBox">
                        <span>Save Item</span>
                    </div>
                </div>
                <div class="add-container" ref="Backlog" >
                    <div class="add-item" contenteditable="true"></div>
                </div>
                
            </li>
        </ul>
        <ul class="drag-list" >
            <!-- Progress -->
            <li class="drag-column progress-column">
                <span class="header">
                    <h1>Progress</h1>
                </span>
                <!-- Content -->
                <div id="progress-content" class="custom-scroll" @drop="drop" data-column="Progress">
                    <ul class="drag-item-list" id="progress-list" data-column="Progress"
                      :class="{ 'over' : enterColumn==='Progress'}"
                      @dragover.prevent
                      @dragenter="dragEnter" >
                      <transition-group name="Animate_tasks"
                        enter-active-class="animate__animated animate__flipInX"
                        leave-to-class="animate__animated animate__flipOutX">
                        <li class="drag-item" draggable="true" :data-key="key"
                            v-for="item, key in columns['Progress']" :key="key"
                            @dragstart="drag"
                            @blur="updateItem"
                            :contenteditable="!dragging"
                            title="Edit">
                            {{item}}
                        </li>
                      </transition-group>
                    </ul>
                </div>
                <div class="add-btn-group" data-column="Progress">
                    <div class="add-btn" @click="showInputBox" >
                        <span class="plus-sign">+</span>
                        <span >Add Item</span>
                    </div>
                    <div class="add-btn solid" @click="saveAndHideInputBox">
                        <span>Save Item</span>
                    </div>
                </div>
                <div class="add-container" ref="Progress" >
                    <div class="add-item" contenteditable="true"></div>
                </div>

            </li>
        </ul>
        <ul class="drag-list" >
            <!-- On-hold -->
            <li class="drag-column on-hold-column">
                <span class="header">
                    <h1>On-hold</h1>
                </span>
                <!-- Content -->
                <div id="on-hold-content" class="custom-scroll" @drop="drop" data-column="OnHold">
                    <ul class="drag-item-list" id="on-hold-list" data-column="OnHold"
                      :class="{ 'over' : enterColumn==='OnHold'}"
                      @dragover.prevent
                      @dragenter="dragEnter" >
                      <transition-group name="Animate_tasks"
                        enter-active-class="animate__animated animate__flipInX"
                        leave-to-class="animate__animated animate__flipOutX">
                        <li class="drag-item" draggable="true" :data-key="key"
                            v-for="item, key in columns['OnHold']" :key="key"
                            @dragstart="drag"
                            @blur="updateItem"
                            :contenteditable="!dragging"
                            title="Edit">
                            {{item}}
                        </li>
                      </transition-group>
                    </ul>
                </div>
                <div class="add-btn-group" data-column="OnHold">
                    <div class="add-btn" @click="showInputBox" >
                        <span class="plus-sign">+</span>
                        <span >Add Item</span>
                    </div>
                    <div class="add-btn solid" @click="saveAndHideInputBox" >
                        <span>Save Item</span>
                    </div>
                </div>
                <div class="add-container" ref="OnHold" >
                    <div class="add-item" contenteditable="true"></div>
                </div>
            </li>
        </ul>
        <ul class="drag-list" >
            <!-- Complete -->
            <li class="drag-column complete-column">
                <span class="header">
                    <h1>Complete</h1>
                </span>
                <!-- Content -->
                <div id="complete-content" class="custom-scroll" @drop="drop" data-column="Complete">
                    <ul class="drag-item-list" id="complete-list" data-column="Complete"
                      :class="{ 'over' : enterColumn==='Complete'}"
                      @dragover.prevent
                      @dragenter="dragEnter" >
                      <transition-group name="Animate_tasks"
                        enter-active-class="animate__animated animate__flipInX"
                        leave-to-class="animate__animated animate__flipOutX">
                        <li class="drag-item" draggable="true" :data-key="key"
                            v-for="item, key in columns['Complete']" :key="key"
                            @dragstart="drag"
                            @blur="updateItem"
                            :contenteditable="!dragging"
                            title="Edit">
                            {{item}}
                        </li>
                      </transition-group>
                    </ul>
                </div>
                <div class="add-btn-group" data-column="Complete">
                    <div class="add-btn" @click="showInputBox" >
                        <span class="plus-sign">+</span>
                        <span >Add Item</span>
                    </div>
                    <div class="add-btn solid" @click="saveAndHideInputBox" >
                        <span>Save Item</span>
                    </div>
                </div> 
                <div class="add-container" ref="Complete" >
                    <div class="add-item" contenteditable="true"></div>
                </div>
            </li>
        </ul>
    </div>
    </section>
</template>

<script>
export default {
    name: "Kanban",
    title() {
      return "Kanban Board"
    },
    data() {
        return {
            columns : {
              "Backlog" : {},
              "Progress" : {},
              "OnHold" : {},
              "Complete": {}
            },
            draggedColumn: "",
            draggedTask : "",
            dragging : false,
            enterColumn : ""
        }
    },
    methods: {
        drag(e) {
            this.draggedColumn = e.target.parentElement.dataset.column
            this.draggedTask = e.target;
            this.dragging = true;
        },
        dragEnter(e) {
            if (e.target.dataset.column) 
              this.enterColumn = e.target.dataset.column
        },
        drop(e) {
            let column = e.target.parentElement.dataset.column
            //assign property inside a Drop column
            if (this.draggedColumn !== column) {
              let key = this.draggedTask.textContent +`${'_item_'+Object.keys(this.columns[column]).length}`
              let item = this.draggedTask.textContent
              this.columns[column][key] = item
              //delete property from Dragged column
              delete this.columns[this.draggedColumn][this.draggedTask.dataset.key]
            }
            this.dragging = false
            this.enterColumn = ""
        },
        updateItem(event) {
            let item = event.target.textContent
            let key = event.target.dataset.key
            let column = event.target.parentElement.dataset.column
            if (item && item.trim().length)
              this.columns[column][key] = item
            else
              delete this.columns[column][key]
        },
        showInputBox(event) {
          let column = event.currentTarget.parentElement.dataset.column // currentTarget = component with event
          this.$refs[column].style.display = "flex" //shows a text field 
          this.$refs[column].children[0].focus() // focus on text field
          this.$refs[column].parentElement.children[2].children[1].style.display="flex" // show hidden button
        },
        saveAndHideInputBox(event) {
          let column = event.currentTarget.parentElement.dataset.column
          this.$refs[column].style.display = "none" //hide a text field
          this.$refs[column].parentElement.children[2].children[1].style.display="none" //hide button
          let item =  this.$refs[column].children[0].textContent
          if (item && item.trim().length) {
            let key = item + `${'_item_'+ Object.keys(this.columns[column]).length}`
            this.columns[column][key] = item
            this.$refs[column].children[0].textContent = ""
          }
        },
        saveToLocalStorage() {
          localStorage.setItem("Kanban", JSON.stringify(this.columns))
        },
        getFromLocalStorage() {
          let local = localStorage.getItem("Kanban")
          if (local) {
            this.columns = JSON.parse(local)
          }     
        },
        saveToDB() {
          //actions to load data to Data Base
        }
    },
    beforeMount: function () {
      this.getFromLocalStorage()
    },
    watch: {
      columns : {
        handler () {
          this.saveToLocalStorage()
        },
        deep:true
      },
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Quicksand&display=swap");
.animate__animated {
  animation-duration: 1.5s;
}

h1 {
  letter-spacing: 2px;
  text-shadow: 2px 2px 5px black;
  font-family: 'Quicksand';
  margin: 1vh;
}

.main-title {
  text-align: center;
  font-size: 3rem;
  color: var(--title-alt);
  text-shadow: 10px 18px 5px var(--title-shadow);
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.drag-container {
  margin: 20px;


  display: flex;
}

.drag-list {
  max-width: 50vw;
  display: flex;
  align-items: flex-start;
  flex-grow: 1;
}

/* Columns */
.drag-column {
  max-height: 50vh;
  flex:1;
  margin: 0 10px;
  position: relative;
  background-color: var(--kanban-drag-column);
  border-radius: 10px;
  overflow-x: hidden;
  z-index: 10;
  width: 20vw;
}

.backlog-column .header,
.backlog-column .solid,
.backlog-column .solid:hover {
  background-color: var(--column-1);
}

.backlog-column .over {
  background-color: var(--column-1-alt)
}

.progress-column .header,
.progress-column .solid,
.progress-column .solid:hover {
  background-color: var(--column-2);
}

.progress-column .over {
  background-color: var(--column-2-alt);
}

.complete-column .header,
.complete-column .solid,
.complete-column .solid:hover {
  background-color: var(--column-3);
}

.complete-column .over {
  background-color: var(--column-3-alt);
}

.on-hold-column .header,
.on-hold-column .solid,
.on-hold-column .solid:hover {
  background-color: var(--column-4);
}
.on-hold-column .over {
  background-color: var(--column-4-alt);
}
/* Custom Scrollbar */
.custom-scroll {
  overflow-y: auto;
  max-height: 75vh;
}

.custom-scroll::-webkit-scrollbar-track {
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.4);
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.3);
  margin-right: 5px;
}

.custom-scroll::-webkit-scrollbar {
  width: 10px;
}

.custom-scroll::-webkit-scrollbar-thumb {
  border-radius: 10px;
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: rgba(0, 0, 0, 0.8);
}

.header {
  display: flex;
  justify-content: center;
  border-radius: 10px;
  margin: 10px;
}

.header h1 {
  font-size: 1.25rem !important;
  color: #9dc10cc7
}

/* Drag and Drop */
.over {
  padding: 10px 0;
}

.drag-item-list {
  min-height: 50px;
}

.drag-item {
  margin: 5px 5px;
  padding: 10px;
  height: fit-content;
  background-color: var(--kanban-li-back);
  border-radius: 10px;
  line-height: 1.5rem;
  letter-spacing: 1px;
  cursor: pointer;
  user-select: initial;
}
.drag-list li,.drag-list span {
  color: whitesmoke;
}


.drag-item:focus {
  outline: none;
  background-color: white;
  color: black;
}

/* Add Button Group */
.add-btn-group {
  display: flex;
  justify-content: space-between;
}

.add-btn {
  z-index: 10;
  margin: 10px;
  padding: 5px 10px;
  display: flex;
  align-items: center;
  cursor: pointer;
  width: fit-content;
  border-radius: 5px;
  transition: all 0.3s ease-in;
  user-select: none;
}

.add-btn:hover {
  background-color: rgba(255, 255, 255, 0.9);
  color: black;
}

.add-btn:active {
  transform: scale(0.97);
}

.solid {
  display: none;
}

.solid:hover {
  transition: unset;
  filter: brightness(95%);
  color: white;
}

.plus-sign {
  font-size: 1.5rem;
  margin-right: 5px;
  position: relative;
  top: -3px;
}

.add-container {
  margin: 10px;
  padding: 5px 10px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.9);
  min-height: 100px;
  display: none;
}

.add-item {
  width: 100%;
  min-height: 100px;
  height: auto;
  background-color: white;
  border-radius: 10px;
  margin: 5px auto;
  resize: none;
  color: black;
  padding: 10px;
  text-align: left;
}

.add-item:focus {
  outline: none;
}

/* Media Query: Large Smartphone (Vertical) */
@media screen and (max-width: 800px) {
  body {
    overflow-y: auto;
  }
  .drag-container {
    margin: 0;
    /* changed*/
    width: 100vw;
    max-height: 50vh;
    display: flex;
    flex-wrap: wrap;
  }

  .drag-list {
    max-width: 50vw;
    display: block;
  }

  .drag-column {
    
    margin: 10px;
    /* changed */
    width: 45vw;
    max-height: 35vh;
  }
  .header {
    padding: 5px;
    margin: 5px;
    position: sticky;
    top: 0;
  }
  .main-title {
    font-size: 2.3rem;
  }
  .add-item {
    box-sizing: border-box;
    min-height: 5vh;
  }

}
</style>