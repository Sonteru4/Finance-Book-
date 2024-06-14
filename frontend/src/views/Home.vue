<template>
  <div>
    <Navbar/>
    <div class="container">
      <b-row style="margin-top: 40px; margin-bottom: 30px;" align="left">
        <b-col>
          <div style="float: left;">
            <span>
              <b>Chart Type</b>
            </span>
            <b-form-select style="margin-top: 5px;" v-model="chartType" :options="chartOptions"></b-form-select>
          </div>
        </b-col>
        <b-col>
          <div v-if="chartType" style="float: left;">
            <span>
              <b>First Value</b>
            </span>
            <b-form-select style="margin-top: 5px;" v-model="xValue" :options="xValueOptions"></b-form-select>
          </div>
        </b-col>
        <b-col>
          <div v-if="chartType && xValue" style="float: left;">
            <span>
              <b>Second Value</b>
            </span>
            <b-form-select
              @change="getGraph"
              style="margin-top: 5px;"
              v-model="yValue"
              :options="yValueOptions"
            ></b-form-select>
          </div>
        </b-col>
      </b-row>
      <lineChart v-if="chartType == 'line' && loadGraph" :datasets="datasets" :labels="labels"/>
      <barChart v-if="chartType == 'bar' && loadGraph" :datasets="datasets" :labels="labels"/>
      <h3
        v-if="chartType == 'pie' && loadGraph"
      >{{xValue.parent}} ({{xValue.val}}) : {{yValue.parent}} ({{yValue.val}})</h3>
      <pieChart v-if="chartType == 'pie' && loadGraph" :datasets="datasets" :labels="labels"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import GraphData from "@/assets/graph_data.json";
import lineChart from "../../charts/lineChart.js";
import barChart from "../../charts/barChart.js";
import pieChart from "../../charts/pieChart.js";

export default {
  name: "home",
  components: {
    Navbar,
    lineChart,
    barChart,
    pieChart
  },
  data() {
    return {
      xLabel: null,
      yLabel: null,
      loadGraph: false,
      chartType: null,
      xValue: null,
      yValue: null,
      graph_data: GraphData,
      chartOptions: [
        { value: null, text: "Please select a chart" },
        { value: "line", text: "Line Chart" },
        { value: "bar", text: "Bar Chart" },
        { value: "pie", text: "Pie Chart" }
        // { value: "area", text: "Area Chart" }
      ],
      xValueOptions: null,
      yValueOptions: null,
      labels: [],
      datasets: [
        {
          label: "",
          backgroundColor: "#31418d",
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ]
    };
  },
  methods: {
    async getGraph() {
      this.labels = [];
      this.datasets[0].data = [];
      await this.getXvalue(); // Get Labels (X axis values)
      await this.getYvalue(); // Get Datasets (Y axis values)
      // this.datasets[0].label =
      //   this.xValue.parent +
      //   " - " +
      //   this.xValue.val +
      //   " (x-axis) vs " +
      //   this.yValue.parent +
      //   " - " +
      //   this.yValue.val +
      //   " (y-axis)";
      this.datasets[0].label =
        this.xValue.val +
        " of " +
        this.xValue.parent +
        " (x-axis) vs " +
        this.yValue.val +
        " of " +
        this.yValue.parent +
        " (y-axis)";
      this.loadGraph = true;
    },
    getXvalue() {
      for (var j in GraphData[0]) {
        if (j == this.xValue.parent) {
          if (typeof GraphData[0][j] == "object") {
            for (var k in GraphData[0][j]) {
              if (k == this.xValue.val) {
                for (var i in GraphData) {
                  this.labels.push(GraphData[i][j][k]);
                  this.xLabel = k;
                }
                return;
              }
            }
            return;
          } else {
            for (var i in GraphData) {
              this.labels.push(GraphData[i][j]);
              this.xLabel = j;
            }
          }
          return;
        }
      }
    },
    getYvalue() {
      for (var j in GraphData[0]) {
        if (j == this.yValue.parent) {
          if (typeof GraphData[0][j] == "object") {
            for (var k in GraphData[0][j]) {
              if (k == this.yValue.val) {
                for (var i in GraphData) {
                  this.datasets[0].data.push(GraphData[i][j][k]);
                  this.yLabel = k;
                }
                return;
              }
            }
            return;
          } else {
            for (var i in GraphData) {
              this.datasets[0].data.push(GraphData[i][j]);
              this.yLabel = j;
            }
          }
          return;
        }
      }
    }
  },
  async mounted() {
    try {
      let response = await axios_instance.get("YOUR_API_NAME");
      // data from response.data as per your api configuration
    } catch (err) {
      // alert("Error!");
    }
    var graphData = GraphData[0];
    var tempJSON = [
      { parent: null, value: null, text: "Please select a chart" }
    ];
    for (var i in graphData) {
      if (typeof graphData[i] == "object") {
        for (var j in graphData[i]) {
          var sub_key = j; // Key
          var sub_val = graphData[i][j]; // Value
          tempJSON.push({
            value: { parent: i, val: sub_key },
            text: i + " (" + sub_key + ")"
          });
        }
      } else {
        tempJSON.push({ value: { parent: i, val: i }, text: i });
      }
    }
    this.xValueOptions = tempJSON;
    this.yValueOptions = tempJSON;
  }
};
</script>
