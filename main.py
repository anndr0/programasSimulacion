# Autor : Ana María Durán Burgos
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

" FUNCIONES "


def accionMatrizVector(v, mat):
    """Programming Drill 3.1.1"""
    mat0 = [0 for i in range(len(v))]
    for i in range(len(v)):
        res = 0
        for j in range(len(v)):
            res += mat[i][j] * v[j]
        mat0[i] = res
    return mat0


def accionMatrizVectorCplx(v, mat):
    # 11. Función para calcular la "acción" de una matriz sobre un vector.
    mat0 = [0 for i in range(len(v))]
    for i in range(len(v)):
        res = (0, 0)
        for j in range(len(v)):
            c1 = mat[i][j]
            c2 = v[j]
            res = sumaCplx(res, prodCplx(c1, c2))
        mat0[i] = res
    return mat0


def sumaCplx(c1, c2):
    # Suma complejos representados como una tupla
    numReal = c1[0] + c2[0]
    numImg = c1[1] + c2[1]
    res = numReal, numImg
    return res


def prodCplx(c1, c2):
    # Multiplica complejos representados como una tupla
    a1a2 = c1[0] * c2[0]
    b1b2 = c1[1] * c2[1]
    a1b2 = c1[0] * c2[1]
    a2b1 = c2[0] * c1[1]
    multiplication = (a1a2 - b1b2, a1b2 + a2b1)
    return multiplication


def tranpuestaMatriz(mat):
    # 7. Transpuesta de una matriz/vector
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j < i:
                nueva = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = nueva
    return mat


""" EXPERIMENTOS """


def canicasClicks(mat, v, clicks):
    for i in range(clicks):
        newV = accionMatrizVector(mat, v)
    print(newV)


mat = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 1, 0]]

v = [6, 2, 1, 5, 3, 10]
clicks = 2
canicasClicks(v, mat, clicks)


def multiplesRendijas(v, mat, click):
    matTrans = tranpuestaMatriz(mat)
    for i in matTrans:
        if sum(i) != 0:
            return False
    for i in range(click):
        vec = accionMatrizVector(v, mat)
    return vec


mat1 = [[1 / 3, 0, 0], [1 / 3, 0, 1], [1 / 3, 1, 0]]
v1 = [0, 1, 0]
multiplesRendijas(mat1, v1, 1)


def canicasClicksCuan(v, mat, clicks):
    for i in range(clicks):
        newV = accionMatrizVectorCplx(mat, v)
    return newV


def multRenCuant(v, mat, clicks):
    matTrans = tranpuestaMatriz(mat)
    ln = len(matTrans)
    for i in range(ln):
        if sum(matTrans[i]) != 1:
            new = False
    for i in range(clicks):
        newV = accionMatrizVectorCplx(v, mat)
    print(newV)


mat3 = [[(0, 1), (0, 0)],
        [(0, 0), (0, 1)]]
v3 = [(0, 1), (0, 1)]
multRenCuant(v, mat3, 1)

def diagrama(v):
    counts = {}
    vector = []
    if sum(v) == 1:
        for i in range(len(v)):
            x = str(i)
            counts[x] = v[i - 1]
    plot_histogram(counts)
    plt.show()
    return plt