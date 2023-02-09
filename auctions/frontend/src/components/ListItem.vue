<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card bg-dark text-white" style="border-radius: 1rem;">
                        <div class="card-body p-5 text-center">

                            <div class="mb-md-5 mt-md-4 pb-5">

                                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">List Item</h2>
                                <form id="post" class="p-1">
                                    <div class="form-outline form-white mb-4">
                                        <input type="text" id="typeItemX" name="title"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2 " for="typeItemX">Listing
                                            Title</label>
                                    </div>
                                    <div class="form-outline form-white mb-4">
                                        <textarea type="text" id="typeItemX" name="description"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2 " for="typeItemX">Description</label>
                                    </div>
                                    <div class="form-outline form-white mb-4">
                                        <input type="number" id="typePriceX" name="price"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typePriceX">Price</label>
                                    </div>

                                    <div class="form-outline form-white mb-4">
                                        <input type="datetime-local" name="end_time" id="typeDateTime2X"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeDateTime2X">Termination of
                                            Bid</label>
                                    </div>

                                    <div class="form-outline form-white mb-4">
                                        <input type="file" name="picture" id="typeImageX" accept="image/*"
                                            v-on:change="changeImage()" class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeImageX">Upload Item
                                            Picture</label>
                                    </div>
                                </form>

                                <button class="btn btn-outline-light btn-lg px-5" @click="send_question()"
                                    type="submit">List</button>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            image: undefined,
        }
    },
    components: {},
    methods: {
        getCookie() {
            let cookieValue: string = "";
            if (document.cookie && document.cookie !== '') {
                var cookies: string[] = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie: string = cookies[i].trim();
                    if (cookie.substring(0, 10) === ('csrftoken=')) {
                        cookieValue = decodeURIComponent(cookie.substring(10));
                        break;
                    }
                }
            }
            return cookieValue;
        },
        async send_question() {
            var form = document.getElementById("post") as HTMLFormElement;
            let d: Date = new Date();
            let n: any = (<HTMLInputElement>document.getElementById("typeDateTime2X")).value
            if (n < d.toISOString()) {
                alert("Please enter a future date");
                return;
            }
            if (form) {
                const data = new FormData(form);
                if (this.image) {
                    data.append("picture", this.image);
                }
                let response = await fetch('http://127.0.0.1:8000/api/items/', {
                    method: "POST",
                    body: data,
                    headers: {
                        "X-CSRFToken": this.getCookie(),
                    },
                });
                window.location.replace("http://127.0.0.1:8000/listings")
            }
        },
        changeImage() {
            let pic: any = document.getElementById("typeImageX");
            this.image = pic;
        },
    },
});
</script>