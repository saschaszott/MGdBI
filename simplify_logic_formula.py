from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, simplify_logic
from sympy.logic.boolalg import truth_table

A, B, C = symbols('A B C')

# Aussage 1: (¬A ∧ ¬B ∧ ¬C) ∨ (¬A ∧ ¬B ∧ C) ∨ (A ∧ B ∧ ¬C)
expr = Or(And(Not(A), Not(B), Not(C)), And(Not(A), Not(B), C), And(A, B, Not(C)))
# Aussage 2: (A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ B ∨ C)
#expr = And(Or(A, Not(B), Not(C)), Or(Not(A), B, C))

# Aussagen vereinfachen
simplified = simplify_logic(expr, form='dnf') # 'dnf' für disjunktive NF, 'cnf' für konjunktive NF
print("Originalaussage:", expr)
print("Vereinfachte Aussage:", simplified)
print(f"WW-Tafel für Originalaussage {expr}:")
for row in truth_table(expr, [A, B, C]):
    print(row)
print("\n")
print(f"WW-Tafel für vereinfachte Aussage {simplified}:")
for row in truth_table(simplified, [A, B, C]):
    print(row)