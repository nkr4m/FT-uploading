#multiple array input

def mul_func(li):
    mul = 1
    for ele in li:
        mul = mul * ele
    return mul

print("Enter the number of arrays you want to create")
n = int(input())
count = 1
for i in range(n):
    print("Enter the size of array number:", count)
    m = int(input())
    print("Enter the elements of the array number:", count)
    li = [int(x) for x in input().split()]
    ans = mul_func(li)
    print(ans)
    count = count + 1

