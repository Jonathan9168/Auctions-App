<template>
  <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">
                  Answer
                </h2>
                <!--<p class=" mb-1 card-text-colour2">Please answer a question below!
                                </p>-->
                <form id="post" class="p-1">
                  <!--
                                    <div class="form-outline form-white mb-4">
                                        <select id="selectquestion" name="selectquestion"
                                            class="form-control form-control-lg">
                                            <option value="test">Test</option>
                                        </select>
                                        <label class="form-label card-text-colour2" for="selectquestion">Select
                                            Question</label>
                                    </div>
                                    this page already knows the question id, so we don't need to ask the user to select it
                                    -->
                  <div class="form-outline form-white mb-4">
                    <p>Question: {{question}}</p>
                    <label class="form-label card-text-colour2" for="typeAnswerX">Enter your Answer here:</label>
                    <textarea id="typeAnswerX" class="form-control form-control-lg" required />
                  </div>
                </form>

                <button class="btn btn-outline-light btn-lg px-5" @click="send_answer" type="submit">
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
      question: "",
    };
  },
  components: {},
  methods: {
    async send_answer() {
      let answer1: string = (<HTMLInputElement>document.getElementById("typeAnswerX")).value;
      if (answer1 == "") {
        alert("Please type in the answer field");
        return;
      }
      let obj: any = document.getElementById("typeAnswerX");
      let answer: any = obj.value;
      console.log(this.get_id());
      let vars = {
        answer: answer,
        user: await this.get_id(),
        question: this.id,
      };

      let response: any = await fetch("http://127.0.0.1:8000/api/answers/", {
        method: "POST",
        headers: {
          "X-CSRFToken": this.getCookie(),
        },
        body: JSON.stringify(vars),
      });
      history.back();
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
    async fetch_question() {
      let url: any = "http://127.0.0.1:8000/api/question/" + this.id + "/";
      let response: any = await fetch(url, {
        method: "GET",
      });
      if (!response.ok){
        alert("This question does not exist")
        window.location.replace("http://127.0.0.1:8000/listings")
      }
      let data = await response.json()
      console.log(data)
      this.question = data.question[0].question
      if (data.question[0].answer != null){
        alert("This question has already been answered")
        window.location.replace("http://127.0.0.1:8000/listings")
      }
      let url2: any = "http://127.0.0.1:8000/api/item/" + data.question[0].item + "/";
      let res2: any = await fetch(url2, {
        method: "GET",
      });
      let data2 = await res2.json()
      let id2 = this.get_id()
      if (data2.item[0].user != id2){
        //alert("You cannot repond to a question about someone else's item!")
        //window.location.replace("http://127.0.0.1:8000/listings")
      }
    },
  },
  mounted(){
    this.fetch_question()
  }
});
</script>
