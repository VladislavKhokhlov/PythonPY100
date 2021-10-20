def alive_10():
    months = 1
    step = int(input("Степуха:"))
    rashod = int(input("Расходы:"))
    rashod_10 = rashod
    while months < 10:
        rashod = rashod + (rashod * 0.03)
        rashod_10 += rashod
        months += 1
        # print(rashod)
        # print(rashod_10)

    return (rashod_10 - (step * 10))

if __name__ == "__main__":
    x = alive_10()
    print(round(x))