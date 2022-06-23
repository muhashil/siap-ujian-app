const prefix = 'http://localhost:8000/api/v1'
const path = {
  banner: {
    base: prefix+'/banners'
  },
  matter: {
    base: prefix+'/materi',
    detail: prefix+'/materi/{slug}',
  },
  quiz: {
    base: prefix+'/quizes',
    detail: prefix+'/materi/{slug}',
  },
}
export default path
