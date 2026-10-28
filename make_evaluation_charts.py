"""Recreate a simple comparison chart from illustrative model metrics."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
metrics = pd.read_csv(ROOT / "data" / "illustrative_model_metrics.csv")
x = np.arange(len(metrics))
width = 0.34

fig, ax = plt.subplots(figsize=(8, 4.8))
ax.bar(x - width / 2, metrics["MAE_t_ha"], width, label="MAE (tonnes/ha)")
ax.bar(x + width / 2, metrics["RMSE_t_ha"], width, label="RMSE (tonnes/ha)")
ax.set_xticks(x)
ax.set_xticklabels(["Mean baseline", "Linear regression", "Random forest", "Gradient boosting"])
ax.set_ylabel("Error (tonnes per hectare)")
ax.set_title("Illustrative Test-Set Error by Model")
ax.legend()
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
output = ROOT / "figures" / "illustrative_error_comparison.png"
fig.savefig(output, dpi=160)
print(f"Saved {output}")
print("Reminder: example metrics are hypothetical, not real model results.")
