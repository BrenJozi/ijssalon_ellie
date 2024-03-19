# huiswerk opgave 10.4 - import functies en variabelen
from helper import *

# huiswerk opgave 10.9 - import
from presentatie import *

# huiswerk opgave 10.11 - import csv
import csv

# huiswerk opgave 10.2 - dictionairy maken
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# huiswerk opgave 10.5 - nieuwe variable toevoegen
totaal_inkomsten = som(inkomsten)

# Presenteer de inkomsten
presenteer(inkomsten, totaal_inkomsten)

# huiswerk opgave 10.12 - code toevoegen
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])