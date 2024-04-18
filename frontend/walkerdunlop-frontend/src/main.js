import { createApp } from 'vue'
import App from './App.vue'

import { LMap, LTileLayer, LMarker, LPopup } from 'vue3-leaflet';
// import 'leaflet/dist/leaflet.css';

import './assets/css/app.css'
import router from './router';
import Notifications from '@kyvg/vue3-notification'


const app = createApp(App)
app.use(router)
app.use(Notifications)
app.component('l-map', LMap);
app.component('l-tile-layer', LTileLayer);
app.component('l-marker', LMarker);
app.component('l-popup',LPopup)
app.mount('#app')
