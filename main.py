import time


def solve_knapsack(N, A, P, E, G):
    t_s = time.time()
    dp = [[[0 for _ in range(P + 1)] for _ in range(A + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for a in range(A + 1):
            for p in range(P + 1):
                dp[i][a][p] = dp[i - 1][a][p]
                if a >= E[i - 1] and p >= G[i - 1]:
                    dp[i][a][p] = max(dp[i][a][p], dp[i - 1][a - E[i - 1]][p - G[i - 1]] + E[i - 1])

                    # Si la valeur maximale atteinte est égale à la valeur totale,
                    # tous les objets éligibles ont été sélectionnés, on peut arrêter.
                    if dp[i][a][p] == a:
                        break

                # Si la valeur maximale atteinte est égale à la valeur totale,
                # tous les objets éligibles ont été sélectionnés, on peut arrêter.
                if dp[i][A][p] == A:
                    break

            if dp[i][A][P] == A:
                break

    max_value = dp[N][A][P]
    selected_objects = []

    i, a, p = N, A, P
    while i > 0 and a > 0 and p > 0:
        if dp[i][a][p] != dp[i - 1][a][p]:
            selected_objects.append(i)
            a -= E[i - 1]
            p -= G[i - 1]
        i -= 1
    t_e = time.time()
    t_d = t_e - t_s
    return max_value, selected_objects, t_d


# Exemple d'utilisation avec des valeurs aléatoires
N = 8
A = 100000
P = 500
E = [2400, 500, 3000, 1000, 4100, 1200, 2000, 2000]
G = [12, 4, 20, 3, 23, 8, 12, 3]

divisor = 10
A //= divisor
E = [e // divisor for e in E]

max_value, selected_objects, t_d = solve_knapsack(N, A, P, E, G)
print("Valeur maximale :", max_value)
print("Objets sélectionnés :", selected_objects)
print("Cela a duré :", t_d, "secondes")
