const prefix = 'http://localhost:8000/api/v1'
const path = {
  matter: {
    base: prefix+'/materi',
    detail: prefix+'/materi/{slug}',
  },
  banner: {
    base: prefix+'/banners'
  }
}
export default path
