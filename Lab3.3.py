class Komentarze:
    komentarze = {}

class Urzytkownik(Komentarze):
    liczba_komentarzy = 0
    def __init__(self, nazwa, komentarz):
        self.nazwa = nazwa
        self.komentarz = komentarz
    def dodaj_komentarz(self):
        if Urzytkownik.liczba_komentarzy < 1:
            self.komentarze[self.nazwa] = self.komentarz
            Urzytkownik.liczba_komentarzy += 1
        else:
           return print(f'{self.nazwa} możesz wystawić tylko jeden komentarz!')

class Administrator(Urzytkownik):
    def edytuj_komentarz(self):
            self.komentarze[self.nazwa] = self.komentarz
            print(f'Komentarz zmieniony przez administratora dla użytkownika {self.nazwa}')

marian = Urzytkownik('Marian', 'Nie lubię tego!')
marian.dodaj_komentarz()
print(marian.komentarze)
marian = Urzytkownik('Marian', 'Lubię to!')
marian.dodaj_komentarz()
marcin = Administrator('Marian', 'Lubię to!')
marcin.edytuj_komentarz()
print(marian.komentarze)