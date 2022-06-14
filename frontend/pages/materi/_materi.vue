<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Detail Materi")
    div(style="margin-top: 70px;")
    .row
      .col-12.mb-4
        b-card(:header="matter.title")
          b-card-text {{matter.content}}
</template>

<script>
import DetailNavbar from "../../components/header/DetailNavbar";
export default {
  name: "_materi",
  components: {DetailNavbar},
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
      if (!res) return this.$router.push({name: 'SubjectMatter'})
    }
  },
  computed: {
    matter() {
      return this.$store.getters.getDetailMatter
    }
  }
}
</script>

<style scoped>

</style>
