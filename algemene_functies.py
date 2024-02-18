## Huiswerkopgaven 8.12
## Vraag 2
def mijn_functie_1(a, b, c, d):
    test_a = a * a
    test_b = b * b
    test_c = c * c
    test_d = d * c
    return test_a, test_b, test_c, test_d

## Argumenten inputs
output = mijn_functie_1(2, 4, 10, 12)
print(output)

## Vraag 3
def mijn_functie_2(arg1, arg2):
    test_1 = arg1 + arg2
    test_2 = arg1 - arg2
    test_3 = arg1 * arg2
    test_4 = arg1 / arg2

    return [test_1, test_2, test_3, int(test_4)]

## Argumenten inputs
argumenten = [(12, 3), (12, 2), (10, 5), (100, 20)]

for arg1, arg2 in argumenten:
    output = mijn_functie_2(arg1, arg2)
    print(output)