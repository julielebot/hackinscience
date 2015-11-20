alphabet = "abcdefghijklmnopqrstuvwxyz"
for lettre1 in alphabet:
    if len(lettre1) == 1:
        for lettre2 in alphabet:
            if len(lettre2) == 1:
                if lettre1 != lettre2:
                    print(lettre1 + lettre2)
