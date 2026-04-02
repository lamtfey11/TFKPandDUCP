import math
import matplotlib.pyplot as plt
import numpy as np

def grafs(U, n, m):
    n_rows = 2
    fig, axes = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 8))

    # если график один, превращаем axes в список
    if n_rows == 1:
        axes = [axes]

    for i, ax in enumerate(axes):
        x = np.arange(m + 1)
        y = U[i]

        ax.plot(x, y, marker='o')

        for xi, yi in zip(x, y):
            ax.text(xi, yi + 0.03, f"{yi:.2f}", fontsize=8, ha='center')

        ax.set_title(f"График {i + 1}")
        ax.set_xlabel("x")
        ax.set_ylabel("U")
        ax.grid(True)

    plt.tight_layout(pad=2.0)
    plt.savefig("graphs2.png", dpi=150)
    plt.close()

def graf(U, n, m):
    t_index = 2 # номер времени

    fig, ax = plt.subplots(figsize=(10, 5))  # шире и удобнее

    x = np.arange(m + 1)
    y = U[t_index - 1]

    ax.plot(x, y, marker='o', linestyle='-', color='b')

    for xi, yi in zip(x, y):
        ax.text(xi, yi + 0.02, f"{yi:.2f}", fontsize=9, ha='center')

    ax.set_title(f"График для времени {t_index}")
    ax.set_xlabel("x")
    ax.set_ylabel("U")
    ax.grid(True)

    plt.tight_layout()
    plt.savefig("graf2.png", dpi=150)
    plt.close()

def main():
    X = 1
    T = 1
    a = 1
    m = 5
    n = 10
    N = 15
    U = [[0.0 for _ in range(m + 1)] for _ in range(n + 1)]
    h = X / m
    tau = T / n
    p = (3.0 * N + 1.0) / (N + 2.0)
    for i in range(0, m + 1):
        U[0][i] = p * math.pow(i * h, 2)

    for t in range(0, n + 1):
        U[t][0] = 0
        U[t][m] = p
    
    for j in range (1, n + 1):
        for i in range (1, m):
            U[j][i] = ((tau  * a * a) / (h * h)) * (U[j - 1][i - 1] - 2 * U[j - 1][i] + U[j - 1][i + 1]) + U[j - 1][i]

    for i in range(n + 1):
        print(f"{i:3}: ", end="")  # индекс времени с выравниванием
        for j in range(m + 1):
            print(f"{U[i][j]:8.4f}", end=" | ")  # 8 символов, 4 после запятой
        print()  # новая строка после каждого времени

    grafs(U, n, m)

    graf(U, n, m)

if __name__ == "__main__":
    main()
