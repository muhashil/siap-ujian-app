import Vuex from 'vuex'
import matter from "./modules/matter";

new Vuex.Store({
  state: () => ({
    is_loading: false,
  }),
  mutations: {
    SET_IS_LOADING(state, payload) {
      state.is_loading = payload
    },
  },
  getters: {
    GET_IS_LOADING(state) {
      return state.is_loading
    }
  },
  modules: {
    matter
  }
})
