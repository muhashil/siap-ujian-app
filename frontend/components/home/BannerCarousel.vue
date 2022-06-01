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
    <b-carousel-slide>
      <template #img>
        <img
          class="d-block img-fluid w-100"
          height="380"
          src="https://picsum.photos/1024/380/?image=52"
          alt="image slot"
          style="border-radius: 20px;"
        >
      </template>
    </b-carousel-slide>
    <b-carousel-slide>
      <template #img>
        <img
          class="d-block img-fluid w-100"
          height="380"
          src="https://picsum.photos/1024/380/?image=54"
          alt="image slot"
          style="border-radius: 20px;"
        >
      </template>
    </b-carousel-slide>
    <b-carousel-slide>
      <template #img>
        <img
          class="d-block img-fluid w-100"
          height="380"
          src="https://picsum.photos/1024/380/?image=55"
          alt="image slot"
          style="border-radius: 20px;"
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
  methods: {
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  }
}
</script>

<style scoped>

</style>
