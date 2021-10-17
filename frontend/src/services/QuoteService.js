import http from '../config/http'


export const get = (searchData) => {

    const url = `?date=${searchData.date}&symbol=${searchData.symbol}`

    return http.get(url)
}
