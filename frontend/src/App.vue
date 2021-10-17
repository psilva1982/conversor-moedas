<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-spacer></v-spacer>

      <v-btn text to="/">
        <v-icon class="mr-1">mdi-chart-bar</v-icon>
        <span class="mt-1">Gráfico</span></v-btn
      >
      <v-btn text to="/data">
        <v-icon class="mr-1">mdi-table</v-icon>
        <span class="mt-1">Dados salvos</span></v-btn
      >

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <v-icon class="mr-1">mdi-rocket-launch</v-icon>
        <span class="mr-2">Consulta API</span>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>
