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
    detail: prefix+'/quizes/{slug}',
  },
  question: {
    base: prefix+'/quizes/{slug}/questions',
    detail: prefix+'/questions/{slug}',
  },
}
export default path
