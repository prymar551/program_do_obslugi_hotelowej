import listy

def add_people():
    number_of_people_added = int(input("ile osob chcesz dodac?: "))
    for i in range(number_of_people_added):
        name = str(input("podaj imie: "))
        surname = str(input("podaj nazwisko: "))
        room = str(input("podaj numer pokoju: "))
        print()
        listy.People_from_name.update({surname: {"imie": name, "nazwisko": surname, "pokoj": room }})


def delet_people():
    back_or_again = 1
    while back_or_again == 1:
        name_delet = str(input("podaj nazwiso osoby ktorąchcesz usunać: "))
        room_delet = int(input("podaj pokoj ktory zostal zwolniony"))
        listy.People_from_name.pop(name_delet)
        print()
        print("1 - usun kolejna osobe")
        print("2 - wroc")
        back_or_again = int(input("wybor: ")) 
        
    