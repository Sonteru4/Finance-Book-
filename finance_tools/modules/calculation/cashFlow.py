from scipy.optimize import fsolve


class CashFlowCalculator:
    def __init__(self, val, t, interset_rate):
        self.val = val
        self.t = t
        self.interset_rate = interset_rate
        self.PV = self.valAt(0)

    def valAt(self, time):
        return self.val * (1 + self.interset_rate) ** (time - self.t)

    def tryR(self, r):
        return self.val * (1 + r) ** (0 - self.t)


def wacc(price, outstanding, debtValue, debtYield, stockReturn, taxRate):
    equity = price * outstanding
    total = equity + debtValue

    return (equity / total) * stockReturn + (debtValue / total) * debtYield * (1 - taxRate)


def npv_for_give_rate(r, array_of_cash_flows):
    return sum([x.tryR(r) for x in array_of_cash_flows])


def find_irr(arr):
    return fsolve(npv_for_give_rate, 0, (arr))


def npv(array_of_cash_flows):
    return sum([x.PV for x in array_of_cash_flows])
