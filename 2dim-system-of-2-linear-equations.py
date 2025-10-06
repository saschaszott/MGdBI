"""
Visualisierung des Lösungsraums von linearen Gleichungssystemen mit 2 Gleichungen und 2 Unbekannten
1. Keine Lösung (zwei parallele Geraden)
2. Genau eine Lösung (Schnittpunkt von zwei Geraden)
3. Unendlich viele Lösungen (identische Geraden)
"""

import matplotlib.pyplot as plt
import numpy as np

# x-Werte
x = np.linspace(-5, 5, 400)

# Fall 1: keine Lösung (parallele Geraden)
y1 = 2*x
y2 = 2*x - 5

# Fall 2: eindeutige Lösung (Schnittpunkt)
y3 = 2*x - 2
y4 = x

# Fall 3: unendlich viele Lösungen (identische Geraden)
y5 = 2*x + 1
y6 = (4*x + 2) / 2  # Vielfaches der ersten Gleichung

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: keine Lösung
axs[0].plot(x, y1, label="2x₁ - x₂ = 0")
axs[0].plot(x, y2, label="2x₁ - x₂ = 5")
axs[0].set_title("Keine Lösung (parallele Geraden)")
axs[0].legend()
axs[0].grid(True)

# Plot 2: eindeutige Lösung
axs[1].plot(x, y3, label="2x₁ - x₂ = 2")
axs[1].plot(x, y4, label="x₁ - x₂ = 0")
axs[1].set_title("genau eine Lösung (Schnittpunkt)")
axs[1].legend()
axs[1].grid(True)

# Plot 3: unendlich viele Lösungen
axs[2].plot(x, y5, label="2x₁ - x₂ = -1")
axs[2].plot(x, y6, linestyle="--", label="4x₁ - 2x₂ = -2")
axs[2].set_title("unendl. viele Lösungen (identische Geraden)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()