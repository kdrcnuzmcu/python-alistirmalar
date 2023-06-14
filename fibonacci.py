def FibonacciHesapla():
    tane = int(input("Kac tane olsun?:"))
    count = 0
    n = tane
    a = 0
    b = 1
    sayilar = []
    while count < n:
        if count == 0:
            print("{}-".format(count + 1),0)
            sayilar.append(0)
        elif count == 1:
            print("{}-".format(count + 1),1)
            sayilar.append(1)
        elif count > 1:
            print("{}-".format(count + 1), a + b)
            sayilar.append(a + b)
            a, b = b, a
            b = a + b
        count += 1
    # return sayilar

FibonacciHesapla()