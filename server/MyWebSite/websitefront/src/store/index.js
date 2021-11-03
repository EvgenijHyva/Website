import { createStore } from 'vuex'

export default createStore({
  state: {
    authModalShow: true,
    user: "Anonymous",
    is_staff: false,
    userDarkThemeMode: false,
    showAuth: false, // this property allow to hide and show Auth component.
    key: null,
    activeProject: "Mainpage",
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
