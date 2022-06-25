<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Detail Kuis" backUrl="/quiz")
    div(style="margin-top: 70px;")
    .d-flex.mt-3.pb-3(style="overflow-x: auto;")
      b-button.mx-1(size="sm" :variant="isButtonActive(q) ? 'info' : 'outline-info'" v-for="(q, i) in question"
        @click="$router.push({path: `/quiz/${quiz_slug}/question/${q.slug}`})") {{i+1}}
    .row
      .col-12.mb-4
        b-card
          b-card-text {{recent_question.question}}
          b-form-group(v-slot="{ ariaDescribedby }")
            b-form-radio.mb-2(
              v-model="answer_selected"
              :aria-describedby="ariaDescribedby"
              name="answer"
              v-for="(a) in recent_question.answers"
              :value="a"
            ) {{a.answer}}
          b-button-toolbar.mb-4(key-nav)
            b-button-group.mx-1
              b-button(size="sm" @click="gotoPrevious") &laquo;
            b-button-group.mx-1
              b-button.mx-1(size="sm" variant="info" @click="showSolution") Pembahasan
            b-button-group.mx-1
              b-button(size="sm" @click="gotoNext") &raquo;
          b-card(v-if="is_show_solution" )
            b-card-text {{recent_question.description}}
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
      question_slug: this.$route.params.question,
      recent_question: {},
      answer_selected: null,
      is_show_solution: false
    }
  },
  mounted() {
    if (!this.question.length) this.fetchAllQuestion().then(() => this.recentQuestion())
    else this.recentQuestion();
  },
  methods: {
    async fetchAllQuestion() {
      return await this.$store.dispatch('fetchQuestion', this.quiz_slug)
    },
    recentQuestion() {
      this.recent_question = this.question.find((q) => {
        return q.slug === this.question_slug
      })
    },
    showSolution() {
      if (this.answer_selected) {
        this.is_show_solution = !this.is_show_solution
      } else
        this.$bvModal.show('modalNotAnswered')
    },
    isButtonActive(item) {
      return item.slug === this.question_slug
    },
    activeIndex() {
      return this.question.findIndex((q) => {
        return q.slug === this.question_slug
      })
    },
    gotoNext() {
      if (this.activeIndex() < this.question.length-1)
        this.$router.push({path: `/quiz/${this.quiz_slug}/question/${this.question[this.activeIndex()+1].slug}`})
    },
    gotoPrevious() {
      if (this.activeIndex() > 0)
        this.$router.push({path: `/quiz/${this.quiz_slug}/question/${this.question[this.activeIndex()-1].slug}`})
    }
  },
  computed: {
    question() {
      return this.$store.getters.getQuestion
    },
    isLoading() {
      return this.$store.getters.getLoading
    }
  }
}
</script>

<style scoped>

</style>
