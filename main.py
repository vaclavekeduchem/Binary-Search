import math

abeceda = ["a", "b", "c", "d", "o", "p", "q", "x", "y", "z"]


def hledej(cil, hodnoty, zacatek=0, konec=0):
    if konec == 0:
        konec = len(hodnoty)

    stred = math.floor((zacatek + konec) / 2)

    if hodnoty[stred] == cil:
        return print(f"Index hledáného cíle je {stred}")

    if hodnoty[stred] > cil:
        return hledej(cil, hodnoty, zacatek, stred-1)

    if hodnoty[stred] < cil:
        return hledej(cil, hodnoty, stred+1, konec)


if __name__ == "__main__":
    hledej("c", abeceda)
