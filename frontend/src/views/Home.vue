<template>
  <v-container>
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
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>

export default {
  data: () => ({
    symbol: null,
    symbols: [
      { id: 'RBL', description: 'Real' },
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
    getQuote () {
      console.log(this.symbol)
      console.log(this.date)
    }
  }
}
</script>
