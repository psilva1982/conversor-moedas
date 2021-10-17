import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import highcharts from './plugins/highcharts'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  highcharts,
  render: h => h(App)
}).$mount('#app')
