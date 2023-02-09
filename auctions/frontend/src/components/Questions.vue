<template>
  <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">
                  Question
                </h2>
                <!--<p class=" mb-1 card-text-colour2">Please enter your question below!
                                </p>-->
                <form id="post" class="p-1">
                  <!--<div class="form-outline form-white mb-4">
                                        <input type="text" id="typeItemX" class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeItemX">Item Name</label>
                                    </div>
                                    This page already knows what item it is.
                                    -->

                  <div class="form-outline form-white mb-4">
                    <label class="form-label card-text-colour2" for="typeQuestionX">Enter your question here:</label>
                    <textarea id="typeQuestionX" class="form-control form-control-lg" />
                  </div>

                  <!--
                                    <div class="form-outline form-white mb-4">
                                        <input type="datetime-local" id="typeTimeX"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeTimeX">Time
                                            Created:</label>
                                    </div>
                                    Creation time is added automatically
                                    -->
                </form>

                <button class="btn btn-outline-light btn-lg px-5" @click="send_question" type="submit">
                  Submit
                </button>
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

export default defineComponent({
  data() {
    return {
      id: this.$route.params.id,
    };
  },
  components: {},
  methods: {
    async send_question() {
      let question1: string = (<HTMLInputElement>document.getElementById("typeQuestionX")).value;
      if (question1 == "") {
        alert("Please type in the question field");
        return;
      }
      let obj: any = document.getElementById("typeQuestionX");
      let question: any = obj.value;
      console.log(await this.get_id());
      let vars = {
        question: question,
        user: await this.get_id(),
        item: this.id,
      };

      let response: any = await fetch("http://127.0.0.1:8000/api/questions/", {
        method: "POST",
        body: JSON.stringify(vars),
        headers: {
          "X-CSRFToken": this.getCookie(),
        },
      });
      history.back();
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
    },
    async get_id() {
      let response: any = await fetch("http://127.0.0.1:8000/api/uid/", {
        method: "GET",
      });
      let data: any = await response.json();
      return data.id;
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
  mounted(){
    this.fetch_item();
  }
});
</script>
