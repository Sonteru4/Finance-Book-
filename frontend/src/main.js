import Vue from "vue";
import Moment from "vue-moment";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue from "bootstrap-vue";
import "./custom.scss";

Vue.use(BootstrapVue);
Vue.use(Moment);
Vue.config.productionTip = false;

Vue.filter("amount", function(value) {
  if (!value) return "";
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
