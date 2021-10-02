import math
'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(x):
    '''
    determina daca un nr este prim
    :paramx:un nr intreg
    :return:
    True,daca x este prim sau False in caz contrar
    '''
    if x < 2:
        # print("NU")
        return False
    else:
        ok = True
        for i in range(2, x // 2 + 1):
            '''
      range(5)  0,1,2,3,4
      range(2,5)  2,3,4
      range(2,5,2)  2,4
      '''
            if x % i == 0:
                ok = False
            if ok:
                # print("DA")
                return True
            else:
                # print("NU")
                return False
    assert is_prime(-1) is False
    assert is_prime(0) is False


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    product = 1
    for element in lst:
        product *= element
    return product


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    if is_prime(x) or is_prime(y):
        return 1
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    lst = [x, y]
    product = get_product(lst)
    factori_primi = {}
    cmmdc = 1
    for factor in range (2, int(math.sqrt(product)) + 1):
        while product % factor == 0:
            if factor not in factori_primi:
                factori_primi[factor] = 0
            factori_primi[factor] += 1
            product //= factor
    if product != 1:
        factori_primi[product] += 1
    for key, value in factori_primi.items():
        cmmdc = cmmdc * math.pow(key, value//2)
    return cmmdc


def main():
    # interfata de tip consola aici
    # x = input('Dati un numar x = ')
    # x = int(x)
    # print(is_prime(x))

    # lst = list()
    # length = input('Dati dimeansiunea listei len(lst) = ')
    # for number in range(0, int(length)):
    #     lst.append(int(input('Dati valoarea pentru a o adauga in lista:')))
    # produs = get_product(lst)
    # print('Produsul este: ', produs)

    # x = int(input('Dati primul numar x = '))
    # y = int(input('Dati al doilea numar y = '))
    # print('CMMDC al celor doua numere este ', get_cmmdc_v1(x, y))

    x = int(input('Dati primul numar x = '))
    y = int(input('Dati al doilea numar y = '))
    print('CMMDC al celor doua numere este ', get_cmmdc_v2(x, y))


if __name__ == '__main__':
    main()
