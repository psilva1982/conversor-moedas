import http from '../config/http'

export const get = (searchData) => {
  const url = `api/dollar-quote/?date=${searchData.date}&symbol=${searchData.symbol}`
  return http.get(url)
}

export const list = (sortBy, sortDesc, page, itemsPerPage) => {
  // Ajustando a ordenação
  if (sortDesc === 'true') {
    sortBy = '-' + sortBy
  }
  return http.get(`api/quotes/?page=${page}&ordering=${sortBy}&page_size=${itemsPerPage}`)
}
