<template lang="pug">
  div.container(style="max-width: 500px;")
    TopNavbar
    FormSearch(style="margin-top: 100px;")
    div.mt-4
      h6
        b Pengumuman
      BannerCarousel
    div.mt-4
      h6
        b CPNS
      div.d-flex.justify-content-between
        div(@click="$router.push({path: '/materi'})")
          MainButtonNavigation(label="MATERI")
            BIconBook.suFont22
        div(@click="$router.push({path: '/quiz'})")
          MainButtonNavigation(label="LATIHAN" )
            BIconPencilSquare.suFont22
        MainButtonNavigation(label="UJIAN" )
          BIconPatchCheck.suFont22MATERI
    div.mt-4
      h6
        b SBMPTN
      div.d-flex.justify-content-between
        div(@click="$router.push({path: '/materi'})")
          MainButtonNavigation(label="MATERI" )
            BIconBook.suFont22
        MainButtonNavigation(label="LATIHAN" )
          BIconPencilSquare.suFont22
        MainButtonNavigation(label="UJIAN" )
          BIconPatchCheck.suFont22
    div.mt-4
      h6
        b NEWS
      NewsList

    //Tutorial
</template>

<script>
import TopNavbar from "../components/header/TopNavbar";
import {BIconSearch, BIconBook, BIconPencilSquare, BIconPatchCheck} from 'bootstrap-vue'
import FormSearch from "../components/home/FormSearch";
import BannerCarousel from "../components/home/BannerCarousel";
import MainButtonNavigation from "../components/home/MainButtonNavigation";
import NewsList from "../components/home/NewsList";
export default {
  name: 'IndexPage',
  components: {
    NewsList, BannerCarousel, FormSearch, TopNavbar, BIconSearch, BIconBook, BIconPencilSquare, BIconPatchCheck,
    MainButtonNavigation
  },
  methods: {

  }
}
</script>
