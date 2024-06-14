<template>
  <b-container fluid style="padding-bottom: 70px;">
    <h3 style="margin-top: 50px;">
      <b>CASH FLOW</b>
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
            <th>Period Ending</th>
            <th
              v-for="item in items"
              v-bind:key="item.endDate"
            >{{item.endDate | moment("DD-MMM-YYYY")}}</th>
          </tr>
          <tr>
            <td>Net Income</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.netIncome || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.netIncome"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr class="custom-header">
            <td colspan="6">
              <b>Operating Activities, Cash Flows Provided by Organization</b>
            </td>
          </tr>
          <tr>
            <td>Depreciation</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.depreciation || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.depreciation"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Adjustments to Net Income</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.changeToNetincome || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.changeToNetincome"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Changes in Accounts Receivables</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.changeToAccountReceivables || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.changeToAccountReceivables"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Changes in Liabilities</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.changeToLiabilities || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.changeToLiabilities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Changes in Inventories</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.changeToInventory || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.changeToInventory"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Changes in Other Operating Activities</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">{{item.changeToOperatingActivities || "0" | amount}}</span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.changeToOperatingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>
              <b>Total Cash Flow from Operating Activities</b>
            </td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.totalCashFromOperatingActivities || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.totalCashFromOperatingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr class="custom-header">
            <td colspan="6">
              <b>Investing Activities, Cash Flows Provided by Organization</b>
            </td>
          </tr>
          <tr>
            <td>Capital Expenditures</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.capitalExpenditures || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.capitalExpenditures"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Investments</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.investments || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.investments"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Other Cash Flows from Investing Activities</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.otherCashflowsFromInvestingActivities || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.otherCashflowsFromInvestingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>
              <b>Total Cash Flows from Investing Activities</b>
            </td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.totalCashflowsFromInvestingActivities || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.totalCashflowsFromInvestingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr class="custom-header">
            <td colspan="6">
              <b>Financing Activities, Cash Flows Provided by Organization</b>
            </td>
          </tr>
          <tr>
            <td>Dividends Paid</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.dividendsPaid || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.dividendsPaid"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Sale Purchase of Stock</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.repurchaseOfStock || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.repurchaseOfStock"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Net Borrowings</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.netBorrowings || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.netBorrowings"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>Other Cash Flows from Financing Activities</td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.otherCashflowsFromFinancingActivities || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.otherCashflowsFromFinancingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <tr>
            <td>
              <b>Total Cash Flows from Financing Activities</b>
            </td>
            <td v-for="item in items" v-bind:key="item">
              <span v-if="!editMode">
                <b>{{item.totalCashFromFinancingActivities || "0" | amount}}</b>
              </span>
              <b-form-input
                v-if="editMode"
                style="font-size: 12px;"
                v-model="item.totalCashFromFinancingActivities"
                type="text"
              ></b-form-input>
            </td>
          </tr>
          <!-- <tr class="custom-header">
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
          </tr>-->
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
          _id: "5cf65c24eb81c76b2146e281",
          changeToInventory: 50000000,
          endDate: 1498780800,
          repurchaseOfStock: "-11788000000",
          netIncome: "25489000000",
          maxAge: 1,
          netBorrowings: "31459000000",
          totalCashflowsFromInvestingActivities: "-46781000000",
          otherCashflowsFromFinancingActivities: -190000000,
          changeToOperatingActivities: 349000000,
          issuanceOfStock: 772000000,
          effectOfExchangeRate: 19000000,
          changeToAccountReceivables: -1216000000,
          ticker: "MSFT",
          dividendsPaid: "-11845000000",
          changeToNetincome: 1287000000,
          capitalExpenditures: "-8129000000",
          changeToLiabilities: "3901000000",
          otherCashflowsFromInvestingActivities: -197000000,
          totalCashFromFinancingActivities: "8408000000",
          depreciation: "7800000000",
          changeInCash: 1153000000,
          totalCashFromOperatingActivities: "39507000000",
          investments: "-12511000000"
        },
        {
          _id: "5cf65c24eb81c76b2146e281",
          changeToInventory: 50000000,
          endDate: 1498780800,
          repurchaseOfStock: "-11788000000",
          netIncome: "89894949",
          maxAge: 1,
          netBorrowings: "31459000000",
          totalCashflowsFromInvestingActivities: "-46781000000",
          otherCashflowsFromFinancingActivities: -190000000,
          changeToOperatingActivities: 349000000,
          issuanceOfStock: 772000000,
          effectOfExchangeRate: 19000000,
          changeToAccountReceivables: -1216000000,
          ticker: "MSFT",
          dividendsPaid: "-11845000000",
          changeToNetincome: 1287000000,
          capitalExpenditures: "-8129000000",
          changeToLiabilities: "3901000000",
          otherCashflowsFromInvestingActivities: -197000000,
          totalCashFromFinancingActivities: "8408000000",
          depreciation: "7800000000",
          changeInCash: 1153000000,
          totalCashFromOperatingActivities: "39507000000",
          investments: "-12511000000"
        },
        {
          _id: "5cf65c24eb81c76b2146e281",
          changeToInventory: 5465165165,
          endDate: 1498780800,
          repurchaseOfStock: "-11788000000",
          netIncome: "7111232198",
          maxAge: 1,
          netBorrowings: "31459000000",
          totalCashflowsFromInvestingActivities: "-46781000000",
          otherCashflowsFromFinancingActivities: -190000000,
          changeToOperatingActivities: 349000000,
          issuanceOfStock: 772000000,
          effectOfExchangeRate: 19000000,
          changeToAccountReceivables: -1216000000,
          ticker: "MSFT",
          dividendsPaid: "-11845000000",
          changeToNetincome: 1287000000,
          capitalExpenditures: "-8129000000",
          changeToLiabilities: "3901000000",
          otherCashflowsFromInvestingActivities: -197000000,
          totalCashFromFinancingActivities: "8408000000",
          depreciation: "7800000000",
          changeInCash: 1153000000,
          totalCashFromOperatingActivities: "39507000000",
          investments: "-12511000000"
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
      let response = await axios_instance.get("YOUR_API_NAME");
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