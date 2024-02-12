# Write a function that accepts string from user and print all permutations of that string.

def to_string(list):
    return ''.join(list)


def permute(a, l, r):
    if l == r:
        print(to_string(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(str, l+1, r)
            a[i], a[l] = a[l], a[i]


str = input()
r = len(str)    
a = list(str)


permute(a, 0, r)
