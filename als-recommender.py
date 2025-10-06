"""
Recommender-System auf Basis von Alternating Least Squares (ALS)

Hierbei wird eine lückenhafte Empfehlungsmatrix R mit den
beobachteten Bewertungen in die Produktform zweier
Faktormatrizen U und V zerlegt, so dass R ≈ U Vᵀ
Die Matrizen U und V werden iterativ durch Lösen
kleinerer linearer Gleichungssysteme aktualisiert.
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import solve

# lückenhaft besetzte Empfehlungsmatrix R mit den
# beobachteten Bewertungen für 3 Nutzende und 3 Bücher
# Zeilen entsprechenden den Büchern, Spalten den Nutzenden
# np.nan repräsentiert fehlende Bewertungen
R = np.array([
    [5, np.nan, 3],
    [4, 2, np.nan],
    [np.nan, 1, 4]
])

num_books, num_users = R.shape
k = 2            # Anzahl der latenten Features (z.B. Genres, andere Eigenschaften)
lambda_reg = 0.1 # Regularisierungsparameter (Vermeidung von Überanpassung)
num_iter = 2     # Anzahl ALS-Iterationen

# Zufällige Initialisierung der Faktormatrizen U und V
np.random.seed(42)
U = np.random.rand(num_books, k)  # Bücher-Faktoren
V = np.random.rand(num_users, k)  # Nutzenden-Faktoren

# Maske der beobachteten Werte (True, wo Wert in R bekannt)
mask = ~np.isnan(R)

# Lösen von LGS für jeden Nutzenden
for iteration in range(num_iter):

    # --- Schritt 1: Nutzer-Vektoren (V) aktualisieren ---
    for i in range(num_users):
        # Indizes der Bücher, die i-ter Nutzer bewertet hat
        idx = mask[:, i]
        if np.any(idx):
            U_i = U[idx, :]               # Bücher, die i-ter Nutzer kennt
            r_i = R[idx, i]               # Bewertungen des i-ten Nutzers
            # Lösung des kleinen LGS: (UᵀU + λI) y_i = Uᵀ r_i
            V[i, :] = solve(U_i.T @ U_i + lambda_reg * np.eye(k),
                            U_i.T @ r_i)

    # --- Schritt 2: Buch-Vektoren (U) aktualisieren ---
    for i in range(num_books):
        # Indizes der Nutzenden, die i-tes Buch bewertet haben
        idx = mask[i, :]
        if np.any(idx):
            V_i = V[idx, :]               # Nutzer, die Buch i bewertet haben
            r_i = R[i, idx]               # Bewertungen zum Buch i
            # Lösung des kleinen LGS: (VᵀV + λI) x_i = Vᵀ r_i
            U[i, :] = solve(V_i.T @ V_i + lambda_reg * np.eye(k),
                            V_i.T @ r_i)

# Vorhersage aller Bewertungen
R_pred = U @ V.T

# Visualisierung
fig, ax = plt.subplots()
cax = ax.matshow(R_pred, cmap='viridis')

# Bekannte Werte markieren
for i in range(num_books):
    for j in range(num_users):
        if not np.isnan(R[i,j]):
            ax.text(j, i, f"{R[i,j]:.1f}", va='center', ha='center', color='white', fontweight='bold')
        else:
            ax.text(j, i, f"{R_pred[i,j]:.1f}", va='center', ha='center', color='red')

ax.set_xticks(range(num_users))
ax.set_yticks(range(num_books))
ax.set_xlabel("Nutzende")
ax.set_ylabel("Bücher")
ax.set_title("Recommender: Bekannte Werte (weiß) und Vorhersagen (rot)")
fig.colorbar(cax, label="Bewertung")
plt.show()