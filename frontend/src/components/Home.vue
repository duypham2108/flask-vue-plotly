<template>
  <v-container>
    <vue-plotly ref="container" :data="data" :layout="layout" :options="options" />
    <div id="myDiv"></div>
  </v-container>
  
</template>

<script>
import VuePlotly from "@statnett/vue-plotly";
import axios from "axios";

const events = [
  'click',
  'hover',
  'unhover',
  'selecting',
  'selected',
  'restyle',
  'relayout',
  'autosize',
  'deselect',
  'doubleclick',
  'redraw',
  'animated',
  'afterplot'
]

export default {
  watch: {
    gene: function(val) {
      this.getGeneCount()
    }
  
  },
  props: ["gene"],
  components: {
    VuePlotly
  },
  data() {
    return {
      data: null,
      myPlot: "123",
      layout: {
        title: "Spatial",
        autosize: false,
        width: 600,
        height: 600,
        images: [
          {
            "xref": "x",
            "yref": "y",
            "x": 1,
            "y": 3,
            "sizex": 2,
            "sizey": 2,
            "sizing": "stretch",
            "opacity": 0.4,
            "layer": "below"
          },
        ],
        xaxis: {
            showgrid: false,
            showticklabels: false
        },
        yaxis: {
            showgrid: false,
            showticklabels: false
        },
      },
      options: {
        displaylogo: false,
        scrollZoom: true,
        responsive: true,
  
        
        },
      
    };
  },
  created() {
    this.$refs.container.$on('selected', d => {
        console.log("123")
    })
  },
  
  mounted() {
    axios
      .get("http://127.0.0.1:5000/api/v1/sin")
      .then(response => {
        this.data = response.data;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));

    console.log("data is", this.gene);


    var graphDiv = document.getElementById('myDiv');
    var N = 1000;
    var color1 = '#7b3294';
    var color1Light = '#c2a5cf';
    var colorX = '#ffa7b5';
    var colorY = '#fdae61';

    function randomArray() {
      var out = new Array(N);
      for(var i = 0; i < N; i++) {
        out[i] = Math.random();
      }
      return out;
    }
    var x = randomArray();
    var y = randomArray();

    Plotly.newPlot(graphDiv, [{
      type: 'scatter',
      mode: 'markers',
      x: x,
      y: y,
      xaxis: 'x',
      yaxis: 'y',
      name: 'random data',
      marker: {color: color1, size: 10}
    }, {
      type: 'histogram',
      x: x,
      xaxis: 'x2',
      yaxis: 'y2',
      name: 'x coord dist.',
      marker: {color: colorX}
    }, {
      type: 'histogram',
      x: y,
      xaxis: 'x3',
      yaxis: 'y3',
      name: 'y coord dist.',
      marker: {color: colorY}
    }], {
      title: 'Lasso around the scatter points to see sub-distributions',
      dragmode: 'lasso',
      xaxis: {
        zeroline: false,
      },
      yaxis: {
        domain: [0.55, 1],
      },
      xaxis2: {
        domain: [0, 0.45],
        anchor: 'y2',
      },
      yaxis2: {
        domain: [0, 0.45],
        anchor: 'x2'
      },
      xaxis3: {
        domain: [0.55, 1],
        anchor: 'y3'
      },
      yaxis3: {
        domain: [0, 0.45],
        anchor: 'x3'
      }
    });

    graphDiv.on('plotly_selected', function(eventData) {
      var x = [];
      var y = [];

      var colors = [];
      for(var i = 0; i < N; i++) colors.push(color1Light);

      console.log(eventData.points)

      eventData.points.forEach(function(pt) {
        x.push(pt.x);
        y.push(pt.y);
        colors[pt.pointNumber] = color1;
      });

      Plotly.restyle(graphDiv, {
        x: [x, y],
        xbins: {}
      }, [1, 2]);

      Plotly.restyle(graphDiv, 'marker.color', [colors], [0]);
    });

  
    
    
    
  },

  methods: {
    getGeneCount() {
      axios
      .get("http://127.0.0.1:5000/api/v1/getGeneCount", {
        params: {
          "gene": this.gene
        }
      }) 
      .then(response => {
        this.gene_count = response.data[0].gene_count;
        this.data[0].marker.color = this.gene_count;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));

      


    },



  },


};
</script>
