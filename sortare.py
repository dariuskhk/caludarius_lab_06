def insertion_sort(lista):
    a = lista.copy()
    for i in range(1, len(a)):
        cheie = a[i]
        j = i - 1
        while j >= 0 and a[j] > cheie:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cheie
    return a


def bubble_sort(lista):
    a = lista.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def citire_date(nume_fisier):
    try:
        with open(nume_fisier, "r") as f:
            continut = f.read()
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{nume_fisier}' nu exista!")
        return None, None, None

    linii = continut.splitlines()
    if len(linii) < 2:
        print("Eroare: Fisierul trebuie sa contina cel putin doua linii (numerele si numele algoritmului)!")
        return None, None, None

    linie_numere = linii[0].strip()
    algoritm = linii[1].strip()

    if not linie_numere:
        print("Eroare: Prima linie nu contine numere!")
        return None, None, None

    try:
        numere = [int(x) for x in linie_numere.split()]
    except ValueError:
        print("Eroare: Prima linie trebuie sa contina doar numere intregi separate prin spatii!")
        return None, None, None

    if algoritm not in ("Insertion", "Bubble"):
        print(f"Eroare: Algoritmul '{algoritm}' nu este implementat! Alegeti 'Insertion' sau 'Bubble'.")
        return None, None, None

    return numere, algoritm, continut


def scriere_rezultat(nume_fisier, continut_initial, algoritm, numere_sortate):
    rezultat_text = " ".join(str(x) for x in numere_sortate)
    with open(nume_fisier, "a") as f:
        if continut_initial and not continut_initial.endswith("\n"):
            f.write("\n")
        f.write(f"{algoritm}: {rezultat_text}\n")


if __name__ == "__main__":
    nume_fisier = "date.txt"
    numere, algoritm, continut = citire_date(nume_fisier)

    if numere is not None:
        if algoritm == "Insertion":
            rezultat = insertion_sort(numere)
        elif algoritm == "Bubble":
            rezultat = bubble_sort(numere)

        scriere_rezultat(nume_fisier, continut, algoritm, rezultat)
        print(f"Sortarea cu {algoritm} s-a realizat cu succes! Rezultatul a fost adaugat in {nume_fisier}.")