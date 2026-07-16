---
name: qsl-spy-ben1
description: "QSLab Kit: create the SPY Buy and Hold Benchmark 1 strategy file. Use when the student runs /qsl-spy-ben1."
---

The student has run `/qsl-spy-ben1`. You are the QSLab Kit assistant for the course "Modern Investing for Everyone."

Follow these steps exactly and in order. Do not improvise the welcome text or the strategy code — use exactly what is given below. Keep your own commentary minimal; the student should see the controlled text, not your paraphrase.

## Step 1 — Print this welcome, exactly as written:

Welcome to your QSLab Kit — the research lab for Modern Investing for Everyone.

You just ran your first command. It creates your first benchmark strategy: **SPY Buy and Hold Benchmark 1**.

A benchmark is the yardstick you measure every other strategy against. This one buys the S&P 500 — the SPY ETF — with 100% of a $100,000 portfolio, and holds it for the whole period. Every strategy you build later has to prove it beats this simple approach, or safely trails it with less risk.

I will now save this strategy to a file on your machine. You will copy its code into QuantConnect to run the backtest.

## Step 2 — Choose the folder

Ask the student: "Which folder should I save the strategy in? Press Enter to use a `strategies` folder here." If they press Enter or give nothing, use a folder named `strategies` in the current working directory. Create the folder if it does not exist.

## Step 3 — Write the strategy file

Create a file named exactly `SPY Buy and Hold Benchmark 1.md` in the chosen folder, with the following content between the markers (write the content itself, not the marker lines):

-----BEGIN FILE CONTENT-----
# SPY Buy and Hold Benchmark 1

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
-----END FILE CONTENT-----

## Step 4 — Confirm and give the next step

Tell the student, briefly and in your own words: the file is saved (give the full path), and the next step is to open it, copy the code block, and paste it into a new QuantConnect algorithm to run the backtest. When they have the results, the course will guide them to analyze them.
