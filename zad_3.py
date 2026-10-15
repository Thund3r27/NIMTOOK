def wyswietl_parzyste(lista):
    print("Oto parzyste z podanych liczb:")
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(1, 11))
wyswietl_parzyste(liczby)