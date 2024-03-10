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

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l2 = [i**2 for i in l1]
# print(l2)
# l3 = [3**y for y in range(1,6)]
# print(l3)
# l4 = [x for x in l1 if x%2==1]
# print(l4)
# l5= [(x,y) for x in l2 for y in l3]
# print(l5)
# l6 = []
# for i in l2:
#     for j in l3:
#         l6.append((i,j))
# print(l6)

# s1= {1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9}
# s2 = {}
# for key, value in s1.items():
#     s2[value]= key
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)

from math import sqrt
#
# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 - (4*a*c)
#     if delta < 0:
#         print('brak pierwiastkow')
#     elif delta==0:
#         print("jeden pierwiastek")
#         x = (-b) / (2*a)
#         return x
#     elif delta > 0:
#         print("dwa pierwiastki")
#         x1 = (-b + sqrt(delta)) / (2*a)
#         x2 = (-b - sqrt(delta)) / (2 * a)
#         return x1, x2
# print(rownanie_kwadratowe(6,3,2))
# print(rownanie_kwadratowe(1,3,2))
# print(rownanie_kwadratowe(1,3,6))

# def dlugosc_odcinka(x1=1,x2=2,y1=1,y2=2):
#     return sqrt((x1-x2)**2 + (y1-y2)**2)
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2,3,2,3))
# print(dlugosc_odcinka(x1=2,x2=3,y1=2,y2=3))

# plik = open('D:\\175180\\WD\\Lab3\\tekst.txt', 'r', encoding='utf-8')
# znak = plik.read(10)
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znak)
# print(linia)
# print(linie)

# plik = open('tekst.txt', 'a+')
# plik.write('aaaaa')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()
# print(znaki)

with open('tekst.txt', 'r') as plik:
    znaki = plik.read(10)
print(znaki)

