const a_req = require('axios')

async function getActivity(){
    try{
        let response = await axiosRequest.get('https://www.boredapi.com/api/activity')
        console.log(`You could ${response.data.activity}`)
    } catch(error){
        console.log(`ERROR: ${error}`)
    }
}
getActivity()
