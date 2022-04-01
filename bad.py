abeceda = ["a", "b", "c", "d", "o", "p", "q", "x", "y", "z"]


# Linear Seach Algorithm
def hledej(cil):
    for i, pismeno in enumerate(abeceda):
        if pismeno == cil:
            return print(f"Index hledáného cíle je {i}")


hledej("y")
