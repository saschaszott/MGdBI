"""
Bildet Paare natürlicher Zahlen (i, j) bijektiv auf eine einzige natürliche Zahl n ab, indem die Paare antidiagonal
(für alle Diagonalelemente gilt i + j = konstant) durchnummeriert werden.

    pi(i, j) = (i + j)(i + j + 1) / 2 + j

Dieses Skript berechnet und druckt das 25x25-Tableau (i, j von 0 bis 24). Es prüft anschließend, dass alle 625 Werte
eindeutig sind und die Umkehrfunktion korrekt zurückrechnet.
"""

from __future__ import annotations
from math import floor

def pairing(i: int, j: int) -> int:
    """Cantorsche Paarungsfunktion: bildet (i, j) bijektiv auf n ab."""
    return (i + j) * (i + j + 1) // 2 + j

def unpairing(n: int) -> tuple[int, int]:
    """Kehrfunktion: aus Eintrag n werden (i, j) = (Spalte, Zeile) rekonstruiert."""
    # k ist die Diagonale (i + j), auf der n liegt.
    # k (k + 1) / 2 = 1/2k^2 + 1/2k = n nach k auflösen: k^2 + k - 2n = 0 <=> k = -1/2 +/- sqrt(1/4 + 2n) = -1/2 + sqrt(1 + 8n)/2
    k = int(floor(((8 * n + 1) ** 0.5 - 1) // 2))
    j = n - k * (k + 1) // 2
    i = k - j
    return i, j

def print_table(size: int = 10) -> None:
    """Druckt das size x size Tableau von pi(i, j), Zeilen = j, Spalten = i."""
    col_width = len(str(pairing(size - 1, size - 1))) + 2
    divider = "  | "  # horizontaler Strich nach der ersten Spalte (den Zeilenlabels)

    header = "j\\i".rjust(5) + divider + "".join(
        str(i).rjust(col_width) for i in range(size)
    )
    print(header)
    print("-" * len(header))

    for j in range(size):
        row = str(j).rjust(5) + divider + "".join(
            str(pairing(i, j)).rjust(col_width) for i in range(size)
        )
        print(row)

def verify(size: int = 10) -> None:
    """Prüft Eindeutigkeit der Werte und Korrektheit der Umkehrfunktion."""
    seen: dict[int, tuple[int, int]] = {}
    for i in range(size):
        for j in range(size):
            n = pairing(i, j)
            if n in seen:
                raise AssertionError(f"Kollision: {seen[n]} und {(i, j)} liefern beide n={n}")
            seen[n] = (i, j)
            if unpairing(n) != (i, j):
                raise AssertionError(f"Umkehrfunktion falsch bei n={n}")

    print(f"\n{size * size} Paare geprüft: alle Werte eindeutig, "
          f"Umkehrfunktion stimmt überein.")

if __name__ == "__main__":
    print("Cantorsche Paarungsfunktion pi(i, j) = (i+j)(i+j+1)/2 + j\n")
    print_table(25)
    verify(25)