<template>
  <div class="container mt-4">
    <div class="row">
      <div class="col-sm-2 text-center mb-2">
        <img v-if="user[0]?.['profile_picture'] != undefined"
          :src="'http://127.0.0.1:8000/media/' + user[0]?.['profile_picture']" style="width: 5em; height: 5em" />
        <img v-else :src="'http://127.0.0.1:8000/media/default_profile_picture.png'" style="width: 5em; height: 5em" />
      </div>
      <div class="col-sm-8 text-center p-2 rounded" style="background-color: rgb(23, 45, 125, 0.2)">
        <h1>{{ user[0]?.["email"] }}</h1>
        <p class="text-secondary">{{ user[0]?.["city"] }}</p>
        <p class="text-secondary">{{ user[0]?.["dob"] }}</p>
      </div>
      <div class="col-sm-2 text-center">
        <router-link to="/editProfile"><button class="btn btn-primary">Edit profile</button></router-link>
      </div>
    </div>
  </div>
  <section class="gradient-custom">
    <div class="container py-5 background-colour">
      <table class="table table-striped table-dark text-white table-hover text-center table-bordered">
        <thead>
          <tr>
            <th colspan="6" class="p-3 card-text-colour">YOUR LISTINGS</th>
          </tr>
          <tr>
            <th scope="col" class="p-3">Ending time</th>
            <th scope="col" class="p-3">Image</th>
            <th scope="col" class="p-3">Title</th>
            <th scope="col" class="p-3">Description</th>
            <th scope="col" class="p-3">Current bid</th>
            <th scope="col" class="p-3">View</th>
          </tr>
        </thead>
        <tbody v-if="items.length > 0">
          <tr v-for="item in items" style="text-align: center; vertical-align: middle">
            <td>{{ formatDate(item["auction_end_time"]) }}</td>
            <td>
              <img :src="'http://127.0.0.1:8000/media/' + item['image']" style="height: 75px; width: 75px" />
            </td>
            <td>{{ item["title"] }}</td>
            <td>{{ item["description"] }}</td>
            <td>£{{ item["starting_price"] }}</td>
            <td>
              <router-link :to="'/item/' + item['id']"><button class="btn btn-secondary">
                  VIEW LISTING
                </button></router-link>
            </td>
          </tr>
        </tbody>
        <tbody v-else>
          <tr>
            <td class="text-secondary">No items to display</td>
            <td class="text-secondary">No items to display</td>
            <td class="text-secondary">No items to display</td>
            <td class="text-secondary">No items to display</td>
            <td class="text-secondary">No items to display</td>
            <td class="text-secondary">No items to display</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      id: 0,
      user: [],
      items: [],
    };
  },
  components: {},
  methods: {
    async get_id() {
      let response: any = await fetch("http://127.0.0.1:8000/api/uid/", {
        method: "GET",
      });
      let data: any = await response.json();
      this.id = data.id;
      this.fetch_user();
    },
    async fetch_user() {
      let url: any = "http://127.0.0.1:8000/api/user/" + this.id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      let data: any = await response.json();
      this.user = data.user;
    },
    formatDate(date: Date) {
      var hours: number = new Date(date).getHours();
      var minutes: number = new Date(date).getMinutes();
      var ampm: string = hours >= 12 ? "pm" : "am";
      hours = hours % 12;
      hours = hours ? hours : 12;
      var mins: any = minutes < 10 ? (("0" + minutes) as String) : minutes;
      var strTime: string = hours + ":" + mins + " " + ampm;
      return (
        new Date(date).getDate() +
        "/" +
        (new Date(date).getMonth() + 1) +
        "/" +
        new Date(date).getFullYear() +
        "  " +
        strTime
      );
    },
    async fetch_items() {
      let response: any = await fetch("http://127.0.0.1:8000/api/items/", {
        method: "GET",
      });
      let data: any = await response.json();
      console.log(data.items);
      let id: number = +this.id;
      console.log(id);
      this.items = data.items.filter(function (i: any, n: any) {
        return i.user === id;
      }, id);
    },
  },
  mounted() {
    this.get_id();
    this.fetch_items();
  },
});
</script>
