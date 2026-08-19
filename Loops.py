i = 1
while i <= 15:
    print("Running")
    i += 1
    if i == 10:
        continue
    print("Hy")
print("Done")

for i in range(5):
    print(i, end=" ")

for i in range(0, 10, 3):
    print(i)

string = "Python"
for i in string:
    print(i)

for row in range(3):
    for col in range(3):
        print("*", end="")
    print() # for next line

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
    print(n*i)
