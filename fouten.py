# importeer math module_vraag 2
import math

# maak functie_vraag 3
def discriminant(a, b, c):
    
    #discriminant formule
    discriminant_formule = b**2 - 4*a*c
  
    #Defineer functie_vraag 4
    D1 = (-b + math.sqrt(discriminant_formule))/(2 * a)
    D2 = (-b - math.sqrt(discriminant_formule))/(2 * a)
    
    ##Defineer functie_vraag 5
    uitvoer = [D1 , D2]
    return uitvoer

# Print code_vraag 6
print(f"Voor de formule ax^2 + bx + c, geef a, b en c: , b, c")

#Input waardes_vraag 7 en edit voor vraag 10
try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
except ValueError:
    print("Er is een fout in a, b of c")
    exit

# Defineer uitkomst_vraag 8
uitkomst = discriminant(a, b, c)

# vraag 9
D1 = uitkomst[0]
D2 = uitkomst[1]

# Print string_Vraag 10
print(f"Voor de formule {a}x^2 + {b}x + {c}, zijn D1 en D2: {D1} en {D2}")



