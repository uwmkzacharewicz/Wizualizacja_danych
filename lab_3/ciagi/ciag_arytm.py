def w_roznica(a2, a1):
    return a2-a1


def n_wyraz(n, a1, r):
    return a1+(n-1)*r


def suma_n_wyrazow(n, a1, r):
    return (2*a1+(n-1)*r)/2*n


def wyswietl_ciag(a1, r, ile):
    for x in range(1, ile+1):
        print("a{} = {}" .format(x, n_wyraz(x, a1, r)))
