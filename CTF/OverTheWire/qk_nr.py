import numpy as np

qk_nr = []
n=1000000
for i in range(1,n+1):
    for k in range(1,n+1):
        res = np.power(i,2) + np.power(k,3)
        if res > n:
            break
        qk_nr.append([i,k])
        
# print(qk_nr[:1000])
print(len(qk_nr))