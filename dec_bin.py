def dec_to_bin(number):
    if number <= 1:
        return str(number)
    else:
        return dec_to_bin(number // 2) + str(number % 2)
