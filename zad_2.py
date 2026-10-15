def piecliczbfor(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

def piecliczbskladana(lista):
    return [liczba * 2 for liczba in lista]