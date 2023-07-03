a = input("Enter any word")

def check(a):
    reversed_a = a[::-1]
    if a == reversed_a:
        return True
    else:
        return False
    

res = check(a)

if res == 1:
    print("pal")
else:
    print("no")