def iter(n):
    for i in range(0, n+1):
        if i%4==0 and i%3==0:
            print(i)

n = int(input("n: "))
iter(n)