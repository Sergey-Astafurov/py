
import math
sp = [int(i) for i in input().split()]

res = math.gcd(*sp)
print(res)