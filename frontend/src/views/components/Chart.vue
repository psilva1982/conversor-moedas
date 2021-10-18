<template>
  <highcharts :options="chartOptions"></highcharts>
</template>

<script>
const moment = require('moment')

export default {
  props: ['data'],
  data: () => ({
    chartOptions: {
      chart: {
        type: 'spline'
      },
      title: {
        text: 'Cotação do Dólar'
      },
      series: [{
        name: '',
        data: []
      }],
      xAxis: {
        type: 'datetime'
      }
    }
  }),

  mounted () {
    this.chartOptions.series[0].name = this.data[0].symbol
    const values = []
    this.data.forEach(quote => {
      const value = { x: moment(quote.date).toDate(), y: parseFloat(quote.value) }
      console.log(value[0])
      values.push(value)
    })

    this.chartOptions.series[0].data = values
  }
}
</script>

<style>
</style>
