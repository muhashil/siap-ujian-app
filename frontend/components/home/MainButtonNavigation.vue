<template lang="pug">
  div.card.suMainButtonNavigation
    div.card-body.bodyButton
      slot
      div.ml-1 {{label}}
</template>

<script>
export default {
  name: "MainButtonNavigation",
  props: {
    label: String
  }
}
</script>

<style scoped>

</style>
