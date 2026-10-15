def wyswietlcodrugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(10, 20))
wyswietlcodrugi(liczby)