def generator(n):
    for i in range(n+1, 0, -1):
        print(i)

n = int(input("n: "))
generator(n)