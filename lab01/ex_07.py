print("########################")

sep = " : "
P= "Python"
G= "Guido van Rossum"
C= "C++"
B= "Bjarne Stroustrup"
J="Java"
J2="Jame Gosling"
P2="Pascal"
N="Niklaus Wirth"
print(P + sep + G)
print(P+sep+G)
print(J ,J2, sep=sep)
print(f"{P2} : {N}")
print("#########################")

print("#"*25)
print(f"{P:>6} {sep} {G}")
print(f"{C:>6} {sep} {B}")
print(f"{J:>6} {sep} {J2}")
print(f"{P2:6} {sep} {N}")