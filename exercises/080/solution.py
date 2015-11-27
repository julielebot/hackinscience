alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if len(i) == 1:
        for j in alphabet:
            if len(j) == 1:
                if i < j:
                    print(i+j)
