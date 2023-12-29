const a_req = require('axios')

a_req
    .get('https://www.boredapi.com/api/activity')
    .then(response => {
        console.log(`You could ${response.data.activity}`)
    })
    .catch(error => {
        console.log(`ERROR! ${error}`)
    })
