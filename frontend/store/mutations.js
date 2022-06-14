export default {
  setLoading(state, payload) {
    state.is_loading = payload
  },
  setMatter(state, payload) {
    state.matters = payload
  },
  setDetailMatter(state, payload) {
    state.matter = payload
  },
  setBanner(state, payload) {
    state.banners = payload
  }
}
