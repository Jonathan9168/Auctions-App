<template>
  <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">
                  Login
                </h2>
                <p class="mb-5 card-text-colour2">
                  Please enter your login and password!
                </p>
                <form id="post" class="p-1">
                  <div class="form-outline form-white mb-4">
                    <input type="email" id="typeEmailX" v-model="email" class="form-control form-control-lg" required />
                    <label class="form-label card-text-colour2" for="typeEmailX">Email</label>
                  </div>

                  <div class="form-outline form-white mb-4">
                    <input type="password" id="typePasswordX" v-model="password" class="form-control form-control-lg"
                      required />
                    <label class="form-label card-text-colour2" for="typePasswordX">Password</label>
                  </div>
                </form>

                <button class="btn btn-outline-light btn-lg px-5" @click="logIn()" type="submit">
                  Login
                </button>
              </div>

              <div>
                <p class="mb-0 card-text-colour2">
                  Don't have an account?
                  <router-link to="/signup"><a href="#" class="card-text-colour2 fw-bold">SignUp</a></router-link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
//import Signup from "./components/Signup.vue";

export default defineComponent({
  data() {
    return {
      email: "",
      password: "",
    };
  },
  components: {},
  methods: {
    async get_csrf() {
      let response: any = await fetch("http://127.0.0.1:8000/login/", {
        method: "GET",
      });
      let data = await response.text();
    },
    async logIn() {
      let e_mail: string = (<HTMLInputElement>document.getElementById("typeEmailX")).value;
      let p_word: string = (<HTMLInputElement>document.getElementById("typePasswordX")).value;
      const validateEmail = (email:string) => {
        return String(email)
          .toLowerCase()
          .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          );
      };
      if (!validateEmail(e_mail)) {
        alert("Please enter a valid email");
        return;
      }
      if (e_mail == "" && p_word == "") {
        alert("Please enter you email and your password");
        return;
      }
      if (e_mail == "") {
        alert("Please enter you email");
      }
      if (p_word == "") {
        alert("Please enter your password");
      }
      let vars: any = { type: "login", email: this.email, password: this.password };
      let response: any = await fetch("http://127.0.0.1:8000/api/users/", {
        method: "POST",
        body: JSON.stringify(vars),
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.getCookie(),
        },
      });
      let data: any = await response.text();
      if (response.ok && data == "logged in") {

        window.location.replace("http://127.0.0.1:8000/profile/");
      }
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
  mounted() {
    this.get_csrf();
  },
});
</script>
