<template>  

<v-app>
  <v-navigation-drawer
      class="deep-purple accent-4"
      :width="325"
      dark
      permanent
      app
    >
      <v-list>
        <v-list-item>
          <v-autocomplete
            v-model="gene"
            :items="genes"
            dense
            filled
            label="Gene name"

          ></v-autocomplete>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>
  
  <v-app-bar
    app
    color="primary"
    dark
  >
    <div class="d-flex align-center">
    </div>

  </v-app-bar>

  
  
  <v-main>

  <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <!-- If using vue-router -->
        <router-view :gene="gene"></router-view>
      </v-container>
    </v-main>  
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  
 
  
  name: 'App',

  data: () => ({
    genes: [],
    selectedGene: null,
    gene: null,
    gene_count: null,
    componentKey: 0,
  }),
  mounted() {
    axios
      .get("http://127.0.0.1:5000/api/v1/getGeneList")
      .then(response => {
        this.genes = response.data[0]["gene_names"];
        this.gene = this.genes[0]
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  }
};
</script>

