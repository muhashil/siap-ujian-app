import path from "../../utils/path";

const state = {
  matters: []
}

const mutations = {
  SET_MATTERS(state, payload) {
    state.matters = payload
  }
}

const actions = {
  async fetchMatters({ commit, dispatch, state }, payload) {
    try {
      commit('SET_IS_LOADING', true)
      return await this.$axios.post(path.matters.base, {oauth_token: payload})
    } catch(error) {
      commit('SET_IS_LOADING', false)
    } finally {
      commit('SET_IS_LOADING', false)
    }
  }
}

const getters = {
  GET_MATTERS(state) {
    return state.matters
  }
}
export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
