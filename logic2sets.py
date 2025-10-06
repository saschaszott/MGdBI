"""
Veranschaulichung der Verbindung zwischen Aussagenlogik und Mengenlehre.
Übersetzung einer aussagenlogischen Formel in eine mengentheoretische Formel.
"""

from itertools import product

# Grundmenge (Universum)
X = {1, 2, 3, 4, 5}

# Teilmengen von X als Aussagen
A = {1, 2}
B = {2, 3, 5}

# Logische Interpretation: True/False
def logical_formula(A_val, B_val):
    # (A ∧ B) ∨ (¬A)
    return (A_val and B_val) or (not A_val)

# Mengeninterpretation
def set_formula(A_set, B_set, X):
    # (A ∩ B) ∪ (X \ A)
    return (A_set & B_set) | (X - A_set)

print("Wahrheitstabelle für Aussage (A ∧ B) ∨ (¬A)")
print("| A | B | Ergebnis |")
print("|---|---|----------|")
for a, b in product([False, True], repeat=2):
    print("|", int(a), "|", int(b), "|", int(logical_formula(a, b)), "       |")

# === Mengenoperation ===
result_set = set_formula(A, B, X)
print("\nGrundmenge X =", X)
print("A =", A)
print("B =", B)
print("(A ∩ B) ∪ (X \\ A) =", result_set)