# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    S=input()
    eve,odd='',''
    for i in range(len(S)):
        if i%2==0:
            eve+=S[i]
        else: odd+=S[i]
    print(eve,odd)
