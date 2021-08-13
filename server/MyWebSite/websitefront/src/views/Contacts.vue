<template>
    <section id="contact" v-if="this.contacts !== null && this.contacts.user_is_authorized">
        <div class="social-icons">
            <a :href="this.contacts.github" target="blank" class="social-link"><i class="fab fa-github-square"></i></a>
            <a :href="this.contacts.vk" target="blank" class="social-link"><i class="fab fa-vk"></i></a>
            <a :href="this.contacts.facebook" target="blank" class="social-link"><i class="fab fa-facebook"></i></a>
            <a :href="this.contacts.instagram" target="blank" class="social-link"><i class="fab fa-instagram"></i></a>
            <a :href="this.contacts.telegram_username" target="blank" class="social-link"><i class="fab fa-telegram-plane"></i></a>
            <a :href="this.contacts.whatsapp" target="blank" class="social-link"><i class="fab fa-whatsapp"></i></a>
        </div>
    </section>
</template>

<script>
import { apiService } from "../common/api.service"
const contactsEndpoint = "/api/contacts/"
export default {
    name: "Contacts",
    methods: {
      getContacts() {
        apiService(contactsEndpoint)
          .then(contacts => this.contacts = contacts )
          .catch(err => console.log(err))
      }
    },
    data() {
      return {
        contacts: null,
      }
    },
    created: function() {
      this.getContacts()    
    }
}
</script>

<style>

/* Contact Section */
.fab {
  font-size: 100px;
  margin-right: 50px;
  cursor: pointer;
  color: var(--primary-color);
}

.fab:hover {
  color: var(--on-background);
}


.slider {
  background: #ccc;
  bottom: 0;
  cursor: pointer;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  transition: 0.4s;
}

.slider::before {
  background: #fff;
  bottom: 4px;
  content: "";
  height: 26px;
  left: 4px;
  position: absolute;
  transition: 0.4s;
  width: 26px;
}

input:checked + .slider {
  background: var(--primary-color);
}

input:checked + .slider::before {
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round::before {
  border-radius: 50%;
}
.social-link, .social-link:hover, .social-link:focus {
  text-decoration: none;
  border-bottom: none;
}


</style>