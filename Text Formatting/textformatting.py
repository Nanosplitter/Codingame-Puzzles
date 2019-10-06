txt = input()
res = ""
needcap = True
punc = []
for i in txt:
    if not i.isalpha():
        res += "%p%" + i + "%space%"
        punc.append(i)

    if i.isalpha() and needcap:
        res += i.upper()
        needcap = False

    elif i.isalpha():
        res += i.lower()

    if i == ".":
        needcap = True
        
    if i == " ":
        res += "%space%"

res = res.replace("%space%", " ")
for i in range(100):
    res = res.replace(" %p%", "%p%")
    res = res.replace("  ", " ")
res = res.replace("%p%", "")
for i in range(100):
    for p in punc:
        res = res.replace(p + p, p)

print(res.strip())