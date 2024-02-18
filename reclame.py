## Huiswerkopgaven 8.12
## Vraag 12

## importeer van ander bestand een functie
from algemene_functies import mijn_functie_2

## Huiswerkopgaven 8.12
## Vraag 5
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

## Argumenten inputs
smaak = "aardbei"
prijs = 4
korting = 0.1

resultaat = aanbieding_1(smaak, prijs, korting)
print(resultaat)

## Huiswerkopgaven 8.12
## Vraag 6
#def inkomsten_totaal(inkomsten):
#    totaal_inkomsten = sum(inkomsten)
#    return totaal_inkomsten

## Argumenten inputs
#dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]

#resultaat = inkomsten_totaal(dagelijkse_inkomsten)
#print(f"Totaal van alle inkomsten: {resultaat} euro.")

## Huiswerkopgaven 8.12
## Vraag 7
def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

# Argumenten inputs
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09

resultaat = inkomsten_totaal(dagelijkse_inkomsten, btw_percentage)
print(resultaat)

## Huiswerkopgaven 8.12
## Vraag 8
def laag_en_hoog(mijn_lijst):
    hoogste_laagste = [max(mijn_lijst), min(mijn_lijst)]
    return hoogste_laagste

## Argumenten inputs
inkommsten = [220, 430, 125, 160, 205, 90, 345]
output = laag_en_hoog(inkommsten)
print(output)

## Huiswerkopgaven 8.12
## Vraag 9
#def gemiddelde(mijn_lijst):
#    totaal_inkomsten = sum(mijn_lijst)
#    aantal_elementen = len(mijn_lijst)
#    
#    gemiddelde_waarde = totaal_inkomsten / aantal_elementen
#    return gemiddelde_waarde

## Argumenten inputs
#inkomsten = [220, 430, 125, 160, 205, 90, 345]
#output = gemiddelde(inkomsten)
#print(output)

## Huiswerkopgaven 8.12
## Vraag 10
def gemiddelde(mijn_lijst):
    totaal_inkomsten = sum(mijn_lijst)

## het is een beetje onduidelijk of het hier over gemiddelde inkomsten gaat of het totaalbedrag van de hele week?
    return f"De gemiddelde inkomsten deze week zijn {totaal_inkomsten} euro."

## Argumenten inputs
inkomsten = [220, 430, 125, 160, 205, 90, 345]
output = gemiddelde(inkomsten)
print(output)

## Huiswerkopgaven 8.12
## Vraag 11
def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)

    return resultaat

## Argumenten inputs
voorbeeld_input = [210,5,3,2,1,2,9]
output = meervoudig(voorbeeld_input)
print(output)


## Huiswerkopgaven 8.12
## Vraag 12

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)

    resultaat_mijn_functie_2 = mijn_functie_2(*korte_lijst)

    return resultaat_mijn_functie_2