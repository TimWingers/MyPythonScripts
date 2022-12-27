#Сортировка списка вставками
def insert_sort(A):
  N = len(A)
  for top in range(1, N):
    k = top
    while k > 0 and A[k-1] > A[k]:
      A[k], A[k-1] = A[k-1], A[k]
      k -= 1

#Сортировка списка выбором
def choise_sort(A):
  N = len(A)
  for pos in range(0, N-1):
    for k in range(pos+1, N):
      if A[k] < A[pos]:
        A[k], A[pos] = A[pos], A[k]

#Сортировка списка методом пузырька
def bubble_sort(A):
  N = len(A)
  for bypass in range(1, N):
    for k in range(0, N-bypass):
      if A[k] > A[k+1]:
        A[k], A[k+1] = A[k+1], A[k]


#Тестирование функции
def test_sort(insert_sort):
  print("testcase #1: ", end="")
  A = [4, 2, 5, 1, 3]
  A_sorted = [1, 2, 3, 4, 5]
  sort_algorithm(A)
  print("Ok" if A == A_sorted else "Fail")