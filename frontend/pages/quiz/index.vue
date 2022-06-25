<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Kuis CPNS" back-url="/" )
    div(style="margin-top: 70px;")
    .row
      .col-12.mb-4(v-for="(item, key) in quiz" )
        b-card(:header="`Kuis ${key+1}`")
          h5.mb-3 {{item.title}}
          b-button.suButtonPrimary(:href="`/quiz/${item.slug}/question`" variant="info" ) Kerjakan
    Loading(
      :active="isLoading"
      :is-full-page="true"
      loader="bars"
      background-color="#4B4B4B"
      color="#008FD7")
</template>

<script>
import DetailNavbar from "../../components/header/DetailNavbar";
import TabListMatter from "../../components/matters/TabListMatter";
import Loading from "vue-loading-overlay";
export default {
  name: "QuizPage",
  components: {TabListMatter, DetailNavbar, Loading},
  data() {
    return {

    }
  },
  mounted() {
    this.fetchQuiz()
  },
  methods: {
    async fetchQuiz() {
      await this.$store.dispatch('fetchQuiz');
    }
  },
  computed: {
    quiz() {
      return this.$store.getters.getQuiz
    },
    isLoading() {
      return this.$store.getters.getLoading
    }
  }
}
</script>

<style scoped>

</style>
