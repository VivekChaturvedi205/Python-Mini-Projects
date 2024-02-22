#0      *
#1     ***
#2    *****
#3   *******
#4  *********

# Ans
# k=1
# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end="")
#         j+=1
#     b=1
#     while b<=k:
#         print("*",end="")
#         b+=1
#     k+=2
#     i+=1
#     print()

l=[3,5,9,10,11]
target=14
for index,value in enumerate(l):
    for j  in range(index+1,len(l)):
        if l[index]+l[j]==target:
            print(index, j)
            break    