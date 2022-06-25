<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Detail Materi" back-url="/materi" )
    div(style="margin-top: 70px;")
    .row
      .col-12.mb-4
        b-card(:header="matter.title")
          b-card-text {{matter.content}}
    Loading(
      :active="isLoading"
      :is-full-page="true"
      loader="bars"
      background-color="#4B4B4B"
      color="#008FD7")
</template>

<script>
import Loading from "vue-loading-overlay";
import DetailNavbar from "../../components/header/DetailNavbar";
export default {
  name: "_materi",
  components: {DetailNavbar, Loading},
  data() {
    return {
    }
  },
  mounted() {
    this.fetchDetailMatter()
  },
  methods: {
    async fetchDetailMatter() {
      let res = await this.$store.dispatch('fetchMatterDetail', this.$route.params.materi)
      if (!res) return this.$router.push({name: 'SubjectMatterPage'})
    }
  },
  computed: {
    matters() {
      return this.$store.getters.getMatter
    },
    matter() {
      return this.$store.getters.getDetailMatter
    },
    isLoading() {
      return this.$store.getters.getLoading
    }
  }
}
</script>

<style scoped>

</style>
