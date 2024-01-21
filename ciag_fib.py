def ciag_Fibonacciego(n):
    if n <= 0:
        return False
    if n == 1 or n == 2:
        return 1
    else:
        return ciag_Fibonacciego(n - 1) + ciag_Fibonacciego(n - 2)
