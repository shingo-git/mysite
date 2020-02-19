input = 1500

def sum_div(n):
    for i in range(1,n + 1):
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                sum = sum + j
    return sum

lt1 = []
lt2 = []

for i in range(1,input+1):
    j = sum_div(i)          #jを関数に入れるとｴﾗｰ、仕方ないのでﾘｽﾄ化
    lt1.append(i)
    lt2.append(j)

for i in range(len(lt1)):
    for j in range(i,len(lt1)):
        if lt1[i] == lt2[j]:
            if lt1[j] == lt2[i]:
                if not lt1[j] == lt2[j]:
                    print(lt1[j],lt2[j])
