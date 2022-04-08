# Enter your code here. Read input from STDIN. Print output to STDOUT
phone_book={}
n=int(input())
for i in range(n):
    x,y=input().split()
    phone_book[x]=y
while True:
    try:
        z=input()
        if z in phone_book.keys():
            print(z+"="+phone_book[z])
        else:
            print("Not found")
    except EOFError:
        break        
