import funkcje
import listy

choice = 0

while choice != 6:
    print("PROGRAM DO OBSLUGI HOTELOWEJ")
    print()
    print("1 - dodaj goscia")
    print("2 - usun goscia")
    print("3 - wyszukaj goscia po nazwisku")
    print("4 - wyszukaj goscia po pokoju")
    print("5 - tworca")
    print("6 - wyjdz")
    print()
    choice = int(input("wybierz: "))
    if (choice == 1):
        funkcje.add_people()
    elif (choice == 2):
        funkcje.delet_people()