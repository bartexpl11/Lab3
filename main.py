# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Wrong value")
# except Exception:
#     print("Error na wszytskie bledy")
# else:
#     print(result)

l1 = [1,2,3,4,5,6,7,8,9]
l2 = []
for i in l1:
    l2.append(i**2)
print(l2)
l2 = [i**2 for i in l1]
print(l2)
l3 = [3**y for y in range(1,6)]
print(l3)
l4 = [x for x in l1 if x%2==1]
print(l4)
l5= [(x,y) for x in l2 for y in l3]
print(l5)
l6 = []
for i in l2:
    for j in l3:
        l6.append((i,j))
print(l6)
