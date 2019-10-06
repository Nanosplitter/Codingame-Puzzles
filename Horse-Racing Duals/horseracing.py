import sys
import math
import itertools

st = []
diff = 100000000
tempDif =100000000 
n = int(input())
for i in range(n):
    st.append(int(input()))
st.sort()

for i in range(len(st)):
    if(i != 0):
        tempDif = st[i] - st[i-1]
        if(tempDif<diff ):
            diff = tempDif
print(diff)