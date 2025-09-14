from sympy import symbols
from sympy.logic.boolalg import Or, And, Not
from sympy.logic.boolalg import truth_table

A, B, C = symbols('A B C')

# Aussage 1: (¬A ∧ ¬B ∧ ¬C) ∨ (¬A ∧ ¬B ∧ C) ∨ (A ∧ B ∧ ¬C)
expr1 = Or(And(Not(A), Not(B), Not(C)), And(Not(A), Not(B), C), And(A, B, Not(C)))
# Aussage 2: (A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ B ∨ C)
expr2 = And(Or(A, Not(B), Not(C)), Or(Not(A), B, C))

# Wahrheitswerttabellen erzeugen
print(f"WW-Tafel für Aussage {expr1}:")
for row in truth_table(expr1, [A, B, C]):
    print(row)
print("\n")
print(f"WW-Tafel für Aussage {expr2}:")
for row in truth_table(expr2, [A, B, C]):
    print(row)