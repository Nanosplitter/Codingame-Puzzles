n,s=input(),""
while n:s="01T"[n%3]+s;n=-~n/3
print s or 0