a = int(input("Enter number:"))

def check(a):
    if a % 2 ==0:
        return "EVEN"
    else:
        return "ODD"

res = check(a)
print(f"The number {a} is {res}")

