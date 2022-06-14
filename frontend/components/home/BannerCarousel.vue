<template>
  <b-carousel
    id="carousel-1"
    v-model="slide"
    :interval="4000"
    controls
    background="#FFFFFF"
    style="text-shadow: 1px 1px 2px #333;"
    @sliding-start="onSlideStart"
    @sliding-end="onSlideEnd"
  >
    <b-carousel-slide v-for="(item, index) in banners">
      <template #img>
        <img
          class="d-block img-fluid w-100"
          height="380"
          :src="item.image"
          :alt="item.title"
          style="border-radius: 15px;"
        >
      </template>
    </b-carousel-slide>
  </b-carousel>
</template>

<script>
export default {
  name: "BannerCarousel",
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  mounted() {
    this.fetchBanner()
  },
  methods: {
    async fetchBanner() {
      await this.$store.dispatch('fetchBanner');
    },
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  },
  computed:{
    banners(){
      return this.$store.getters.getBanner
    }
  }
}
</script>

<style scoped>

</style>
