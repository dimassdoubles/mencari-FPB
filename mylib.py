def cari_fpb(a, b):
    """a > b"""
    # NOTE algoritma Euclid
    # FPB(a,b)
    # syarat a > b

    should_continue = True
    while should_continue:
        q = 1
        while True:
            if q*b > a:
                q -= 1
                break
            q += 1

        r = a % b
        print(f"{a} = {q}.{b} + {r}")
        if r == 0:
            break
        a = b
        b = r

    return b
