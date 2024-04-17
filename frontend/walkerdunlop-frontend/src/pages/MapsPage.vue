<template>
    <div>
      <header class="bg-blue-500 text-white py-4">
        <div class="container mx-auto text-center">
          <h1 class="text-2xl font-semibold">Welcome to My Maps</h1>
        </div>
      </header>
  
      <div style="height: 500px;margin-top:0px">
        <l-map :zoom="zoom" :center="center">
          <l-tile-layer :url="url"></l-tile-layer>
          <l-marker :lat-lng="center"></l-marker>
        </l-map>
      </div>
  
      <footer class="bg-gray-200 py-4">
        <div class="container mx-auto text-center">
          <p class="text-sm text-gray-600">© 2024 My Maps. All rights reserved.</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    props: ['latitude', 'longitude'],
    setup(props) {
    const zoom = ref(15); // Adjust the zoom level as needed
    const center = ref([props.latitude, props.longitude]);
    const url = 'https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png';

    return { zoom, center, url };
    }
  }
  </script>

  
<style>

</style>
