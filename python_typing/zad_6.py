def lacz_usun_duplikaty_i_do_trzeciej_potegi(lista1, lista2):
    polaczone_listy = lista1 + lista2
    bez_duplikatow = list(set(polaczone_listy))
    do_trzeciej_potegi = [x ** 3 for x in bez_duplikatow]
    return do_trzeciej_potegi

print(lacz_usun_duplikaty_i_do_trzeciej_potegi([1, 2, 3], [3, 4, 5]))
print(lacz_usun_duplikaty_i_do_trzeciej_potegi([10, 20], [20, 30, 40]))