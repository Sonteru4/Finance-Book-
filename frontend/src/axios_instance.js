const axios = require("axios");
const defaultOptions = {
  baseURL: process.env.VUE_APP_API_URL // VUE_APP_API_URL can ve found in the .env file
};
let axiosInstance = axios.create(defaultOptions);
axiosInstance.interceptors.request.use(function(config) {
  // let token = "";
  // config.headers.Authorization = token ? `Bearer ${token}` : "";
  return config;
});

export default axiosInstance;



