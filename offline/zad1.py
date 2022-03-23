"""
Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
  def __init__(self):
    self.val = None # przechowywana liczba rzeczywista
    self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (lista nie ma wartownika). 
Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej o najwyżej k. 
Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest 1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n 
może zawierać liczby w dowolnej kolejności. Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę.
"""


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def insert_1(A, x):
    A.append(x)
    i = len(A) - 1
    while i > 0 and x.val < A[parent(i)].val:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def insert_2(A, x):
    A[len(A) - 1] = x
    i = len(A) - 1
    while i > 0 and x.val < A[parent(i)].val:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l].val < A[min_ind].val:
        min_ind = l
    if r < n and A[r].val < A[min_ind].val:
        min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify(A, n, min_ind)


def SortH(p, k):
    n=0
    q=p
    while q is not None:
        n+=1
        q=q.next
    if k>=n:
        k=n-1

    H = []
    for i in range(k + 1):
        curr = p
        p = p.next
        curr.next = None
        insert_1(H, curr)

    sorted_list = Node()
    l = sorted_list
    while p is not None:
        H[0], H[k] = H[k], H[0]
        l.next = H[k]
        l = l.next
        heapify(H, len(H) - 1, 0)
        curr = p
        p = p.next
        curr.next = None
        insert_2(H, curr)
        heapify(H, len(H), 0)

    for i in range(k, -1, -1):
        H[0], H[i] = H[i], H[0]
        heapify(H, i, 0)
        l.next = H[i]
        l = l.next

    return sorted_list.next