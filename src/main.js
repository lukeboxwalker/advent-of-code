import Vue from 'vue'
import App from './App.vue'
import 'animate.css'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'

import './app.scss'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  render: h => h(App),
}).$mount('#app')
