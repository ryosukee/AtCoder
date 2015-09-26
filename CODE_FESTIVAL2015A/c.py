import bisect

num, dead = input().split()
num = int(num)
dead = int(dead)

count = 0
total_b = 0
differences = []
total_a = 0
for i in range(num):
    # input
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    bisect.insort(differences, a - b)
    total_a += a
    if total_a <= dead:
        count += 1
    else:
        # remove max difference item
        total_a -= differences.pop(-1)
    total_b += b

if total_b >= dead:
    print(-1)
else:
    print(num - count)
