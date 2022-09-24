import {createApp} from 'vue'
import {createPinia} from "pinia"
import App from './App.vue'
import {Quasar} from 'quasar'
import router from './router'
import quasarUserOptions from './quasar-user-options'


import 'animate.css';
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'


import hljs from 'highlight.js/lib/core';
import javascript from 'highlight.js/lib/languages/javascript';
import hljsVuePlugin from '@highlightjs/vue-plugin';
import 'highlight.js/styles/an-old-hope.css'

// Register the languages you want to use
hljs.registerLanguage('javascript', javascript);

const app = createApp(App)

app.use(router)
app.use(hljsVuePlugin);
app.use(createPinia())
app.use(Quasar, quasarUserOptions)

app.mount('#app')