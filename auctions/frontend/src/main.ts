import { createApp } from 'vue'
import './assets/global.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css';
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/profile', component: () => import('./components/Profile.vue') },
        { path: '/editProfile', component: () => import('./components/EditProfile.vue') },
        { path: '/', component: () => import('./components/Login.vue') },
        { path: '/signup', component: () => import('./components/SignUp.vue') },
        { path: '/listings', component: () => import('./components/Listings.vue') },
        { path: '/listItem', component: () => import('./components/ListItem.vue') },
        { path: '/item/:id', component: () => import('./components/Item.vue') },
        { path: '/user/:id', component: () => import('./components/User.vue') },
        { path: '/question/:id', component: () => import('./components/Questions.vue') },
        { path: '/answer/:id', component: () => import('./components/Answers.vue') },
        { path: '/bid/:id', component: () => import('./components/Bid.vue') },
    ]
})

createApp(App).use(router).mount('#app')
