"""
Erzeugung und Ausgabe des Pascalschen Dreiecks.
Im Pascalschen Dreieck entspricht der Eintrag in der n-ten Zeile und k-ten Spalte
dem Binomialkoeffizienten "n über k" (nCk).
"""

def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

n = 20
triangle = pascals_triangle(n)
max_width = len(' '.join(map(str, triangle[-1])))
for row in triangle:
    row_str = ' '.join(map(str, row))
    print(row_str.center(max_width))