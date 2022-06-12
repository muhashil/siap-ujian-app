<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar
    div(style="margin-top: 55px;")
    TabListMatter
</template>

<script>
import DetailNavbar from "../../components/header/DetailNavbar"
import TabListMatter from "../../components/matters/TabListMatter"
export default {
  name: "SubjectMatter",
  components: {TabListMatter, DetailNavbar},
  data() {
    return {

    }
  },
  mounted() {
    this.fetchMatters()
  },
  methods: {
    async fetchMatters() {
      await this.$store.dispatch('fetchMatters');
    }
  },
  computed: {
    matters() {
      return this.$store.state.matters
    }
  },
}
</script>

<style scoped>

</style>
