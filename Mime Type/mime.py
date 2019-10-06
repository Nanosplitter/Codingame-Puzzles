table = dict()
n = int(input())
q = int(input())
for i in range(n):
    e, t = input().split()
    table[(e).lower()] = t
for i in range(q):
    fname = input().lower()
    fnameArr = list(fname)
    fnameArr[fname.rfind(".")] = "---"
    ext = "".join(fnameArr).replace(".", "").replace("---", ".").split('.')[-1]
    if ext in table:print(table[ext])
    else:print("UNKNOWN")