import path from "../utils/path";

export default {
  async fetchBanner({ commit }) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.banner.base)
      if (res.data.action) {
        commit('setBanner', res.data.result)
        commit('setLoading', false)
      }
    } catch(error) {
      commit('setLoading', false)
    } finally {
      commit('setLoading', false)
    }
  },
  async fetchMatter({ commit }) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.matter.base)
      if (res.data.action) {
        commit('setMatter', res.data.result)
        commit('setLoading', false)
      }
    } catch(error) {
      commit('setLoading', false)
    } finally {
      commit('setLoading', false)
    }
  },
  async fetchMatterDetail({ commit }, slug) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.matter.detail.replace('{slug}', slug))
      if (res.data.action) {
        commit('setDetailMatter', res.data.result)
        commit('setLoading', false)
        return res.data.result
      }
      return null
    } catch(error) {
      commit('setLoading', false)
      return error
    } finally {
      commit('setLoading', false)
    }
  },
  async fetchQuiz({ commit }) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.quiz.base)
      if (res.data.action) {
        commit('setQuiz', res.data.result)
        commit('setLoading', false)
      }
    } catch(error) {
      commit('setLoading', false)
    } finally {
      commit('setLoading', false)
    }
  },
  async fetchQuizDetail({ commit }, slug) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.quiz.detail.replace('{slug}', slug))
      if (res.data.action) {
        commit('setDetailQuiz', res.data.result)
        commit('setLoading', false)
        return res.data.result
      }
      return null
    } catch(error) {
      commit('setLoading', false)
      return error
    } finally {
      commit('setLoading', false)
    }
  },
  async fetchQuestionDetail({ commit }, slug) {
    try {
      commit('setLoading', true)
      let res = await this.$axios.get(path.question.detail.replace('{slug}', slug))
      if (res.data.action) {
        commit('setDetailQuestion', res.data.result)
        commit('setLoading', false)
        return res.data.result
      }
      return null
    } catch(error) {
      commit('setLoading', false)
      return error
    } finally {
      commit('setLoading', false)
    }
  }
}
