a = int(input("Chislo: "))
a_1 = a % 2 == 0
a_2 = a % 3 == 0
if a_1 or a_2:  # TODO Заменить многоточие необходиммым условием
    print("'Число number кратно 2 или 3'")
