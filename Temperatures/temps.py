p=print
input()
s=input()
if(len(s)==0):p(0);quit()
s=list(map(int,s.split()))
r=min(s,key=abs)
if(abs(r)in s):p(abs(r));quit()
p(r)