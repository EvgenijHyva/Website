import { createStore } from 'vuex'

export default createStore({
  state: {
    authModalShow: true,
    user: "Anonym",
    userDarkThemeMode: localStorage.getItem("Dark") || false,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
