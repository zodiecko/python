lista = [1, 1, 2, 3, 5, 8]

def simple_search(n, lista):
    for i in range(len(lista)):
        if n == lista[i]:
            return i

print(binary_search(2, lista))
#não fiz