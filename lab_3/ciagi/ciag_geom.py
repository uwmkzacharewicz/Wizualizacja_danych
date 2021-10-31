def w_iloraz(a2, a1):
    return a2/a1


def n_wyraz(n, a1, q):
    return a1 * q**(n-1)


def suma_n_wyrazow(n, a1, q):
    if q == 1:
        return a1 * n
    else:
        return a1 * (1 - q ** n) / (1 - q)


def wyswietl_ciag(a1, q, ile):
    for x in range(1, ile+1):
        print("a{} = {}" .format(x, n_wyraz(x, a1, q)))
