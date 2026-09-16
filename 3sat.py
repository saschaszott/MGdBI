"""
Entscheidungsproblem 3-SAT: Gegeben ist eine aussagenlogische Formel in konjunktiver Normalform (KNF), die aus Klauseln
mit jeweils genau drei Literalen besteht. Es ist zu entscheiden, ob die Formel erfüllbar ist, also ob es eine Belegung
der Variablen (Elementaraussagen) mit Wahrheitswerten gibt, die die Formel erfüllt (d.h. Wahrheitswert der Formel unter
dieser WW-Belegung ist wahr).
"""
from itertools import product

def satisfies(formula, assignment):
    """
    Prüft, ob die übergebene Belegung die übergebene KNF-Formel erfüllt.

    Ein Literal wird hierbei wie folgt codiert: x_i wird durch i repräsentiert, ¬x_i durch -i.

    Eine Klausel ist eine Liste von Literalen. Die KNF-Formel ist eine Liste von Klauseln.
    """

    # durchlaufe die Klauseln der KNF-Formel
    for clause in formula:
        # Eine Klausel (Disjunktion) ist genau dann wahr, wenn mindestens eines ihrer Literale wahr ist.
        clause_is_true = False

        # durchlaufe die Literale der Klausel
        for literal in clause:
            variable = abs(literal) # Betrag der Zahl, um Variable zu erhalten
            value = assignment[variable]

            if literal > 0 and value:
                clause_is_true = True

            if literal < 0 and not value:
                clause_is_true = True

        # Ist eine Klausel falsch, ist die ganze KNF-Formel (da Konjunktion von Klauseln) falsch.
        if not clause_is_true:
            return False

    return True

def three_sat(formula, number_of_variables):
    """
    Prüft durch vollständiges Ausprobieren aller 2^number_of_variables Belegungen, ob die KNF-Formel erfüllbar ist.

    Gibt im Falle der Erfüllbarkeit eine erfüllende Belegung zurück oder None, falls keine existiert.
    """

    # Alle 2^number_of_variables möglichen Belegungen erzeugen
    for values in product([False, True], repeat=number_of_variables):

        # WW-Belegung erzeugen
        assignment = {
            variable: values[variable - 1]
            for variable in range(1, number_of_variables + 1)
        }

        if satisfies(formula, assignment):
            return assignment

    return None

def formula_to_string(formula):
    """
    Gibt die übergebene KNF-Formel in ausdruckbarer Form zurück.
    """

    formula_string = ""

    for clause in formula:
        clause_string = "(" + " ∨ ".join([f"x{abs(literal)}" if literal > 0 else f"¬x{abs(literal)}" for literal in clause]) + ")"
        formula_string += clause_string + " ∧ "

    return formula_string[:-3]  # Entferne das letzte " ∧ "

# KNF-Formel (für 3-SAT) codieren
# Beispiel: (x1 ∨ x2 ∨ x3) ∧ (x1 ∨ x3 ∨ x5) ∧ (¬x3 ∨ ¬x4 ∨ x5)
formula = [
    [1, 2, 3],
    [1, 3, 5],
    [-3, -4, 5]
]

# Anzahl der Aussagevariablen in der Formel (x1, x2, x3, x4, x5)
number_of_variables = 5

solution = three_sat(formula, number_of_variables)

if solution is None:
    print(f"Die KNF-Formel {formula_to_string(formula)} ist NICHT erfüllbar.")

else:
    print(f"Die KNF-Formel {formula_to_string(formula)} ist ERFÜLLBAR.\nEine mögliche WW-Belegung der Elementaraussagen ist:")

    for variable in range(1, number_of_variables + 1):
        print(f"x{variable} = {solution[variable]}")
