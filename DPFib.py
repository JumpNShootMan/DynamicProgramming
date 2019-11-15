def FibonacciDPUtil(n, tab):
    if n < 2:
        tab[0] = 0
        tab[1] = 1
    else:
        FibonacciDPUtil(n - 1, tab)
        tab[n] = tab[n - 1] + tab[n - 2]
            
def FibonacciDP(n):
    tab = [0] * (n + 1)
    FibonacciDPUtil(n, tab)
    return tab[n]