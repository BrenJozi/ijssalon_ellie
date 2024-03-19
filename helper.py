def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,persoonen):
    bedrag_pp = bedrag/persoonen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

# huiswerk opgave 10.3 - som toegevoegd
def som(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total
    