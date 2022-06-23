export default {
  setLoading(state, payload) {
    state.is_loading = payload
  },
  setBanner(state, payload) {
    state.banners = payload
  },

  //Materi
  setMatter(state, payload) {
    state.matter.list = payload
  },
  setDetailMatter(state, payload) {
    state.matter.detail = payload
  },

  //Quiz
  setQuiz(state, payload) {
    state.quiz.list = payload
  },
  setDetailQuiz(state, payload) {
    state.quiz.detail = payload
  },
}
