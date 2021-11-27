<template>
    <section id="projects">
    <!-- Projects -->
        <h1>This project was created using</h1>
        <div class="project-icons">
            <i class="fab fa-python" title="Python"></i>
            <i class="fab fa-js" title="JavaScript"></i>
            <i class="fab fa-vuejs" title="Vue.js"></i>
            <i class="fab fa-html5" title="Html 5"></i>
            <i class="fab fa-bootstrap" title="Bootstrap 4"></i>
            <i class="fab fa-font-awesome" title="Font-awesome"></i>
        </div>
    </section>
</template>

<script>
export default {
    name: "Projects", 
}
</script>

<style>
/* Projects Section */
.buttons {
  margin-top: 15px;
  margin-bottom: 50px;
}

button {
  min-width: 100px;
  height: 40px;
  cursor: pointer;
  border-radius: 10px;
  margin-right: 10px;
  border: 2px solid var(--primary-color);
  font-size: 15px;
  outline: none;
}

button:disabled {
  opacity: 0.4;
  cursor: default;
}

button:hover:not(.outline) {
  filter: brightness(110%);
}

.primary {
  background: var(--primary-color);
  color: var(--on-primary);
}

.secondary {
  border: 2px solid var(--secondary-color);
}

.secondary,
.secondary:hover,
.outline.secondary:hover {
  background: var(--secondary-color);
  color: var(--on-primary);
}

.outline {
  background: var(--background);
  color: var(--on-background);
}

.outline:hover {
  background: var(--primary-color);
  color: var(--on-primary);
}


.project-icons {
  display: flex;
  flex-wrap: wrap;
  margin: 40px 0 20px ;
}
.project-icons .fab{
  font-size: 70px;
  cursor: none;
  padding: 0 10px;
}
.project-icons .fab:hover {
  color: transparent;
}

p {
  margin: 0;
  line-height: 25px;
}

@media screen and (max-width: 600px) { 
  button {
    font-size: 12px;
    min-width: 25vw;
    height: 4.5vh;
    margin: 2vw;
  }
 
}
</style>