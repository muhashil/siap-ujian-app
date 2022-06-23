<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Detail Kuis")
    div(style="margin-top: 70px;")
    .d-flex.mt-3.pb-3(style="overflow-x: auto;")
      b-button.mx-1(size="sm" variant="outline-info") 1
      b-button.mx-1(size="sm" variant="outline-info") 2
      b-button.mx-1(size="sm" variant="outline-info") 3
      b-button.mx-1(size="sm" variant="outline-info") 4
      b-button.mx-1(size="sm" variant="outline-info") 5
      b-button.mx-1(size="sm" variant="outline-info") 6
      b-button.mx-1(size="sm" variant="outline-info") 7
      b-button.mx-1(size="sm" variant="outline-info") 8
      b-button.mx-1(size="sm" variant="outline-info") 9
      b-button.mx-1(size="sm" variant="outline-info") 10
      b-button.mx-1(size="sm" variant="outline-info") 11
      b-button.mx-1(size="sm" variant="outline-info") 1
      b-button.mx-1(size="sm" variant="outline-info") 2
      b-button.mx-1(size="sm" variant="outline-info") 3
      b-button.mx-1(size="sm" variant="outline-info") 4
      b-button.mx-1(size="sm" variant="outline-info") 5
      b-button.mx-1(size="sm" variant="outline-info") 6
      b-button.mx-1(size="sm" variant="outline-info") 7
      b-button.mx-1(size="sm" variant="outline-info") 8
      b-button.mx-1(size="sm" variant="outline-info") 9
      b-button.mx-1(size="sm" variant="outline-info") 10
      b-button.mx-1(size="sm" variant="outline-info") 11
    .row
      .col-12.mb-4
        b-card
          b-card-text {{detailQuestion.question}}
          b-form-group(v-slot="{ ariaDescribedby }")
            b-form-radio.mb-2(
              v-model="answer_selected"
              :aria-describedby="ariaDescribedby"
              name="answer"
              v-for="(a) in detailQuestion.answers"
              :value="a"
            ) {{a.answer}}
          b-button-toolbar.mb-4(key-nav)
            b-button-group.mx-1
              b-button(size="sm" ) &laquo;
            b-button-group.mx-1
              b-button.mx-1(size="sm" variant="info" @click="showSolution") Pembahasan
            b-button-group.mx-1
              b-button(size="sm" ) &raquo;
          b-card(v-if="is_show_solution" )
            b-card-text {{detailQuestion.description}}
    b-modal(id="modalNotAnswered" centered hide-header hide-footer)
      .p-3
        p.text-center Ops, untuk melihat pembahasan anda harus menjawab dulu
        .text-center
          b-button(size="sm" variant="info" @click="$bvModal.hide('modalNotAnswered')") Oke
    Loading(
      :active="isLoading"
      :is-full-page="true"
      loader="bars"
      background-color="#4B4B4B"
      color="#008FD7")
</template>

<script>
import Loading from "vue-loading-overlay";
import DetailNavbar from "../../../../components/header/DetailNavbar";
export default {
  name: "_question",
  components: {DetailNavbar, Loading},
  data: function () {
    return {
      quiz_slug: this.$route.params.quiz,
      answer_selected: null,
      is_show_solution: false
    }
  },
  mounted() {
    this.fetchDetailQuestion()
  },
  methods: {
    async fetchDetailQuestion() {
      let res = await this.$store.dispatch('fetchQuestionDetail', this.$route.params.question)
      if (!res) return this.$router.push({name: 'QuizPage'})
    },
    showSolution() {
      if (this.answer_selected) {
        this.is_show_solution = !this.is_show_solution
      } else
        this.$bvModal.show('modalNotAnswered')
    }
  },
  computed: {
    question() {
      return this.$store.getters.getQuestion
    },
    detailQuestion() {
      return this.$store.getters.getDetailQuestion
    },
    isLoading() {
      return this.$store.getters.getLoading
    }
  }
}
</script>

<style scoped>

</style>
