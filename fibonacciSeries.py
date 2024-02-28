userInp=int(input("Enter a range:- "))
first = 0
second = 1
print(first)
print(second)
for _ in range(userInp):
    third = first + second
    print(third)
    first,second=second,third
