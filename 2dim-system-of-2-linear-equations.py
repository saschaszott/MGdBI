import matplotlib.pyplot as plt
import numpy as np

# x-Werte
x = np.linspace(-5, 5, 400)

# Fall 1: keine Lösung (parallele Geraden)
y1 = 2*x + 1
y2 = 2*x - 2

# Fall 2: eindeutige Lösung (Schnittpunkt)
y3 = 2*x + 1
y4 = -0.5*x + 2

# Fall 3: unendlich viele Lösungen (identische Geraden)
y5 = 2*x + 1
y6 = 2*x + 1  # stimmt mit y5 überein

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: keine Lösung
axs[0].plot(x, y1, label="y = 2x+1")
axs[0].plot(x, y2, label="y = 2x-2")
axs[0].set_title("Keine Lösung (parallele Geraden)")
axs[0].legend()
axs[0].grid(True)

# Plot 2: eindeutige Lösung
axs[1].plot(x, y3, label="y = 2x+1")
axs[1].plot(x, y4, label="y = -0.5x+2")
axs[1].set_title("genau eine Lösung (Schnittpunkt)")
axs[1].legend()
axs[1].grid(True)

# Plot 3: unendlich viele Lösungen
axs[2].plot(x, y5, label="y = 2x+1")
axs[2].plot(x, y6, linestyle="--", label="y = 2x+1 (identisch)")
axs[2].set_title("unendl. viele Lösungen (identische Geraden)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()