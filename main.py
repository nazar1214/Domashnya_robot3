import random
def guess_the_number():
    men = 0
    mat = 1000
    randmoit = random.randint(men, mat)
    popitka = 0
    print("вам треба вгадти число від 1000 до 0")

    while True:
            chos = int(input("Ваша спроба: "))
            popitka += 1
            if chos < randmoit:
                print("Ви вибрали число яке менше яке випало")
            elif chos > randmoit:
                print("Ви вибрали число яке більше яке випало")
            else:
                print(f"Ви вгадали число яке випало: {randmoit}, за: {popitka} попиток")
                break

