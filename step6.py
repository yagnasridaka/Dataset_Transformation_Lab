import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
df = pd.read_csv("day02_usage.csv")

Days = df["Day"].to_numpy()
Apps = ["Chat","Video","Study","Games"]
usage = df[Apps].to_numpy()
per_day = usage.sum(axis=1)
shares = usage/per_day[:,None]*100

fig,(ax1,ax2) = plt.subplots(2,1,figsize=(11,8))

for i,app in enumerate(Apps):
    ax1.plot(Days,usage[:,i],marker="o",markersize=3,linewidth=1.6,label=app)

ax1.set_title("Daily Minutes per App - 30 Days")
ax1.set_xlabel("Day")
ax1.set_ylabel("Minutes")
ax1.legend(ncol=4,frameon=False)
peak_day = int(per_day.argmax())
ax1.annotate(f"Busiest Day: {Days[peak_day]}",xy=(Days[peak_day],usage[peak_day].max()),xytext=(Days[peak_day]+3,usage[peak_day].max()+3),arrowprops=dict(arrowstyle="->"))
ax1.grid(alpha=0.3)

bottom = np.zeros(len(Days))
for i,app in enumerate(Apps):
    ax2.bar(Days,shares[:,i],bottom=bottom,label=app)
    bottom += shares[:,i]

ax2.set_title("Per Day Share")
ax2.set_xlabel("Day")
ax2.set_ylabel("% Share")
ax2.set_ylim(0,115)
ax2.legend(ncol=4,frameon=False,loc="upper right")

fig.tight_layout()
fig.savefig("day02_usage_chart.png")

print("Saved usage chart")
print("Sanity Check: ",shares.sum(axis=1))