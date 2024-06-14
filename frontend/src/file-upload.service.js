// file-upload.service.js

import * as axios from 'axios';

const defaultOptions = {
    baseURL: process.env.VUE_APP_API_URL // VUE_APP_API_URL can ve found in the .env file
};

function upload(formData) {
    const url = `${defaultOptions.baseURL}upload_pdf`;
    return axios.post(url, formData)
    // get data
        .then(x => x.data)
        // add url field
        .then(x => x.map(img => Object.assign({},
            img, { url: `${defaultOptions.baseURL}/images/${img.id}` })));
}


function wait(ms) {
    return (x) => {
        return new Promise(resolve => setTimeout(() => resolve(x), ms));
    };
}

export { wait, upload }