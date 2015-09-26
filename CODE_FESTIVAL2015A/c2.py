num, dead = input().split()
num = int(num)
dead = int(dead)

count = 0
total_b = 0
l = list()
append = l.append
total_a = 0
for i in range(num):
    # input
    a, b = input().split()
    a = int(a)
    b = int(b)
    append(a - b)
    
    total_a += a
    total_b += b

if total_b > dead:
    print(-1)
else:
    count = 0
    l.sort()
    l.reverse()
    for dif in l:
        if total_a <= dead:
            break
        total_a -= dif
        count += 1
    print(count)
