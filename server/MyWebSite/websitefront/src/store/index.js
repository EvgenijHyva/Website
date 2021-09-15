import { createStore } from 'vuex'

export default createStore({
  state: {
    authModalShow: true,
    user: "Anonymous",
    userDarkThemeMode: false 
  },
  mutations: {

  },
  actions: {
  },
  modules: {
  },
  /*getters: {
    authModalShow: (state) => { //same as property that need to return
      return state.authModalShow
    } // => computed property
  }*/
})
