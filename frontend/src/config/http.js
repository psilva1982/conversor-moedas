import axios from 'axios'
import https from 'https'

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const http = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,

  httpsAgent: new https.Agent({
    rejectUnauthorized: false
  })
})

export default http
