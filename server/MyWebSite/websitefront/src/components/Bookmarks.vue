<template>
    <section>
        <h1 id="show-modal" @click="showModal = !showModal" >Add Bookmark</h1>
          <div class="container" id="bookmarks-container">
            <transition-group name="flip"
                        enter-active-class="animate__animated animate__flipInX"
                        leave-to-class="animate__animated animate__flipOutX" >
                <div class="item"  v-for="item in bookmarks" :key="item.websiteUrl">
                    <i class="fas fa-times" id="delete-bookmark" @click="deleteBookmark" :data-url="item.websiteUrl"></i>
                    <div class="name">
                        <img :src="item.icon" alt="img">
                        <a :href="item.websiteUrl" target="_blank" :title="item.websiteName">{{item.websiteName}}</a>
                    </div>
                </div>
              </transition-group>
          </div>
        
        <div class="modal-container" id="modal" :class="{ 'show-modal': showModal }">
            <div class="modal">
                <i class="fas fa-times close-icon" id="close-modal" @click="showModal = !showModal"></i>
                <div class="modal-header">
                    <h3>Add Bookmark</h3>
                </div>
                    <div class="modal-content">
                        <vee-form id="bookmark-form" 
                        :validation-schema="formSchema"
                        @submit="createBookmark">
                            <!-- Website Name -->
                            <div class="form-group">
                                <label for="websiteName" class="form-label">Website Name</label>
                                <vee-field name="websiteName" type="text" class="form-input" id="website-name" > </vee-field>
                                <ErrorMessage name="websiteName"  class="error-message" />
                            </div>
                            <div class="form-group">
                                <label for="websiteUrl" class="form-label">Website Url</label>
                                <vee-field name="websiteUrl" type="text" class="form-input" id="website-url" > </vee-field>
                                <ErrorMessage name="websiteUrl"  class="error-message" />
                            </div>
                            <div>
                                <button type="reset">Reset</button>
                                <button type="submit">Save</button>
                            </div>
                        </vee-form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "Bookmarks",
    title() {
      return "Your bookmarks"
    },
    data() {
        return {
            bookmarks: {},
            showModal: false,
            formSchema: {
                websiteName: "required|min:1|max:50",
                websiteUrl: "required|url"
            },
        }
    },
    methods: {
        createBookmark(bookmark, actions) {
            bookmark.icon = `https://www.google.com/s2/u/0/favicons?domain=${bookmark.websiteUrl}`;
            this.bookmarks[bookmark.websiteUrl] = bookmark;
            this.showModal = false;
            this.updateLocalstorage();
            actions.resetForm();
        },
        deleteBookmark(e) {
            delete this.bookmarks[e.target.dataset.url];
            this.updateLocalstorage();
        },
        updateLocalstorage() {
            localStorage.bookmarks = JSON.stringify(this.bookmarks)
        },
    },
    mounted () {
      if (localStorage.bookmarks)
        this.bookmarks = JSON.parse(localStorage.bookmarks)
    }
  
}
</script>

<style scoped>
.animate__animated{
  animation-duration: 1s;
}


h1 {
  text-align: center;
  font-size: 40px;
  padding:20px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: var(--border-radius);
  cursor: pointer;
  text-transform: uppercase;
  margin: 20px auto 10px;
  user-select: none;
  font-family: "Karla", sans-serif;
  text-shadow: 2px 7px 15px var(--bookmarks-title-shadow);
}

h1:hover {
  background: rgba(0, 0, 0, 0.6);
}

label {
    padding: 5px;
}

/* Bookmarks */
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.item {
  background: rgba(0, 0, 0, 0.75);
  color: whitesmoke;
  border-radius: 20px;
  padding: 15px;
  margin: 10px;
  position: relative;
}

.item:hover {
  background: rgba(0, 0, 0, 0.6);
}

a {
  font-size: 20px;
  font-weight: bold;
  text-transform: uppercase;
}

a:link, a:visited {
  color: var(--bookmarks-link);
  text-decoration: none ;
}

a:hover, a:active {
  text-decoration: overline;
}
.fa-times {
  cursor: pointer;
  position: absolute;
  right: 5px;
  top: 5px;
  font-size: 1.2rem;
  color: #91ff2d;
}
.name {
  margin-right: 20px;
  margin-top: 20px;
  margin: auto;
}

.name img {
  height: 20px;
  width: 20px;
  margin-right: 5px;
  vertical-align: sub;
}

.modal-container {
  background: rgba(0, 0, 0, 0.5);
  display: none;
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
}
.show-modal {
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
  max-width: 95%;
  width: 500px;
  animation: modalopen 1.5s;
}

@keyframes modalopen {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.close-icon {
  float:right;
  color: white;
  font-size: 24px;
  position: relative;
  top: 13px;
  right: 13px;
  cursor: pointer;
}

.modal-header {
  background: var(--primary-color);
  color: white;
  padding: 15px;
}

h3 {
  margin: 0;
}

.modal-content {
  padding: 20px;
  background-color: whitesmoke;
}

/* Form */
.form-group {
    height: 75px;
    display: flex;
    flex-direction: column;
}

.error-message {
    margin: 4px;
}
.form-input {
  width: 97%;
  padding: 5px;
  border: 2px solid var(--primary-color); 
  border-radius: var(--border-radius);
  display: block;
  outline: none;
}
.form-label {
  color: var(--primary-color);
  display: block;
}
button {
  cursor: pointer;
  color: whitesmoke;
  background: var(--primary-color);
  height: 30px;
  width: 100px;
  border: none;
  border-radius: var(--border-radius);
  margin-top: 20px;
}
button:hover {
  filter: brightness(120%);
}
button:focus {
  outline: none;
}

@media screen and (max-width:800px) {
  .container {
    flex-direction: column;
  }
}

</style>