vol1 = float(input("ingrese un valor "))
vol2 = float(input("ingrese un valor "))
vol3 = float(input("ingrese un valor "))

rta = (vol1 + vol2 + vol3)/3

if rta < 115:
    print("voltaje correcto")
elif rta > 115 and rta < 220:
    print("!!ALTO VOLTAJE!!")
elif rta > 220:
    print("!!PELIGRO!!")