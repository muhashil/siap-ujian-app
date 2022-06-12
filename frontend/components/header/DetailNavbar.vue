<template>
  <b-navbar class="suTopNavbar text-dark" fixed="top" type="pink" variant="light">
    <b-navbar-brand href="javascript:void(0)" class="text-dark">
      <BIconArrowLeft @click="$router.go(-1)" />
      Materi CPNS
    </b-navbar-brand>
  </b-navbar>
</template>

<script>
import {BIconArrowLeft} from 'bootstrap-vue'
export default {
  name: "DetailNavbar",
  components: {
    BIconArrowLeft
  }
}
</script>

<style scoped>

</style>
