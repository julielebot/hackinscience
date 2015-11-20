a = 0
for i in range(1, 1000):
    if i % 3 == 0:
        a = a + i
for j in range(1, 1000):
    if j % 5 == 0:
        a = a + j
print(a)
