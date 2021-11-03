const axios = require("axios");
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.headers.common['Accept'] = 'application/json'

export { axios };