<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar(title="Materi CPNS" back-url="/" )
    div(style="margin-top: 55px;")
    TabListMatter(:data="matters" :button="{text: 'Pelajari', url: '/materi/{slug}'}")
    Loading(
      :active="isLoading"
      :is-full-page="true"
      loader="bars"
      background-color="#4B4B4B"
      color="#008FD7")
</template>

<script>
import Loading from "vue-loading-overlay";
import DetailNavbar from "../../components/header/DetailNavbar"
import TabListMatter from "../../components/matters/TabListMatter"
export default {
  name: "SubjectMatterPage",
  components: {TabListMatter, DetailNavbar, Loading},
  data() {
    return {
    }
  },
  mounted() {
    this.fetchMatter()
  },
  methods: {
    async fetchMatter() {
      await this.$store.dispatch('fetchMatter');
    }
  },
  computed: {
    matters() {
      return this.$store.getters.getMatter
    },
    isLoading() {
      return this.$store.getters.getLoading
    }
  },
}
</script>

<style scoped>

</style>
