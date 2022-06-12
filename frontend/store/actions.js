import path from "../utils/path";

export default {
  async fetchMatters({ commit }) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.matters.base)
      commit('setMatter', res)
    } catch(error) {
      commit('setLoading', false)
    } finally {
      commit('setLoading', false)
    }
  }
}
