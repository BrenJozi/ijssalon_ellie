#stap_2
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5,
}

#stap_3
aanbieding = prijzen["aardbei"] * 0.8

#   print(aanbieding)

#stap_4
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}"
#printopodracht stap_4 verwijderd
#print(reclame_tekst)

#stap_5
## "index(".")+3" omdat deze dan 2 cijfers achter de comma zal laten zien in het print statement
reclame_tekst2 = reclame_tekst[:reclame_tekst.index(".")+3]
#printopodracht stap_5 verwijderd
#print(reclame_tekst2)

#stap_6
reclame_tekst3 = reclame_tekst2.upper()
#printopodracht stap_6 verwijderd
#print(reclame_tekst3)

#stap_7
reclame_tekst4 = reclame_tekst3.split()
#printopodracht stap_7 verwijderd
#print(reclame_tekst4)

#stap_8
for el in reclame_tekst4:
#printopodracht stap_8 verwijderd
#    print(el)
    
#stap_9
#printopodracht stap_8 verwijderd
#    print(el.lower())

#stap_10
    if len(el) >= 5:
       print(el.upper())
    else:
        print(el.lower())