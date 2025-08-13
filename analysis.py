"""
analysis.py
Performs simple analysis on quarterly MRR growth and generates a plot.
Author/Contact: 23f3002689@ds.study.iitm.ac.in
"""

from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import numpy as np

getcontext().prec = 6

# Quarterly MRR growth data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [7.31, 3.39, 6.88, 9.06]
industry_target = 15.0

# Compute average precisely
vals = [Decimal(str(x)) for x in mrr_growth]
avg = sum(vals) / Decimal(len(vals))

print("Quarterly MRR growth values:", mrr_growth)
print("Computed average MRR growth:", float(avg))

# Plot the trend vs. industry benchmark
x = np.arange(len(quarters))
plt.figure(figsize=(8,5))
plt.plot(x, mrr_growth, marker='o', label="MRR Growth (%)")
plt.hlines(industry_target, xmin=0, xmax=len(quarters)-1, linestyles='--', colors='red', label="Industry Target (15%)")
plt.xticks(x, quarters)
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.title("MRR Growth by Quarter (2024) vs Industry Target")
plt.grid(True)
plt.legend()
plt.savefig("mrr_trend_vs_benchmark.png", bbox_inches='tight')
print("Saved plot to mrr_trend_vs_benchmark.png")
