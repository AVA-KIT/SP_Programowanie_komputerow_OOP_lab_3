class Ksztalt:
        def __init__(self, nazwa):
            self.nazwa = nazwa

class ZmianaKsztaltu:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
    def zwieksz(self):
        self.rozmiar += 1
    def podaj_pole(self):
        raise Exception

class Kwadrat(Ksztalt, ZmianaKsztaltu):
    def __init__(self, nazwa, rozmiar):
        Ksztalt.__init__(self, nazwa)
        ZmianaKsztaltu.__init__(self, rozmiar)
    
    def podaj_pole(self):
        return self.rozmiar **2

class Kolo(Ksztalt, ZmianaKsztaltu):
    def __init__(self, nazwa, rozmiar):
        Ksztalt.__init__(self, nazwa)
        ZmianaKsztaltu.__init__(self, rozmiar)
    def podaj_pole(self):
        return 3.14 * self.rozmiar **2


def main():
    kw1 = Kwadrat("kwadrat_1", 4)
    print(kw1.__dict__)
    kw1.zwieksz()
    print(kw1.__dict__)
    print(f'Pole ', kw1.nazwa, 'wynosi: ', kw1.podaj_pole())
    kol1 = Kolo("koło_1", 4)
    print(kol1.__dict__)
    kol1.zwieksz()
    print(kol1.__dict__)
    print(f'Pole ', kol1.nazwa, 'wynosi: ', kol1.podaj_pole())

if __name__ == '__main__':
    main()