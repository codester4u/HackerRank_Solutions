# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as s
from collections import Counter
def my_mode(sample):
    c = Counter(sample)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

N=int(input())
A=[int(i) for i in input().split()]
print(s.mean(A))
print(s.median(A))
A.sort()
print(my_mode(A)[0])
