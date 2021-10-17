<template>
  <v-container fluid>
    <v-card>
      <v-card-title>Dados salvos na API</v-card-title>
      <v-card-text>
        <v-data-table
          :headers="header"
          :items="quotes"
          :options.sync="pagination"
          :server-items-length="totalQuotes"
          loading-text="Carregando cotações ..."
          no-data-text="Nenhum resultado encontrado ..."
          :loading="loading"
        >
        </v-data-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import * as quoteService from '@/services/QuoteService'
export default {
  data: () => ({
    loading: false,
    quotes: [],
    totalQuotes: 0,
    pagination: {},
    header: [
      { text: 'Data', value: 'date' },
      { text: 'Moeda', value: 'symbol' },
      { text: 'Valor', value: 'value' }
    ]
  }),

  watch: {
    pagination: {
      handler () {
        this.search()
      },
      deep: true
    }
  },

  methods: {
    async search () {
      this.loading = true
      try {
        const { sortBy, sortDesc, page, itemsPerPage } = this.pagination
        const result = await quoteService.list(
          sortBy,
          sortDesc,
          page,
          itemsPerPage
        )
        this.quotes = result.data.results
        this.totalQuotes = result.data.count
      } catch (err) {
        console.log(err)
      }
      this.loading = false
    }
  }
}
</script>

<style>
</style>
