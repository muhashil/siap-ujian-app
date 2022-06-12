<template lang="pug">
  b-container(fluid style="max-width: 500px; padding: 0;")
    DetailNavbar
    div(style="margin-top: 55px;")
    TabListMatter
</template>

<script>
import DetailNavbar from "../../components/header/DetailNavbar";
import TabListMatter from "../../components/matters/TabListMatter";
export default {
  name: "SubjectMatter",
  components: {TabListMatter, DetailNavbar},
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style scoped>

</style>
