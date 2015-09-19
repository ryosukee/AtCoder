import itertools

strs = ('a', 'b', 'c')
length = int(input())

for candidate in itertools.product(strs, repeat=length):
    print(''.join(candidate))
