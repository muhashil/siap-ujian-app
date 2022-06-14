<template lang="pug">
  b-tabs(fill card v-model="tabIndex")
    b-tab(title="TWK")
      b-card-text TWK adalah tes yang di selenggarakan cpns mengenai wawasan kebangsaan dan pancasila
      .row
        .col-12.mb-4(v-for="(item, key) in data" )
          b-card(:header="`Materi ${key+1}`")
            h5.mb-3 {{item.title}}
            b-button.suButtonPrimary(:href="`/materi/${item.slug}`" variant="info" ) Pelajari
    b-tab(title="TIU")
      b-card-text TIU adalah tes yang di selenggarakan cpns mengenai wawasan kebangsaan dan pancasila
      .row
        .col-12.mb-4
          b-card(header="Materi 1" title="Pancasila Dasar Negara")
            b-button.suButtonPrimary(href="#" variant="info" ) Pelajari
        .col-12.mb-4
          b-card(header="Materi 1" title="Pancasila Dasar Negara")
            b-button.suButtonPrimary(href="#" variant="info" ) Pelajari
    b-tab(title="TKP")
      b-card-text TKP adalah tes kepribadian yang di selenggarakan cpns mengenai wawasan kebangsaan dan pancasila
      .row
        .col-12.mb-4
          b-card(header="Materi 1" title="Pancasila Dasar Negara")
            b-button.suButtonPrimary(href="#" variant="info" ) Pelajari
        .col-12.mb-4
          b-card(header="Materi 1" title="Pancasila Dasar Negara")
            b-button.suButtonPrimary(href="#" variant="info" ) Pelajari
</template>

<script>
export default {
  name: "TabListMatter",
  props: {
    data: {
      type: Array,
      default: function () {
        return []
      }
    }
  },
  data() {
    return {
      tabIndex: 0
    }
  }
}
</script>

<style scoped>

</style>
