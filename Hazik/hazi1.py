import math 

# 1. feladat, megadjuk az oldalakat
a = 5
b = 6
c = 7

# kerület 
kerulet = a + b + c
print("A háromszög kerület:", kerulet)

# félkerület 
s = kerulet / 2

# terület Heron-képlettel
terulet = math.sqrt(s* (s - a) * (s-b) * (s-c))
print("A háromszög területe:", terulet)



a = 6  # szabályos háromszög oldala

magassag = (math.sqrt(3)/2) * a
print("A szabályos háromszög magassága:", magassag)



a = 4  # kocka éle

lapatlo = math.sqrt(a**2 + a**2)
testatlo = math.sqrt(a**2 + a**2 + a**2)

print("A kocka lapátlója:", lapatlo)
print("A kocka testátlója:", testatlo)