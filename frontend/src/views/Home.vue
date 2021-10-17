<template>
  <v-container fluid>
    <v-card>
      <v-card-title>Gráfico de Cotações</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="12" lg="2">
            <v-select
              v-model="symbol"
              :items="symbols"
              item-text="description"
              item-value="id"
              label="Moeda"
              outlined
            ></v-select>
          </v-col>

          <v-col cols="12" sm="12" lg="2">
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              :return-value.sync="date"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="date"
                  label="Data"
                  prepend-inner-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  outlined
                ></v-text-field>
              </template>
              <v-date-picker v-model="date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu = false">
                  Cancel
                </v-btn>
                <v-btn text color="primary" @click="$refs.menu.save(date)">
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>

          <v-col cols="12" lg="1">
            <v-btn
              color="primary"
              class="mt-1 py-6"
              :disabled="!valid"
              @click="getQuote"
            >
              <v-icon class="mr-2">mdi-magnify</v-icon> Pesquisar</v-btn
            >
          </v-col>
        </v-row>

        <v-row v-if="quotes != null">
          <v-col cols="12" sm="12" lg="12"> <chart :data="quotes" /> </v-col>
        </v-row>
      </v-card-text>
    </v-card>
    <v-snackbar v-model="loading">
      <v-row no-gutters>
        <v-col cols="8">
          <span class="font-weight-medium">{{ message }} </span></v-col
        >
        <v-col cols="4" class="d-flex justify-end">
          <v-progress-circular size="26" indeterminate></v-progress-circular>
        </v-col>
      </v-row>
    </v-snackbar>
  </v-container>
</template>

<script>
import * as quotaService from '@/services/QuoteService'
import Chart from './components/Chart.vue'
export default {
  components: { Chart },
  data: () => ({
    loading: false,
    message: '',
    symbol: null,
    quotes: null,
    symbols: [
      { id: 'BRL', description: 'Real' },
      { id: 'EUR', description: 'Euro' },
      { id: 'JPY', description: 'Iene' }
    ],
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu: false

  }),

  computed: {

    valid () {
      if (this.symbol == null || this.symbol === '') return false
      return true
    }
  },

  methods: {
    async getQuote () {
      this.quotes = null
      this.message = 'Carregando'
      this.loading = true
      try {
        const res = await quotaService.get({ date: this.date, symbol: this.symbol })

        if (res.status === 200) {
          this.quotes = res.data
        }
      } catch (err) {
        console.log(err)
      }
      this.loading = false
    }
  }
}
</script>
