import { getCookie  } from "./csrf_token.js"; //CSRF_TOKEN, 

async function getJSON(response) {
    if(response.status === 204) return '';
    else if (response.status === 401) return null
    return response.json()
}

function apiService(endpoint, method, data) {
    let token = getCookie("csrftoken")
    const config = {
        method: method || "GET",
        body: data !== undefined ? JSON.stringify(data) : null,
        headers: {
            "content-type": "application/json",
            "X-CSRFTOKEN": token
        }
    }
    return fetch(endpoint, config)
        .then(getJSON)
}

const axios = require("axios");
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.headers.common['Accept'] = 'application/json'

export { apiService, axios };