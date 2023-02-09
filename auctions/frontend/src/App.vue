<template>
  <NavBar />
  <div class="text-colour">
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import NavBar from './components/NavBar.vue';

export default defineComponent({
    data() {
    return{}
  },
  components: {
    NavBar,
  },
  methods:{},
});
</script>
