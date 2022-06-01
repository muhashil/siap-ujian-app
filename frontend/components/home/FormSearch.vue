<template lang="pug">
  div
    b-input-group
      b-form-input(type="text" placeholder="Cari Materi...")
      b-input-group-append
        b-input-group-text.bg-white
          BIconSearch
</template>

<script>
import {BIconSearch} from 'bootstrap-vue'
export default {
  name: "FormSearch",
  components: {BIconSearch}
}
</script>

<style scoped>

</style>
