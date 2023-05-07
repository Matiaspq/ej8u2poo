from claseConjunto import Conjunto
if __name__== '__main__':
    conjunto1=[]
    conjunto2=[]
    uno=int(input("Ingrese elemento para el conjunto 1, finalice con 0: "))
    while uno!=0:
        conjunto1.append(uno)
        uno=int(input("Ingrese elemento para el conjunto 1, finalice con 0: "))
    A=Conjunto(conjunto1)

    dos=int(input("Ingrese elemento para el conjunto 2, finalice con 0: "))
    while dos!=0:
        conjunto2.append(dos)
        dos=int(input("Ingrese elemento para el conjunto 2, finalice con 0: "))
    B=Conjunto(conjunto2)

    print(A,B)
    union=A+B
    print(f"La union de los 2 conjuntos es: {union}")

    diferencia=A-B
    print(f"La diferencia de los 2 conjuntos es: {diferencia}")
    if A==B:
        print("Son iguales")
    else: print("Son distintos")