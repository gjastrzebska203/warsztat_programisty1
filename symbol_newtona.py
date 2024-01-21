def symbol_newtona(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return symbol_newtona(n - 1, k - 1) + symbol_newtona(n - 1, k)
