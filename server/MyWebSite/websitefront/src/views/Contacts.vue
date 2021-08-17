<template>
    <section id="contact" v-if="this.contacts !== null && this.contacts.user_is_authorized">
      <h1>Contact</h1>
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
  color: var(--contact-icons);
  text-shadow: 4px 6px 5px var(--contact-shaddow);
}

.fab:hover {
  color: var(--contact-hover);
}

.social-link, .social-link:hover, .social-link:focus {
  text-decoration: none;
  border-bottom: none;
}


</style>