import math
import matplotlib.pyplot as plt
import numpy as np

def grafs(U, n, m):
    #n_rows = n + 1
    n_rows = 2
    fig, axes = plt.subplots(nrows=n_rows, ncols=1, figsize=(8, 2*(n+1)))

    for i, ax in enumerate(axes):
        x = np.arange(m + 1)
        y = U[i]
        ax.plot(x, y, marker = 'o')

        for xi, yi in zip(x, y):
            ax.text(xi, yi + 0.05, f"{yi:.2f}", fontsize=9, ha='center', va='bottom')

        ax.set_title(f"График {i+1}")

    plt.legend()
    plt.show()

def graf(U, n, m):
    t_index = 16  # номер времени

    fig, ax = plt.subplots(figsize=(8, 5))

    x = np.arange(m + 1)
    y = U[t_index - 1]

    ax.plot(x, y, marker = 'o')
    
    for xi, yi in zip(x, y):
        ax.text(xi, yi + 0.005, f"{yi:.2f}", fontsize=9, ha='center', va='bottom')
    
    ax.set_title(f"График для времени {t_index}")
    ax.set_xlabel("x")
    ax.set_ylabel("U")
    ax.grid(True)

    plt.legend()
    plt.show()

def main():
    X = 1
    T = 1
    a = 1
    m = 5
    n = 80
    N = 15
    U = [[0.0 for _ in range(m + 1)] for _ in range(n + 1)]
    h = X / m
    tau = T / n
    p = (3.0 * N + 1.0) / (N + 2.0)
    for i in range(0, m + 1):
        U[0][i] = p * math.sin(math.pi * h * i)

    for t in range(0, n + 1):
        U[t][0] = 0
        U[t][m] = 0
    
    for j in range (1, n + 1):
        for i in range (1, m):
            U[j][i] = ((tau  * a * a) / (h * h)) * (U[j - 1][i - 1] - 2 * U[j - 1][i] + U[j - 1][i + 1]) + U[j - 1][i]

    for i in range(n + 1):
        print(i, end = ": ")
        for j in range(m + 1):
            print(str(U[i][j]), end = " ")
        print("\n")

    grafs(U, n, m)

    graf(U, n, m)
         

if __name__ == "__main__":
    main()
