n = '0' + input()

count = 0
for i in range(1, len(n)):
    iketa = 10 ** (i-1)
    leftnum = int(n[:-i])
    rightnum = int(n[-i+1:]) if i != 1 else 0
    centernum = int(n[-i])
    
    if iketa != 1:
        count += leftnum * iketa
    else:
        count += leftnum

    if centernum == 1:
        count += rightnum + 1
    elif centernum > 1:
        count += iketa
print(count)

