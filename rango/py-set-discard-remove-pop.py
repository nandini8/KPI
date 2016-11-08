n = int(input())
s = set(map(int, input().split())) 
N = int(input())
for i in range(N):
    com=input().split()
    if com[0] == "pop":
        command = "s."+ com[0] +"()"
    else:
        command ="s." + com[0] + "(" + com[1] + ")"
    eval(command)
print(sum(s))