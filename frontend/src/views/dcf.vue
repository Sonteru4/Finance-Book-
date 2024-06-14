<template>
  <b-container fluid style="padding-bottom: 70px;">
    <h3 style="margin-top: 50px;">
      <b>DCF</b>
    </h3>
    <b-button
      style="float: right;"
      @click="editMode = !editMode"
      variant="primary"
    >{{editMode ? 'CANCEL' : 'EDIT'}}</b-button>
    <b-button
      style="float: right; margin-right: 5px;"
      @click="editMode = !editMode; saveData();"
      variant="primary"
      v-if="editMode"
    >SAVE</b-button>
    <!-- Main table element -->
    <b-row style="margin-top: 50px;">
      <b-col class="div-with-scroll">
        <table style="min-width: 700px !important">
          <tr class="custom-header" style="border: 3px solid #ddd !important;">
            <th>Title</th>
            <th v-for="item in items" v-bind:key="item.year">{{item.year}}</th>
          </tr>

          <tr>
            <td>Net Income</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.net_income || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.net_income"
                type="text"
              ></b-form-input>
            </td>
          </tr>

          <tr class="custom-header">
            <td colspan="6">Operating Expense</td>
          </tr>
          <tr>
            <td>Research Development</td>
            <td v-for="item in items" v-bind:key="item.operating_expense">
              <span v-if="!editMode">{{item.operating_expense.research_development}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.operating_expense.research_development"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>General & Administraive</td>
            <td v-for="item in items" v-bind:key="item.operating_expense">
              <span v-if="!editMode">{{item.operating_expense.selling_general_and_administrative}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.operating_expense.selling_general_and_administrative"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Non Recurring</td>
            <td v-for="item in items" v-bind:key="item.operating_expense">
              <span v-if="!editMode">{{item.operating_expense.non_recurring}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.operating_expense.non_recurring"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Others</td>
            <td v-for="item in items" v-bind:key="item.operating_expense">
              <span v-if="!editMode">{{item.operating_expense.others}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.operating_expense.others"
                type="text"
              ></b-form-input>
            </td>
          </tr>

          <tr class="custom-header">
            <td colspan="6">Other Income / Expense</td>
          </tr>
          <tr>
            <td>Income Tax</td>
            <td v-for="item in items" v-bind:key="item.other_income_or_expense">
              <span v-if="!editMode">{{item.other_income_or_expense.income_tax_expense}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.other_income_or_expense.income_tax_expense"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Interest</td>
            <td v-for="item in items" v-bind:key="item.other_income_or_expense">
              <span v-if="!editMode">{{item.other_income_or_expense.interest_expense}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.other_income_or_expense.interest_expense"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Other Income / Expense</td>
            <td v-for="item in items" v-bind:key="item.other_income_or_expense">
              <span v-if="!editMode">{{item.other_income_or_expense.other_expense_or_income}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.other_income_or_expense.other_expense_or_income"
                type="text"
              ></b-form-input>
            </td>
          </tr>

          <tr class="custom-header">
            <td colspan="6">Revenue</td>
          </tr>
          <tr>
            <td>Total Revenue</td>
            <td v-for="item in items" v-bind:key="item.revenue">
              <span v-if="!editMode">{{item.revenue.total_revenue}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.revenue.total_revenue"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Gross Profit</td>
            <td v-for="item in items" v-bind:key="item.revenue">
              <span v-if="!editMode">{{item.revenue.gross_profit}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.revenue.gross_profit"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Revenue Cost</td>
            <td v-for="item in items" v-bind:key="item.revenue">
              <span v-if="!editMode">{{item.revenue.cost_of_revenu}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.revenue.cost_of_revenu"
                type="text"
              ></b-form-input>
            </td>
          </tr>
        </table>
      </b-col>
    </b-row>
    <div style="margin-top: 25px; text-align: center">
      <b-button @click="prevPageAction()" variant="outline-primary">Prev</b-button>
      <span>&nbsp;</span>
      <span style="padding: 15px;">
        <b>{{pageCount}}</b>
      </span>
      <span>&nbsp;</span>
      <b-button @click="nextPageAction()" variant="outline-primary">Next</b-button>
    </div>
    <!-- Info modal -->
    <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
      <pre>{{ infoModal.content }}</pre>
    </b-modal>
  </b-container>
</template>

<script>
import axios_instance from "../axios_instance.js";

export default {
  data() {
    return {
      items: [
        {
          year: 2016,
          other_income_or_expense: {
            other_expense_or_income: 10123,
            income_tax_expense: 1036,
            interest_expense: 0
          },
          net_income: 9130,
          operating_expense: {
            research_development: 2000,
            selling_general_and_administrative: 10012,
            non_recurring: 2022,
            others: 3033
          },
          revenue: {
            total_revenue: 10000,
            gross_profit: 9500,
            cost_of_revenu: 5000
          }
        },
        {
          year: 2017,
          other_income_or_expense: {
            other_expense_or_income: 10123,
            income_tax_expense: 1036,
            interest_expense: 0
          },
          net_income: 9130,
          operating_expense: {
            research_development: 2000,
            selling_general_and_administrative: 10012,
            non_recurring: 2022,
            others: 3033
          },
          revenue: {
            total_revenue: 10000,
            gross_profit: 9500,
            cost_of_revenu: 5000
          }
        },
        {
          year: 2018,
          other_income_or_expense: {
            other_expense_or_income: 10123,
            income_tax_expense: 1036,
            interest_expense: 0
          },
          net_income: 9130,
          operating_expense: {
            research_development: 2000,
            selling_general_and_administrative: 10012,
            non_recurring: 2022,
            others: 3033
          },
          revenue: {
            total_revenue: 10000,
            gross_profit: 9500,
            cost_of_revenu: 5000
          }
        },
        {
          year: 2019,
          other_income_or_expense: {
            other_expense_or_income: 10123,
            income_tax_expense: 1036,
            interest_expense: 0
          },
          net_income: 9130,
          operating_expense: {
            research_development: 2000,
            selling_general_and_administrative: 10012,
            non_recurring: 2022,
            others: 3033
          },
          revenue: {
            total_revenue: 10000,
            gross_profit: 9500,
            cost_of_revenu: 5000
          }
        }
      ],
      fields: [
        {
          key: "operating_expense.research_development",
          label: "Research Development"
        },
        {
          key: "operating_expense.selling_general_and_administrative",
          label: "General & Administrative"
        },
        { key: "operating_expense.non_recurring", label: "Non Recurring" },
        { key: "operating_expense.others", label: "Others" },
        { key: "net_income", label: "Net Income" },
        {
          key: "other_income_or_expense.income_tax_expense",
          label: "Income Tax"
        },
        { key: "other_income_or_expense.interest_expense", label: "Interest" },
        {
          key: "other_income_or_expense.other_expense_or_income",
          label: "Other Income / Expense"
        },
        { key: "revenue.total_revenue", label: "Total Revenue" },
        { key: "revenue.gross_profit", label: "Gross Profit" },
        { key: "revenue.cost_of_revenu", label: "Revenue Cost" }
      ],
      pageCount: 1,
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 15],
      sortBy: null,
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      editMode: false,
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      }
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    }
  },
  async mounted() {
    // Set the initial number of items
    this.totalRows = this.items.length;
    try {
      let response = await axios_instance.get("ticker_fin?ticker=AAPL");
      // data from response.data as per your api configuration
    } catch (err) {
      //alert("Error!");
    }
  },
  methods: {
    async saveData() {
      try {
        let response = await axios_instance.post("YOUR_API_NAME", this.items);
        // data from response.data as per your api configuration
      } catch (err) {
        alert("Error!");
      }
    },
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    prevPageAction() {
      if (this.pageCount == 1) return;
      this.pageCount = this.pageCount - 1;
    },
    nextPageAction() {
      this.pageCount = this.pageCount + 1;
    }
  }
};
</script>

<style lang="scss" scoped>
table,
td,
th {
  border: 1px solid #ddd !important;
  font-size: 11px;
  text-align: left !important;
}

table {
  border-collapse: collapse !important;
  width: 100% !important;
}

th,
td {
  padding: 7px !important;
}

td:hover {
  background-color: #f0f0f0;
  cursor: pointer;
}
</style>