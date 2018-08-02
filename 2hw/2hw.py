a, b = 2.5, 3.5
c = a + complex(0, b)
d = b + (a * 1j)
e = str(a)+"+"+str(b)+"j"
f = complex(e) ** d
print(f-c-a)
