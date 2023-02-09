<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card bg-dark text-white" style="border-radius: 1rem;">
                        <div class="card-body p-5 text-center">

                            <div class="mb-md-5 mt-md-4 pb-5">

                                <h2 class="fw-bold mb-2 text-uppercase card-text-colour">Signup</h2>
                                <p class=" mb-5 card-text-colour2">Please enter your login and password!
                                </p>
                                <form id="post" class="p-1">
                                    <div class="form-outline form-white mb-4">
                                        <input type="email" name="email" v-model="email" id="typeEmailX"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2 " for="typeEmailX">Email</label>
                                    </div>



                                    <div class="form-outline form-white mb-4">
                                        <input type="password" name="password" v-model="password" id="typePasswordX"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typePasswordX">Password</label>
                                    </div>



                                    <div class="form-outline form-white mb-4">
                                        <input type="date" name="dob" id="typeDateX" v-model="dob"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeDateX">Date of
                                            Birth</label>
                                    </div>

                                    <div class="form-outline form-white mb-4">
                                        <input type="text" name="city" id="typeCityX" v-model="city"
                                            class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeCityX">City</label>
                                    </div>

                                    <div class="form-outline form-white mb-4">
                                        <input type="file" name="picture" id="typeImageX" accept="image/*"
                                            v-on:change="changeImage()" class="form-control form-control-lg" />
                                        <label class="form-label card-text-colour2" for="typeImageX">Upload Profile
                                            Picture</label>
                                    </div>
                                </form>

                                <button class="btn btn-outline-light btn-lg px-5" @click='add_user'>Signup</button>

                            </div>

                            <div>
                                <p class="mb-0 card-text-colour2">Already have an account?
                                    <router-link to="/login"><a href="#"
                                            class="card-text-colour2 fw-bold">Login</a></router-link>
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
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            users: [],
            image: undefined,
            email: "",
            password: "",
            dob: "",
            city: "",
        }
    },
    components: {},
    methods: {
        async get_csrf() {
            let response = await fetch('http://127.0.0.1:8000/login/', {
                method: "GET",
            })
            let data = await response.text();
        },
        async get_users() {
            let response = await fetch('http://127.0.0.1:8000/api/users/', {
                method: "GET",
            })
            let data = await response.json()
            this.users = data.users
        },
        async add_user() {
            let form = document.getElementById("post") as HTMLFormElement;
            let e_mail: string = (<HTMLInputElement>document.getElementById("typeEmailX")).value;
            let p_word: string = (<HTMLInputElement>document.getElementById("typePasswordX")).value;
            let d_ate: any = (<HTMLInputElement>document.getElementById("typeDateX")).value;
            let c_ity: string = (<HTMLInputElement>document.getElementById("typeCityX")).value;
            let p_rofilepic: any = (<HTMLInputElement>document.getElementById("typeImageX")).value;
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
            if (e_mail == "" && p_word == "" && !(d_ate) && c_ity == "" && (!p_rofilepic)) {
                alert("Please enter your details"); return;
            }
            if (e_mail == "") {
                alert("Please enter your email");
                return;
            }
            if (p_word == "") {
                alert("Please enter your password");
                return;
            }
            if (c_ity == "") {
                alert("Please enter your city");
                return;
            }
            if (!(p_rofilepic)) {
                alert("Please add your profile image");
                return;
            }
            let d: Date = new Date();
            if (d_ate > d.toISOString()) {
                alert("Please enter a past date");
                return;
            }
            if (d_ate > new Date()) {
                alert("Please enter a valid date");
                return;
            }
            if (!(d_ate)) {
                alert("Please enter your date");
                return;
            }

            if (form) {
                const data = new FormData(form);
                if (this.image) {
                    data.append("picture", this.image);
                }
                let response = await fetch('http://127.0.0.1:8000/api/users/', {
                    method: "POST",
                    body: data,
                    headers: {
                        "X-CSRFToken": this.getCookie(),
                    },
                });
                window.location.replace("http://127.0.0.1:8000")
            }
            this.get_users();
        },
        changeImage() {
            let pic: any = document.getElementById("typeImageX");
            this.image = pic;
        },
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
    },
    mounted() {
        this.get_csrf();
        this.get_users();
    },
});
</script>