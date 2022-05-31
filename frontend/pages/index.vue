<template lang="pug">
  div.container(style="max-width: 500px;")
    TopNavbar
    FormSearch(style="margin-top: 100px;")
    div.mt-4
      h6
        b Pengumuman
      BannerCarousel
    //Tutorial
</template>

<script>
import TopNavbar from "../components/header/TopNavbar";
import {BIconSearch} from 'bootstrap-vue'
import FormSearch from "../components/home/FormSearch";
import BannerCarousel from "../components/home/BannerCarousel";
export default {
  name: 'IndexPage',
  components: {BannerCarousel, FormSearch, TopNavbar, BIconSearch}
}
</script>
