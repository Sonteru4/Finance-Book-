import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  props: ["datasets", "labels"],
  methods: {
    randomColorGenerator() {
      var letters = "0123456789ABCDEF";
      var color = "#";
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  },
  async mounted() {
    // console.log("this.datasets");
    // console.log(this.datasets);
    var tempLabel = [];
    await this.labels.forEach((element, index) => {
      tempLabel[index] = this.randomColorGenerator();
    });
    this.renderChart(
      {
        labels: this.labels,
        datasets: [
          {
            label: "Data One",
            backgroundColor: tempLabel,
            data: this.datasets[0].data
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
