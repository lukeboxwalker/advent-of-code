import Vue from 'vue'
import App from './App.vue'
import 'animate.css'
import './app.scss'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import VueRouter from 'vue-router'

import router from "./router";

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)

new Vue({
    render: h => h(App),
    router,
}).$mount('#app')
