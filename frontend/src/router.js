import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Tables from "./views/Tables.vue";
import Upload from "./views/Upload.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/tables",
      name: "tables",
      component: Tables
   },
   {
      path: "/upload",
      name: "upload",
      component: Upload
   },
  ]
});
