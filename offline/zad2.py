"""
Dany jest ciąg przedziałów domkniętych L = [[a1, b1], . . . ,[an, bn]]. Początki i końce przedziałów są liczbami naturalnymi. 
Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w całości zawierają się w c (nie licząc samego c). 
Proszę zaproponować i zaimplementować algorytm, który zwraca maksimum z poziomów przedziałów znajdujących się w L. 
Proszę uzasadnić poprawność algorytmu i oszacować jego złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję postaci:
def depth( L ):
...
która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
"""

def partition(A, p, r, indx):
    A[r], A[(p + r) // 2] = A[(p + r) // 2], A[r] 
    x = A[r][indx]
    i = p - 1
    for j in range(p, r):
        if A[j][indx] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r, indx):
    while p < r:
        q = partition(A, p, r, indx)
        if (q - p) > (r - q):
            quicksort(A, q + 1, r, indx)
            r = q - 1
        else:
            quicksort(A, p, q - 1, indx)
            p = q + 1


def depth(T):
    for i in range(len(T)):
        T[i] = [T[i][0], T[i][1], -1, -1]

    quicksort(T, 0, len(T) - 1, 0)
    T[0][2] = 0
    for i in range(0, len(T)):
        if T[i - 1][0] == T[i][0]:
            T[i][2] = T[i - 1][2]
        else:
            T[i][2] = i

    quicksort(T, 0, len(T) - 1, 1)
    T[len(T) - 1][3] = len(T) - 1
    for i in range(len(T) - 2, -1, -1):
        if T[i + 1][1] == T[i][1]:
            T[i][3] = T[i + 1][3]
        else:
            T[i][3] = i

    max_diff = -1
    for i in range(len(T)):
        if T[i][3] - T[i][2] > max_diff:
            max_diff = T[i][3] - T[i][2]

    return max_diff