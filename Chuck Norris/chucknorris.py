res=""
curChar = ""
count=0
for i in input():
    bin = list("{0:b}".format(ord(i)).zfill(7))
    for i in range(len(bin)):
        b=bin[i]
        if b != curChar:
            res+="0"*count
            if b == "0":res+=" 00 ";curChar = "0"
            else:res+=" 0 ";curChar = "1"
            count = 1
        else:count+=1
    res+="0"*count;count = 0
print(res.strip())