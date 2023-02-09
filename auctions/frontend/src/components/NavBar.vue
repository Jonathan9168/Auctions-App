<template>
  <nav class="navbar navbar-expand-lg navbar-light dark-green">
    <div class="container-fluid">
      <router-link v-if="check_logged() == true" to="/listings"><a class="navbar-brand"
          href="#">QuickAucs</a></router-link>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0"></ul>
        <ul class="navbar-nav">
          <li v-if="check_logged()" class="nav-item">
            <router-link to="/listItem"><a class="nav-link" href="#">List Item</a></router-link>
          </li>
          <li v-if="check_logged()" class="nav-item">
            <router-link to="/profile"><a class="nav-link" href="#">Profile</a></router-link>
          </li>
          <li v-if="check_logged()" @click="logout" class="nav-item">
            <a class="nav-link" style="text-decoration: underline !important"
              href="#">Logout</a>
          </li>
          <li v-if="check_logged() == false" class="nav-item">
            <router-link to="/"><a class="nav-link" href="#">Login</a></router-link>
          </li>
          <li v-if="check_logged() == false" class="nav-item">
            <router-link to="/signup"><a class="nav-link" href="#">Sign Up</a></router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {};
  },
  components: {},
  methods: {
    async logout() {
      let response = await fetch("http://127.0.0.1:8000/logout/", {
        method: "POST",
        headers: {
          "X-CSRFToken": this.getCookie(),
        },
      });
      window.location.replace("http://127.0.0.1:8000/");
    },
    check_logged() {
      if (document.cookie.split(";").length > 1) {
        return true;
      }
      return false;
    },
    getCookie() {
      let cookieValue: string = "";
      if (document.cookie && document.cookie !== "") {
        var cookies: string[] = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie: string = cookies[i].trim();
          if (cookie.substring(0, 10) === "csrftoken=") {
            cookieValue = decodeURIComponent(cookie.substring(10));
            break;
          }
        }
      }
      return cookieValue;
    },
  },
});
</script>
