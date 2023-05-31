liczby_pierwsze = []

with open("input.txt") as f:
    for line in f:
        el = int(line)
        if el == 1: continue
        for x in range(2, el):
            if el % x == 0:
                print(f"Znalazłem dzielnik {x} dla {el}")
                break
        else:
            liczby_pierwsze.append(el)

print(liczby_pierwsze)
with open("output.txt", "w") as f:
    for liczba in liczby_pierwsze:
        f.write(f"{liczba}\n")


text = "Ala ma kota"
licznik = {} 

for litera in text:
    if litera in licznik:
        licznik[litera] += 1
    else:
        licznik[litera] = 1

print(licznik)

from collections import Counter
