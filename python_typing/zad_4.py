def czy_suma_wieksza_od_trzeciej(a, b, c):
    suma = a + b
    if suma > c:
        return True
    else:
        return False

print(czy_suma_wieksza_od_trzeciej(5, 10, 12))
print(czy_suma_wieksza_od_trzeciej(5, 10, 20))