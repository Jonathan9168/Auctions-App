<template>
  <div class="container mt-4">
    <div class="row">
      <div class="col-sm-2 text-center mb-2">
        <img v-if="dp != ''" :src="'http://127.0.0.1:8000/media/' + dp" style="width: 5em; height: 5em;" />
        <img v-else :src="'http://127.0.0.1:8000/media/default_profile_picture.png'" style="width: 5em; height: 5em;" />

      </div>
      <div class="col-sm-8 text-center p-2 rounded" style="background-color:rgb(23,45,125,0.2)">
        <form id="put">
          <h1>Email: {{ email }}</h1>
          <input class="input-group mx-auto text-center" name="email" id="e_mail" style="width:60%" v-model="email"
            placeholder="Enter email" />
          <p class="text-secondary mt-3 mb-1">City: {{ city }}</p>
          <input class="input-group mx-auto text-center" name="city" id="city" style="width:60%" v-model="city"
            placeholder="Enter city" />
          <p class="text-secondary mt-3 mb-1">Date of birth: {{ dob }}</p>
          <input class="input-group mx-auto text-center" name="dob" id="dob" style="width:60%" v-model="dob"
            placeholder="Enter dob" />
          <p class="text-secondary mt-3 mb-1">Upload profile picture</p>
          <input type="file" name="image" class="form-control" accept="image/*" v-on:change="changeImage()"
            id="image" />
        </form>
      </div>
      <div class="col-sm-2 text-center">
        <router-link to="/profile"><button class="btn btn-primary">View profile</button></router-link>
      </div>
    </div>
    <div class="text-center">
      <button class="btn btn-primary mt-3" @click="update_user">Update</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      id: 0,
      name: "",
      city: "",
      dob: "",
      email: "",
      dp: "",
      image: undefined,
    }
  },
  components: {},
  methods: {
    async update_user() {
      let form = document.getElementById("put") as HTMLFormElement;
      let e_mail: string = (<HTMLInputElement>document.getElementById("e_mail")).value;
      let city: string = (<HTMLInputElement>document.getElementById("city")).value;
      let dob: any = (<HTMLInputElement>document.getElementById("dob")).value;
      let image: any = (<HTMLInputElement>document.getElementById("image")).value;
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
      if (e_mail == "" && city == "" && !(dob) && !(image)) {
        alert("Please enter details");
        return;
      }
      if (e_mail == "") {
        alert("Please enter an email");
        return;
      }
      if (city == "") {
        alert("Please enter a city");
        return;
      }

      if (!(dob)) {
        alert("Please enter a date of birth");
        return;
      }
      if (!(image)) {
        alert("Please upload an image");
        return;
      }
      let url = "http://127.0.0.1:8000/api/users/"
      if (form) {
        const data: any = new FormData(form);
        data.append("id", this.id.toString());
        if (this.image) {
          data.append("profile_picture", this.image);
          console.log(1)
        }
        let response: any = await fetch(url, {
          method: "PUT",
          body: data,
          headers: {
            "X-CSRFToken": this.getCookie(),
          },
        });
        window.location.replace("http://127.0.0.1:8000/profile")
      }
    },
    async get_id() {
      let response: any = await fetch("http://127.0.0.1:8000/api/uid/", {
        method: "GET",
      });
      let data = await response.json();
      this.id = data.id;
      this.fetch_user()
    },
    async fetch_user() {
      let url: any = "http://127.0.0.1:8000/api/user/" + this.id + "/"
      let response: any = await fetch(url, {
        method: "GET",
      })
      let data: any = await response.json()
      console.log(data.user[0])
      this.city = data.user[0].city
      this.dob = data.user[0].dob
      this.email = data.user[0].email
      this.dp = data.user[0].profile_picture
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
    changeImage() {
      let pic: any = document.getElementById("image");
      this.image = pic;
    },
  },
  mounted() {
    this.get_id();
  }
},
);
</script>