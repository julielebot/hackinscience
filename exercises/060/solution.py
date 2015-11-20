alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',[\]
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for lettre1 in alphabet:
    if len(lettre1) == 1:
        for lettre2 in alphabet:
            if len(lettre2) == 1:
                print(lettre1 + lettre2)
