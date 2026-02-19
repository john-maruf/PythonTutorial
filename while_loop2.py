def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}")


n = input("Enter a number: ")
n = int(n)

while n != 0:
    multiplication_table(n)
    print("Done")
    n = input("Enter a number: ")
    n = int(n)
