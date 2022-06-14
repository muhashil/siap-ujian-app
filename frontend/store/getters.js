export default {
  getLoading(state) {
    return state.is_loading
  },
  getMatter(state) {
    return state.matters
  },
  getDetailMatter(state) {
    return state.matter
  },
  getBanner(state) {
    return state.banners
  },
}
