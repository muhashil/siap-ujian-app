export default {
  getLoading(state) {
    return state.is_loading
  },
  getBanner(state) {
    return state.banners
  },

  //Materi
  getMatter(state) {
    return state.matter.list
  },
  getDetailMatter(state) {
    return state.matter.detail
  },

  //Quiz
  getQuiz(state) {
    return state.quiz.list
  },
  getDetailQuiz(state) {
    return state.quiz.detail
  },
}
