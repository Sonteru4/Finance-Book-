<template>
<div>
  <Navbar />
  <div class="custom-container">
    <b-tabs content-class="mt-3" fill style="margin-top: 50px;">
      <b-tab title="Cash Flow" active><cashFlow /></b-tab>
      <b-tab title="Balance Sheet"><balanceSheet /></b-tab>
      <b-tab title="DCF"><dcf /></b-tab>
    </b-tabs>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import cashFlow from "@/views/cashFlow.vue";
import dcf from "@/views/dcf.vue";
import balanceSheet from "@/views/balanceSheet.vue";

export default {
  name: "tables",
  components: {
    Navbar,
    cashFlow,
    balanceSheet,
    dcf
  },
  data() {
      return {
        fields: ['first_name', 'last_name', 'age'],
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' }
        ]
      }
    }
};
</script>
