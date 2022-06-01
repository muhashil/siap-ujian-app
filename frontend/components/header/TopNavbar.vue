<template>
  <b-navbar class="suTopNavbar text-dark" fixed="top" type="pink" variant="light">
    <b-navbar-brand href="#">
      <img src="/images/logo/siap_ujian.png" alt="logo" style="height: 42px;">
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <BIconPersonCircle />
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import {BIconPersonCircle} from 'bootstrap-vue'
export default {
  name: "TopNavbar",
  components: {
    BIconPersonCircle
  }
}
</script>

<style scoped>

</style>
