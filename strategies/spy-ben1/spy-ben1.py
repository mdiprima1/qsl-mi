# QSL Strategy Package SPY-BEN1 - SPY Buy and Hold Benchmark 1
# Package version 1.2.0 - QS Lab MI Research Package
# Canonical source: this file is copied to students byte-for-byte. Do not edit locally.

from AlgorithmImports import *


class SPYBuyAndHoldBenchmark1(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2005, 1, 1)
        self.SetEndDate(2026, 1, 1)
        self.SetCash(100000)
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.SetBenchmark("SPY")

    def OnData(self, data):
        # Buy once, then hold for the whole period.
        if not self.Portfolio.Invested and data.ContainsKey(self.spy):
            self.SetHoldings(self.spy, 1.0)
