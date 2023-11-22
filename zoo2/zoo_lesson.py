from zoo_lesson_animal import *
from zoo_lesson_gehege import *
from zoo_lesson_lists import *

class zoo():
    def __init__(self):
        self.tiere              =   []
        self.tier_idx           =   0
        self.anzahl_der_tiere   =   None
        self.gesamt_gehege      =   self.build_gehege()
# ----------------------------------------------------------------------------------------------------------------------
    def build_gehege(self):
        '''errichtet Groß-, Mittel_ und Kleingehege in "zoo_lesson_gehege"'''
        gesamtgehege = Gehege(kapazitaet=1000)
        gross_tiergehege    = Grosstiergehege(gesamtgehege.capacity, 'links', 140)
        mittel_tiergehege   = Mitteltiergehege(gesamtgehege.capacity, 'geradeaus', 70)
        klein_tiergehege    = Kleintiergehege(gesamtgehege.capacity, 'rechts')
        return gross_tiergehege, mittel_tiergehege, klein_tiergehege
# ----------------------------------------------------------------------------------------------------------------------
    def insert_animal(self):
        '''fügt dem Tier durch eine User-Eingabe Größe, Gewicht und Merkmale ein. Ermittelt den Namen der Gattung,
        die Genauigkeit des Namentreffers und das Entwicklungsstadium und fügt dies in "tier" ein.
        "tier" wird der liste "self.tiere" hinzugefügt'''
        while True:
            if input('Weiteres Tier eintragen? (ja/nein):') == 'nein':
                break
            print (f'Eintrag des {self.tier_idx + 1}ten Tieres')
            tier   =   Animal(
                int(input('Größe des Tieres in cm eingeben:')),
                float(input('Gewicht des Tieres in kg eingeben:')),
                str(input('Ein Merkmal des Tieres eingeben:')))
            tier.add_characteristic()
            tier.set_characteristic_points()
            tier.insert_name()
            tier.set_stadium()

            self.tiere.append(tier)
            self.anzahl_der_tiere = self.tier_idx + 1
            print(self.tiere[self.tier_idx].__dict__)
            self.tier_idx+=1

            self.put_animal_in_gehege(tier, self.gesamt_gehege)

    def put_animal_in_gehege(self, tier, gesamt_gehege):
        '''vergleicht die durchnittliche Größe eines ausgewachsenen Tieres dieser Gattung mit den Größenbedingungen
        der Gehege und sortiert die Tiere in das richtige Gehege ein'''
        if tier.name in average_animal_size_weight:
            if tier >= gesamt_gehege[0]:
                if tier.size <= gesamt_gehege[0].capacity:
                    gesamt_gehege[0].capacity -= tier.size
                    gesamt_gehege[0].animals.append(tier)
                else:
                    print('im Großtiergehege ist nicht mehr genug Platz')
            elif tier >= gesamt_gehege[1]:
                if tier.size <= gesamt_gehege[1].capacity:
                    gesamt_gehege[1].capacity -= tier.size
                    gesamt_gehege[1].animals.append(tier)
                else:
                    print('im Mitteltiergehege ist nicht mehr genug Platz')
            else:
                if tier.size <= gesamt_gehege[2].capacity:
                    gesamt_gehege[2].capacity -= tier.size
                    gesamt_gehege[2].animals.append(tier)
                else:
                    print('im Kleintiergehege ist nicht mehr genug Platz')

        print(gesamt_gehege[0].__dict__)
        print(gesamt_gehege[1].__dict__)
        print(gesamt_gehege[2].__dict__)
# ----------------------------------------------------------------------------------------------------------------------
main_zoo        = zoo()
main_zoo.insert_animal()
print(main_zoo.__dict__)
