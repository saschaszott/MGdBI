import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np

# Definitionsbereich
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Fall 1: keine Lösung (3 parallele Ebenen)
Z1 = (0 + 2*X - 4*Y)/4
Z2 = (4 + 2*X - 4*Y)/4
Z3 = (8 + 2*X - 4*Y)/4

# Fall 2: eindeutige Lösung
Z4 = 2 * np.ones_like(X)
Z5 = X
Z6 = Y

# Fall 3: unendlich viele Lösungen (Schnitt entlang einer Geraden)
Z7 = (1 + X - Y)/2
Z8 = (4 + 4*X - 4*Y)/8  # Vielfaches von Z4
Z9 = (1 - 2*X - Y)

# Schnittgerade parametrisieren: X = t
t_vals = np.linspace(-2.5, 2.5, 100)
x_vals = t_vals
y_vals = 1 - 5*t_vals
z_vals = 3*t_vals

fig = plt.figure(figsize=(20, 5))
elev, azim = 15, 45  # Perspektive

# Plot 1: keine Lösung
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z1, alpha=0.3, color="red")
ax1.plot_surface(X, Y, Z2, alpha=0.3, color="green")
ax1.plot_surface(X, Y, Z3, alpha=0.3, color="blue")
ax1.view_init(elev=elev, azim=azim)
ax1.set_title("Keine Lösung (parallele Ebenen)")

# Plot 2: eindeutige Lösung
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z4, alpha=0.3, color="red")
ax2.plot_surface(X, Y, Z5, alpha=0.3, color="green")
ax2.plot_surface(X, Y, Z6, alpha=0.3, color="blue")
ax2.view_init(elev=elev, azim=azim)
ax2.set_title("genau eine Lösung (Schnittpunkt)")

# Schnittlinien von je zwei Ebenen plotten
red = np.array(to_rgb("red"))
green = np.array(to_rgb("green"))
blue = np.array(to_rgb("blue"))

t = np.linspace(-5, 5, 50)

x1 = 2 * np.ones_like(t)
y1 = t
z1 = 2 * np.ones_like(t)
ax2.plot(x1, y1, z1, '--', linewidth=1.5, color=(green + blue)/2)

x2 = t
y2 = 2 * np.ones_like(t)
z2 = 2 * np.ones_like(t)
ax2.plot(x2, y2, z2, '--', linewidth=1.5, color=(red + blue)/2)

x3 = t
y3 = t
z3 = t
ax2.plot(x3, y3, z3, '--', linewidth=1.5, color=(red + green)/2)

ax2.view_init(elev=elev, azim=azim)
ax2.set_title("genau eine Lösung (Schnittpunkt)")

# Plot 3: unendlich viele Lösungen
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z7, alpha=0.3, color="red")
ax3.plot_surface(X, Y, Z8, alpha=0.3, color="green")
ax3.plot_surface(X, Y, Z9, alpha=0.3, color="blue")

# Schnittgerade plotten
ax3.plot(x_vals, y_vals, z_vals, color="red", linewidth=1.5)

ax3.view_init(elev=elev, azim=azim)
ax3.set_title("unendl. viele Lösungen (Geradenschnitt)")

plt.tight_layout()
plt.show()