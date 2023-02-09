<template>
  <section class="gradient-custom">
    <div class="container py-5 background-colour">
      <table class="table table-striped table-dark text-white table-hover text-center table-bordered">
        <thead>
          <tr>
            <th colspan="6" class="p-3 card-text-colour">LISTINGS</th>
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
        <tbody>
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
      </table>
    </div>
    <div style="width: 15%; margin: auto" class="input-group">
      <input type="search" class="form-control rounded" placeholder="Search..." id="search_bar" />
      <button type="button" class="btn btn-outline-primary" @click="search_results">
        search
      </button>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      items: [],
    };
  },
  components: {},
  methods: {
    async fetch_items() {
      console.log(document.cookie.split(";"));
      console.log(document.cookie.split(";").length > 1);
      let response: any = await fetch("http://127.0.0.1:8000/api/items/", {
        method: "GET",
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        //headers: {
        //  "Content-Type": "application/json",
        //  "X-CSRFToken": this.getCookie(),
        //},
      });
      let data: any = await response.json();
      this.items = data.items;
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
    async search_results() {
      let obj: any = document.getElementById("search_bar");
      let search_term: any = obj.value;
      let vars: any = { get_type: "search", term: search_term };

      let response: any = await fetch("http://127.0.0.1:8000/api/items/", {
        method: "POST",
        headers: {
          "X-CSRFToken": this.getCookie(),
        },
        body: JSON.stringify(vars),
      });
      let data: any = await response.json();
      this.items = data.items;
    },
    getCookie() {
      let cookieValue: string = "";
      if (document.cookie && document.cookie !== "") {
        var cookies: string[] = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie: any = cookies[i].trim();
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
    this.fetch_items();
  },
});
</script>
