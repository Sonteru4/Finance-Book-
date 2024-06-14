<template>
  <div>
    <b-container fluid style="padding-bottom: 70px;">
      <h3 style="margin-top: 50px;">
        <b>BALANCE SHEET</b>
      </h3>
      <b-form-group label="Table Options">
        <b-form-checkbox v-model="striped" inline>Striped</b-form-checkbox>
        <b-form-checkbox v-model="bordered" inline>Bordered</b-form-checkbox>
        <b-form-checkbox v-model="borderless" inline>Borderless</b-form-checkbox>
        <b-form-checkbox v-model="outlined" inline>Outlined</b-form-checkbox>
        <b-form-checkbox v-model="small" inline>Small</b-form-checkbox>
        <b-form-checkbox v-model="hover" inline>Hover</b-form-checkbox>
        <b-form-checkbox v-model="dark" inline>Dark</b-form-checkbox>
        <b-form-checkbox v-model="fixed" inline>Fixed</b-form-checkbox>
        <b-form-checkbox v-model="footClone" inline>Foot Clone</b-form-checkbox>
      </b-form-group>
      <b-button
        style="float: right;"
        @click="editMode = !editMode"
        variant="primary"
      >{{editMode ? 'CANCEL' : 'EDIT'}}</b-button>
      <b-button
        style="float: right; margin-right: 5px;"
        @click="editMode = !editMode; saveData()"
        variant="primary"
        v-if="editMode"
      >SAVE</b-button>
      <!-- Main table element -->
      <b-row style="margin-top: 50px;">
        <b-col class="div-with-scroll">
          <table style="min-width: 700px !important">
            <tr class="custom-header" style="border: 3px solid #ddd !important;">
              <th>Title</th>
              <th
                v-for="item in items"
                v-bind:key="item.company_name"
              >{{item.current_assets.date | moment("DD-MMM-YYYY")}}</th>
            </tr>
            <tr>
              <td>Company Name</td>
              <td
                v-for="(item) in items"
                v-bind:key="item"
                @click="cellAction(item, 'company_name', '')"
              >
                <span v-if="!editMode">{{item.company_name}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.company_name"
                  type="text"
                ></b-form-input>
              </td>
            </tr>

            <tr class="custom-header">
              <td colspan="6">Current Assets</td>
            </tr>
            <tr>
              <td>Cash</td>
              <td
                v-for="(item) in items"
                v-bind:key="item"
                @click="cellAction(item, 'current_assets', 'cash')"
              >
                <span v-if="!editMode">{{item.current_assets.cash || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_assets.cash"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Inventory</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_assets"
                @click="cellAction(item, 'current_assets', 'inventory')"
              >
                <span v-if="!editMode">{{item.current_assets.inventory || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_assets.inventory"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Net Receivable</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_assets"
                @click="cellAction(item, 'current_assets', 'net_receivable')"
              >
                <span v-if="!editMode">{{item.current_assets.net_receivable || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_assets.net_receivable"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Other Current Assets</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_assets"
                @click="cellAction(item, 'current_assets', 'other_current_assets')"
              >
                <span v-if="!editMode">{{item.current_assets.other_current_assets || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_assets.other_current_assets"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Short Term Investment</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_assets"
                @click="cellAction(item, 'current_assets', 'short_term_investment')"
              >
                <span v-if="!editMode">{{item.current_assets.short_term_investment || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_assets.short_term_investment"
                  type="text"
                ></b-form-input>
              </td>
            </tr>

            <tr class="custom-header">
              <td colspan="6">Current Liabilities</td>
            </tr>
            <tr>
              <td>Accounts Payable</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_liabilities"
                @click="cellAction(item, 'current_liabilities', 'accounts_payable')"
              >
                <span v-if="!editMode">{{item.current_liabilities.accounts_payable || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_liabilities.accounts_payable"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Other Current Liabilities</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_liabilities"
                @click="cellAction(item, 'current_liabilities', 'other_current_liabilities')"
              >
                <span
                  v-if="!editMode"
                >{{item.current_liabilities.other_current_liabilities || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_liabilities.other_current_liabilities"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Short Debt</td>
              <td
                v-for="item in items"
                v-bind:key="item.current_liabilities"
                @click="cellAction(item, 'current_liabilities', 'short_debt')"
              >
                <span v-if="!editMode">{{item.current_liabilities.short_debt || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.current_liabilities.short_debt"
                  type="text"
                ></b-form-input>
              </td>
            </tr>

            <tr class="custom-header">
              <td colspan="6">Equity</td>
            </tr>
            <tr>
              <td>Capital Surplus</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'capital_surplus')"
              >
                <span v-if="!editMode">{{item.equity.capital_surplus || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.capital_surplus"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Common Stock</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'common_stock')"
              >
                <span v-if="!editMode">{{item.equity.common_stock || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.common_stock"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Misc Stocks Options Warrants</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'misc_stocks_options_warrants')"
              >
                <span v-if="!editMode">{{item.equity.misc_stocks_options_warrants || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.misc_stocks_options_warrants"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Other Stockholder Equity</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'other_stockholder_equity')"
              >
                <span v-if="!editMode">{{item.equity.other_stockholder_equity || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.other_stockholder_equity"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Redeemable Preferred Stock</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'redeemable_preferred_stock')"
              >
                <span v-if="!editMode">{{item.equity.redeemable_preferred_stock || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.redeemable_preferred_stock"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Retained Earnings</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'retained_earnings')"
              >
                <span v-if="!editMode">{{item.equity.retained_earnings || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.retained_earnings"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Treasury Stock</td>
              <td
                v-for="item in items"
                v-bind:key="item.equity"
                @click="cellAction(item, 'equity', 'treasury_stock')"
              >
                <span v-if="!editMode">{{item.equity.treasury_stock || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.equity.treasury_stock"
                  type="text"
                ></b-form-input>
              </td>
            </tr>

            <tr class="custom-header">
              <td colspan="6">Long Term Assets</td>
            </tr>
            <tr>
              <td>Amortization</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'amortization')"
              >
                <span v-if="!editMode">{{item.long_term_assets.amortization || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.amortization"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Deferred Long Term Assets Change</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'deferred_long_term_assets_change')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_assets.deferred_long_term_assets_change || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.deferred_long_term_assets_change"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Goodwill</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'goodwill')"
              >
                <span v-if="!editMode">{{item.long_term_assets.goodwill || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.goodwill"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Intangible Assets</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'intangible_assets')"
              >
                <span v-if="!editMode">{{item.long_term_assets.intangible_assets || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.intangible_assets"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Long Term Investment</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'long_term_investment')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_assets.long_term_investment || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.long_term_investment"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Other Assets</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'other_assets')"
              >
                <span v-if="!editMode">{{item.long_term_assets.other_assets || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.other_assets"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Property Plant Equipment</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_assets"
                @click="cellAction(item, 'long_term_assets', 'property_plant_equipment')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_assets.property_plant_equipment || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_assets.property_plant_equipment"
                  type="text"
                ></b-form-input>
              </td>
            </tr>

            <tr class="custom-header">
              <td colspan="6">Long Term Liabilities</td>
            </tr>
            <tr>
              <td>Deferred Long Term Liability</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_liabilities"
                @click="cellAction(item, 'long_term_liabilities', 'deferred_long_term_liability')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_liabilities.deferred_long_term_liability || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_liabilities.deferred_long_term_liability"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Long Term Debt</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_liabilities"
                @click="cellAction(item, 'long_term_liabilities', 'long_term_debt')"
              >
                <span v-if="!editMode">{{item.long_term_liabilities.long_term_debt || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_liabilities.long_term_debt"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Minority Interest</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_liabilities"
                @click="cellAction(item, 'long_term_liabilities', 'minority_interest')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_liabilities.minority_interest || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_liabilities.minority_interest"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Negative Goodwill</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_liabilities"
                @click="cellAction(item, 'long_term_liabilities', 'negative_goodwill')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_liabilities.negative_goodwill || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_liabilities.negative_goodwill"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
            <tr>
              <td>Other Liabilities</td>
              <td
                v-for="item in items"
                v-bind:key="item.long_term_liabilities"
                @click="cellAction(item, 'long_term_liabilities', 'other_liabilities')"
              >
                <span
                  v-if="!editMode"
                >{{item.long_term_liabilities.other_liabilities || "0" | amount}}</span>
                <b-form-input
                  v-if="editMode"
                  style="font-size: 12px;"
                  v-model="item.long_term_liabilities.other_liabilities"
                  type="text"
                ></b-form-input>
              </td>
            </tr>
          </table>
        </b-col>
      </b-row>
      <div style="margin-top: 25px; text-align: center;">
        <b-button @click="prevPageAction()" variant="outline-primary">Prev</b-button>
        <span>&nbsp;</span>
        <span style="padding: 15px;">
          <b>{{pageCount}}</b>
        </span>
        <span>&nbsp;</span>
        <b-button @click="nextPageAction()" variant="outline-primary">Next</b-button>
      </div>
      <!-- <b-row style="margin-top: 25px; margin-bottom: 100px !important; float: right">
      <b-col md="12" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          class="my-0"
        ></b-pagination>
      </b-col>
      </b-row>-->
      <!-- Info modal -->
      <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
        <pre>{{ infoModal.content }}</pre>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
import axios_instance from "../axios_instance.js";

export default {
  data() {
    return {
      items: [
        {
          company_name: "GM",
          current_assets: {
            cash: 15944000000.0,
            date: "2018-12-31 00:00:00",
            inventory: 9816000000.0,
            net_receivable: 6549000000.0,
            other_current_assets: 3392000000.0,
            short_term_investment: 5966000000.0
          },
          current_liabilities: {
            accounts_payable: 22297000000.0,
            date: "2018-12-31 00:00:00",
            other_current_liabilities: 6697000000.0,
            short_debt: 0.0
          },
          equity: {
            capital_surplus: 25563000000.0,
            common_stock: 14000000.0,
            date: "2018-12-31 00:00:00",
            misc_stocks_options_warrants: 0.0,
            other_stockholder_equity: -9039000000.0,
            preferred_stock: 0.0,
            redeemable_preferred_stock: 0.0,
            retained_earnings: 22322000000.0,
            treasury_stock: -9039000000.0
          },
          long_term_assets: {
            amortization: 0.0,
            date: "2018-12-31 00:00:00",
            deferred_long_term_assets_change: 6549000000.0,
            goodwill: 461000000.0,
            intangible_assets: 3718000000.0,
            long_term_investment: 7860000000.0,
            other_assets: 28976000000.0,
            property_plant_equipment: 38758000000.0
          },
          long_term_liabilities: {
            date: "2018-12-31 00:00:00",
            deferred_long_term_liability: 0.0,
            long_term_debt: 12637000000.0,
            minority_interest: 3917000000.0,
            negative_goodwill: 0.0,
            other_liabilities: 29265000000.0
          }
        },
        {
          company_name: "RANSS",
          current_assets: {
            cash: 615911199999.0,
            date: "2018-12-30 00:00:00",
            inventory: 6549000000.0,
            net_receivable: 9800008880.0,
            other_current_assets: 6666902144.0,
            short_term_investment: 5111120000.0
          },
          current_liabilities: {
            accounts_payable: 6666902144.0,
            date: "2018-12-30 00:00:00",
            other_current_liabilities: 615911199999.0,
            short_debt: 1.0
          },
          equity: {
            capital_surplus: 24082000000.0,
            common_stock: 22322000000.0,
            date: "2018-12-30 00:00:00",
            misc_stocks_options_warrants: 0.0,
            other_stockholder_equity: -5111120000.0,
            preferred_stock: 0.0,
            redeemable_preferred_stock: 0.0,
            retained_earnings: 22322000000.0,
            treasury_stock: -5111120000.0
          },
          long_term_assets: {
            amortization: 0.0,
            date: "2018-12-30 00:00:00",
            deferred_long_term_assets_change: 12637000000.0,
            goodwill: 28976000000.0,
            intangible_assets: 38758000000.0,
            long_term_investment: 7860000000.0,
            other_assets: 28976000000.0,
            property_plant_equipment: 7860000000.0
          },
          long_term_liabilities: {
            date: "2018-12-30 00:00:00",
            deferred_long_term_liability: 0.0,
            long_term_debt: 615911199999.0,
            minority_interest: 3917555000.0,
            negative_goodwill: 0.0,
            other_liabilities: 12637096300.0
          }
        },
        {
          company_name: "Wind",
          current_assets: {
            cash: 15944000000.0,
            date: "2018-12-29 00:00:00",
            inventory: 9816000000.0,
            net_receivable: 6549000000.0,
            other_current_assets: 3392000000.0,
            short_term_investment: 5966000000.0
          },
          current_liabilities: {
            accounts_payable: 22297000000.0,
            date: "2018-12-29 00:00:00",
            other_current_liabilities: 6697000000.0,
            short_debt: 0.0
          },
          equity: {
            capital_surplus: 25563000000.0,
            common_stock: 14000000.0,
            date: "2018-12-29 00:00:00",
            misc_stocks_options_warrants: 0.0,
            other_stockholder_equity: -9039000000.0,
            preferred_stock: 0.0,
            redeemable_preferred_stock: 0.0,
            retained_earnings: 22322000000.0,
            treasury_stock: -9039000000.0
          },
          long_term_assets: {
            amortization: 0.0,
            date: "2018-12-29 00:00:00",
            deferred_long_term_assets_change: 6549000000.0,
            goodwill: 461000000.0,
            intangible_assets: 3718000000.0,
            long_term_investment: 7860000000.0,
            other_assets: 28976000000.0,
            property_plant_equipment: 38758000000.0
          },
          long_term_liabilities: {
            date: "2018-12-29 00:00:00",
            deferred_long_term_liability: 0.0,
            long_term_debt: 12637000000.0,
            minority_interest: 3917000000.0,
            negative_goodwill: 0.0,
            other_liabilities: 29265000000.0
          }
        },
        {
          company_name: "RANSS",
          current_assets: {
            cash: 615911199999.0,
            date: "2018-12-28 00:00:00",
            inventory: 6549000000.0,
            net_receivable: 9800008880.0,
            other_current_assets: 6666902144.0,
            short_term_investment: 5111120000.0
          },
          current_liabilities: {
            accounts_payable: 6666902144.0,
            date: "2018-12-28 00:00:00",
            other_current_liabilities: 615911199999.0,
            short_debt: 1.0
          },
          equity: {
            capital_surplus: 24082000000.0,
            common_stock: 22322000000.0,
            date: "2018-12-28 00:00:00",
            misc_stocks_options_warrants: 0.0,
            other_stockholder_equity: -5111120000.0,
            preferred_stock: 0.0,
            redeemable_preferred_stock: 0.0,
            retained_earnings: 22322000000.0,
            treasury_stock: -5111120000.0
          },
          long_term_assets: {
            amortization: 0.0,
            date: "2018-12-28 00:00:00",
            deferred_long_term_assets_change: 12637000000.0,
            goodwill: 28976000000.0,
            intangible_assets: 38758000000.0,
            long_term_investment: 7860000000.0,
            other_assets: 28976000000.0,
            property_plant_equipment: 7860000000.0
          },
          long_term_liabilities: {
            date: "2018-12-28 00:00:00",
            deferred_long_term_liability: 0.0,
            long_term_debt: 615911199999.0,
            minority_interest: 3917555000.0,
            negative_goodwill: 0.0,
            other_liabilities: 12637096300.0
          }
        },
        {
          company_name: "RANSS",
          current_assets: {
            cash: 615911199999.0,
            date: "2018-12-27 00:00:00",
            inventory: 6549000000.0,
            net_receivable: 9800008880.0,
            other_current_assets: 6666902144.0,
            short_term_investment: 5111120000.0
          },
          current_liabilities: {
            accounts_payable: 6666902144.0,
            date: "2018-12-27 00:00:00",
            other_current_liabilities: 615911199999.0,
            short_debt: 1.0
          },
          equity: {
            capital_surplus: 24082000000.0,
            common_stock: 22322000000.0,
            date: "2018-12-27 00:00:00",
            misc_stocks_options_warrants: 0.0,
            other_stockholder_equity: -5111120000.0,
            preferred_stock: 0.0,
            redeemable_preferred_stock: 0.0,
            retained_earnings: 22322000000.0,
            treasury_stock: -5111120000.0
          },
          long_term_assets: {
            amortization: 0.0,
            date: "2018-12-27 00:00:00",
            deferred_long_term_assets_change: 12637000000.0,
            goodwill: 28976000000.0,
            intangible_assets: 38758000000.0,
            long_term_investment: 7860000000.0,
            other_assets: 28976000000.0,
            property_plant_equipment: 7860000000.0
          },
          long_term_liabilities: {
            date: "2018-12-27 00:00:00",
            deferred_long_term_liability: 0.0,
            long_term_debt: 615911199999.0,
            minority_interest: 3917555000.0,
            negative_goodwill: 0.0,
            other_liabilities: 12637096300.0
          }
        }
      ],
      fields: [{ key: "", label: "Title" }, { key: "", label: "Date" }],
      pageCount: 1,
      totalRows: 1,
      currentPage: 1,
      perPage: 2,
      pageOptions: [2, 4, 8],
      sortBy: null,
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      editMode: false,
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      },
      striped: false,
      bordered: false,
      borderless: false,
      outlined: false,
      small: false,
      hover: false,
      dark: false,
      fixed: false,
      footClone: false
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
      this.items = response.data;
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
    },
    cellAction(item, root, sub) {
      //
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
