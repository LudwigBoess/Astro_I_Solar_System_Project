import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table('solar_system.txt', delimiter='\t', header=None)


n = np.zeros(len(df.loc[:,0]))
n = [np.linalg.norm(df.loc[i,1:3]) for i in range(0, len(df.loc[:,0]))]

np.var(n)

fig, ax = plt.subplots(figsize=(8,8))


for i in range(0,10):
    ax.plot(df.loc[:,1+(6*i)], df.loc[:,2+(6*i)])

ax.set_xlabel("x [AU]")
ax.set_ylabel("y [AU]")

ax.set_xlim([-50.0, 50.0])
ax.set_ylim([-50.0, 50.0])
ax.set_aspect("equal")
plt.show()

fig.savefig("test.pdf")

plt.close(fig)
