<template>
  <section class="vh-50 gradient-custom">
    <div class="container py-5 h-50">
      <div class="row d-flex justify-content-center align-items-center h-50">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">
                  Make your Bid
                </h2>
                <p class="mb-1 card-text-colour2">
                  Current bid: £{{ current }}
                </p>
                <form id="post" class="p-1">
                  <!--
                                    <div class="form-outline form-white mb-4">
                                        <input type="text" id="typeItemX" class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2 " for="typeItemX">Item Name</label>
                                    </div>
                                    Basically the user will click a button to take them to this page
                                    and then it will show the item price and ask for a new price,
                                    this page already knows what item it is.
                                    -->

                  <div class="form-outline form-white mb-4">
                    <label class="form-label card-text-colour2" for="typePriceX">Enter your bid price</label>
                    <input type="number" step="any" id="typePriceX" class="form-control form-control-lg" required />
                  </div>

                  <!--
                                    <div class="form-outline form-white mb-4">
                                        <input type="datetime-local" id="typeDateTimeX"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeDateTimeX">Time of
                                            Bid</label>
                                    </div>
                                    Creation time is added automatically
                                    -->
                </form>

                <button class="btn btn-outline-light btn-lg px-5" @click="send_bid()" type="submit">
                  Bid
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="text-center">
    <h1>Bids</h1>
    <div v-for="bid in bids">
      <p>
        Time: {{ formatDate(bid["time_created"]) }} Price: £{{ bid["price"] }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      id: this.$route.params.id,
      bids: [],
      current: 0,
      item: [],
    };
  },
  components: {},
  methods: {
    async send_bid() {
      await this.get_id();
      let obj: any = document.getElementById("typePriceX");
      let bid: any = obj.value;
      bid = parseInt(bid);
      console.log(bid, this.current);
      if (!(bid)) {
        alert("Please enter a number in the field");
        return;
      }
      if (bid < this.current) {
        alert("Your bid must be higher than the current bid");
        return;
      }
      let vars: any = { bid: bid, user: await this.get_id(), item: this.id };
      let response: any = await fetch("http://127.0.0.1:8000/api/bids/", {
        method: "POST",
        body: JSON.stringify(vars),
        headers: {
          "X-CSRFToken": this.getCookie(),
        },
      });
      this.get_bids();
    },
    async get_bids() {
      let response: any = await fetch("http://127.0.0.1:8000/api/bids/", {
        method: "GET",
      });
      let id: number = +this.id;
      let data: any = await response.json();
      var bids: any = data.bids.filter(function (i: any, n: any) {
        return i.item === id;
      }, id);
      this.bids = bids;
      if (this.bids.length == 0){
        this.current = this.item[0]["starting_price"]
      }
      else{
        this.current = bids.at(-1)["price"];
      }
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
    async get_id() {
      let response: any = await fetch("http://127.0.0.1:8000/api/uid/", {
        method: "GET",
      });
      let data: any = await response.json();
      return data.id;
    },
    async fetch_item() {
      let url: any = "http://127.0.0.1:8000/api/item/" + this.id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      if (!response.ok){
        alert("You cannot bid for this item")
        window.location.replace("http://127.0.0.1:8000/listings")
      }
      let data: any = await response.json();
      this.item = data.item;
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
    this.fetch_item();
    this.get_bids();
  },
});
</script>
