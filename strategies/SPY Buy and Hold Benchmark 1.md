# SPY Buy and Hold Benchmark 1

**Strategy ID:** SPY-BEN1 · **Package version:** 1.0.0

**What this is:** a benchmark strategy. It buys the S&P 500 (the SPY ETF) with 100% of a $100,000 portfolio and holds it for the whole period. Use it as the yardstick for every other strategy you build.

**Period:** 2005–2026. **Starting capital:** $100,000. **Holding:** 100% SPY.

## The strategy code — QuantConnect (Python)

Copy everything inside the code box and paste it into a new QuantConnect algorithm.

```python
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
```

## How to run it
1. Go to quantconnect.com and create a new algorithm (choose Python).
2. Delete the template code and paste the code above.
3. Click **Backtest**.
4. When it finishes, download the results. You will analyze them in the next step of the course.

---
*This is the canonical copy of the strategy. The `/qsl-spy-ben1` command writes an identical file into the student's folder; if you change the code here, update the command's SKILL.md to match.*
