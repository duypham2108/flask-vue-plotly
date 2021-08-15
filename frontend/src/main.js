import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Buefy from "buefy";
import "buefy/dist/buefy.css";
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false;
Vue.use(Buefy);

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
