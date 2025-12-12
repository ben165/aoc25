
# This was ChatGPT!

from itertools import product


def gaussian_elimination_gf2(buttons, target):
    """
    buttons: Liste von Knopf-Vektoren, z.B. [[0,1,0,1], ...]
    target:  Ziel-Bitvektor, z.B. [0,1,1,0]

    Rückgabe:
        particular : eine gültige Lösung (falls existiert)
        nullspace  : Liste der Nullraum-Basisvektoren
    """

    # Anzahl der Knöpfe und Lampen
    num_buttons = len(buttons)
    num_lamps = len(target)

    # Matrix A ist Lampen x Knöpfe
    # A[r][c] = buttons[c][r]
    A = [[buttons[c][r] for c in range(num_buttons)] for r in range(num_lamps)]
    b = target[:]

    # Speichere Pivot-Positionen (pro Zeile)
    pivot_col = [-1] * num_lamps

    # --- GAUSS-ELIMINATION ---
    row = 0
    for col in range(num_buttons):
        # Pivot in dieser Spalte finden
        pivot = None
        for r in range(row, num_lamps):
            if A[r][col] == 1:
                pivot = r
                break

        if pivot is None:
            continue  # keine Pivot-Spalte

        # Pivot-Zeile nach oben tauschen (wenn nötig)
        if pivot != row:
            A[row], A[pivot] = A[pivot], A[row]
            b[row], b[pivot] = b[pivot], b[row]

        pivot_col[row] = col

        # Alle anderen Zeilen elimieren
        for r in range(num_lamps):
            if r != row and A[r][col] == 1:
                # Zeile XORen
                for c in range(num_buttons):
                    A[r][c] ^= A[row][c]
                b[r] ^= b[row]

        row += 1
        if row == num_lamps:
            break

    # --- SPEZIELLE LÖSUNG BERECHNEN ---
    # x[c] = 1/0 ob Knopf c gedrückt wird
    x = [0] * num_buttons

    for r in range(num_lamps):
        col = pivot_col[r]
        if col == -1:
            if b[r] == 1:
                # Keine Lösung existiert
                return None, []
            continue
        x[col] = b[r]

    # --- NULLRAUM-BASIS BERECHNEN ---
    free_cols = [c for c in range(num_buttons) if c not in pivot_col]
    nullspace = []

    for free in free_cols:
        vec = [0] * num_buttons
        vec[free] = 1  # freie Variable = 1

        # Rekonstruiere die abhängigen Variablen
        for r in range(num_lamps):
            pc = pivot_col[r]
            if pc != -1 and A[r][free] == 1:
                vec[pc] = 1

        nullspace.append(vec)

    return x, nullspace


def minimal_hamming_solution(particular, nullspace):
    """
    particular: eine gültige Lösung
    nullspace:  Liste der Nullraumvektoren

    Rückgabe:
        beste_loesung
        minimale_anzahl_druecke
    """

    # Wenn es keinen Nullraum gibt, ist die spezielle Lösung bereits optimal
    if not nullspace:
        return particular, sum(particular)

    best = particular[:]
    best_weight = sum(best)

    k = len(nullspace)

    # Alle Kombinationen der Nullraumvektoren durchgehen
    # Für jeden Vektor: 0=weglassen, 1=hinzufügen
    for combo in product([0,1], repeat=k):
        candidate = particular[:]

        # XOR hinzufügen, wenn Combo-Bit = 1
        for i, choose in enumerate(combo):
            if choose == 1:
                candidate = [a ^ b for a, b in zip(candidate, nullspace[i])]

        weight = sum(candidate)
        if weight < best_weight:
            best_weight = weight
            best = candidate[:]

    return best, best_weight
