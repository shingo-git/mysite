input = 10000
lt_PM = []

for i in range(1,input + 1):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum = sum + j
        if j == i - 1:
            if sum == i:
                lt_PM.append(i)

print(lt_PM)
