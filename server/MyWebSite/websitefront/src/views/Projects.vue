<template>
    <section id="projects">
    <!-- Projects -->
        <h1>Buttons</h1>
        <div class="buttons">
            <button class="primary">Primary</button>
            <button class="secondary">Secondary</button>
            <button class="primary" disabled>Disabled</button>
            <button class="outline">Outline</button>
            <button class="secondary outline">Alt Outline</button>
            <button class="outline" disabled>Disabled</button>
        </div>
        <div class="text-box" id="text_box">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odio, cumque! Lorem ipsum dolor sit, amet
                consectetur adipisicing elit. Id vitae ratione, nobis optio rem nulla.
            </p>
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

.text-box {
  width: 40%;
  text-align: justify;
  background-color: var(--text-box);
  color: var(--on-primary);
  border-radius: 10px;
  padding: 30px;
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