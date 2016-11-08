s = input()
ccount=0
vcount=0
for i in range(len(s)):
    if s[i] in ['A','I','E','O','U']:
        vcount += (len(s) - i)
    else:
        ccount += (len(s) - i)
if ccount > vcount:
    print("Stuart",ccount)    
elif ccount < vcount:
    print("Kevin",vcount)
else:
    print("Draw")