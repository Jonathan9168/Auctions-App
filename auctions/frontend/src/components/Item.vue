<template>
  <div class="container mt-4">
    <div class="row">
      <div class="col-sm-2 text-center mb-2">
        <img v-if="item[0]?.['image'] != undefined" :src="'http://127.0.0.1:8000/media/' + item[0]?.['image']"
          style="width: 5em; height: 5em" />
        <img v-else :src="'http://127.0.0.1:8000/media/default_item.png'" style="width: 5em; height: 5em" />
      </div>
      <div class="col-sm-8 text-center p-2 rounded" style="background-color: rgb(23, 45, 125, 0.2)">
        <h1>{{ item[0]?.["title"] }}</h1>
        <p class="text-light">{{ item[0]?.["description"] }}</p>
        <p>
          <router-link :to="'/user/' + item[0]?.['user']"><a href="#" class="link-secondary">Item owner: {{ user
          }}</a></router-link>
        </p>
        <p class="text-secondary">£{{ item[0]?.["starting_price"] }}</p>
        <p class="text-secondary">
          Listing date: {{ formatDate(item[0]?.["listing_time"]) }}
        </p>
        <p class="text-secondary">
          Auction end: {{ formatDate(item[0]?.["auction_end_time"]) }}
        </p>
        <p class="text-secondary">
          Time left until auction end: {{ x }}
        </p>
        <router-link :to="'/question/' + id"><button class="btn btn-secondary">
            Ask A Question
          </button></router-link>
        <router-link :to="'/bid/' + id"><button class="btn btn-secondary m-2">
            Make A Bid
          </button></router-link>
      </div>
    </div>
    <div>
      <h2 class="text-center">Questions</h2>
      <div v-for="question in questions" class="p-2 text-center">
        <p class="m-1 text-primary">
          {{ formatDate(question["time_created"]) }} Question:
          {{ question["question"] }}
        </p>
        <router-link :to="'/user/' + find_match(question)?.['user_id']"><a href="#" class="link-secondary">By user: {{
            find_match(question)?.['email']
        }}</a></router-link>
        <p class="text-success" v-if="question['answer'] != null">
          {{ formatDate(question["answer"]["answered"]) }} Answer:
          {{ question["answer"]["answer_text"] }}
        </p>
        <p class="text-success" v-else>Not answered yet</p>
        <router-link v-if="item[0]?.['user'] == user_id && question['answer'] == null"
          :to="'/Answer/' + question['id']"><button class="btn btn-secondary">Answer</button></router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      id: this.$route.params.id,
      item: [],
      user: "",
      users: [],
      questions: [],
      user_id: 0,
      x: "Loading...",
    };
  },
  components: {},
  methods: {
    find_match(question: any) {
      let id: any = question["user"];
      for (let j = 0; j <= this.users.length; j++) {
        let uid: any = this.users[j];
        if (uid != undefined) {
          if (id == uid.user_id) {
            return uid;
          }
        }
      }
    },
    timeLeft(date: Date) {
      var now: Date = new Date();
      var timeLeft: any = new Date(date).getTime() - now.getTime();
      var days: number = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
      var hours: number = Math.floor(
        (timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      var minutes: number = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
      var seconds: number = Math.floor((timeLeft % (1000 * 60)) / 1000);
      this.x = (
        days +
        "d " +
        hours +
        "h " +
        minutes +
        "m " +
        seconds +
        "s " +
        "until auction end"
      );
    },
    async fetch_item() {
      let url: any = "http://127.0.0.1:8000/api/item/" + this.id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      if (!response.ok){
        alert("This item does not exist")
        window.location.replace("http://127.0.0.1:8000/listings")
      }
      let data: any = await response.json();
      this.item = data.item;
      this.fetch_user(data.item[0].user);
    },
    async fetch_user(user_id: number) {
      let url: any = "http://127.0.0.1:8000/api/user/" + user_id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      let data: any = await response.json();
      this.user = data.user[0].email;
    },
    async fetch_users(user_id: number) {
      let url: any = "http://127.0.0.1:8000/api/user/" + user_id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      let data: any = await response.json();
      console.log("USERS", data);
      var users: any = this.users;
      var email = data.user[0].email;
      users.push({ user_id, email });
      this.users = users;
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
    async fetch_questions() {
      let response: any = await fetch("http://127.0.0.1:8000/api/questions/", {
        method: "GET",
      });
      let data: any = await response.json();
      console.log("QUESTIONS", data);
      let id: number = +this.id;
      this.questions = data.questions.filter(function (i: any, n: any) {
        return i.item === id;
      }, id);
      console.log("FILTERED", this.questions);
      for (let i = 0; i < this.questions.length; i++) {
        this.fetch_users(this.questions[i]["user"]);
      }
      console.log("FETCHED", this.users);
    },
    async check_id() {
      let response: any = await fetch("http://127.0.0.1:8000/api/uid/", {
        method: "GET",
      });
      let data: any = await response.json();
      this.user_id = data.id;
    },
  },
  mounted() {
    this.fetch_item();
    this.fetch_questions();
    this.check_id();
    window.setInterval(() => this.timeLeft(this.item[0]?.["auction_end_time"]), 1000);
  },
});
</script>
