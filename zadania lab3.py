# zad1
A = [1-x for x in range(1,11)]
B = [4**x for x in range(0,8)]
C = [x for x in B if x%2==0]
print(A)
print(B)
print(C)


# zad2
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [x for x in lista1 if x%2==0]
print(lista2)


# zad3
zakupy = {"mleko": "litr", "cukier": "kg", "lizak": "sztuki", "bulki": "sztuki"}
zakupy2 = [key for key in zakupy ]
print(zakupy2)


# zad4
a=5
b=3
c=4
def is_prostokatny(a,b,c):
    if (a>=b and a>=c):
        if b**2 + c**2 == a**2:
            return("JEST prostokatny")
        else:
            return("nie jest prostokatny")
    elif (b>=a and b>=c):
        if a**2 + c**2 == b**2:
            return("JEST prostokatny")
        else:
            return("nie jest prostokatny")
    elif (c>=b and c>=a):
        if b**2 + a**2 == c**2:
            return("JEST prostokatny")
        else:
            return("nie jest prostokatny")
    else:
        print(a)
        print(b)
        print(c)
print(is_prostokatny(a,b,c))


# zad 5
h=5
a=3
def pole_trapesu(a, h):
    return (a*h)/2
print(pole_trapesu(a,h))


# zad6
def iloczyn(a=1, b=4, ile=10):
    ilocz = [a]
    for b
    ilocz.append(a*b)
    return(ilocz)
print(iloczyn())
