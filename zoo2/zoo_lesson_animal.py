from zoo_lesson_lists import *

class Animal:
    def __init__(self,groesse,gewicht,merkmal):
        self.size               =   groesse
        self.weight             =   gewicht
        self.characteristics    =   [merkmal]
        self.criteria_points    =   []
        self.name               =   None
        self.stadium            =   None
# ----------------------------------------------------------------------------------------------------------------------
    def add_characteristic(self):
        ''' Einfügen von Merkmalen in self.characteristics'''
        next_query = True
        while next_query:
            input_characteristic    =   input('Weiteres Merkmal eintragen oder abbrechen("exit"):')
            if input_characteristic != 'exit':
                self.characteristics.append(input_characteristic)
            else:
                next_query = False
# ----------------------------------------------------------------------------------------------------------------------
    def set_characteristic_points(self):
        ''' Global aufgerufen; erhält übereinstimmende Merkmalpunkte von count_characteristic_points für jedes Tier
             und setzt Diese in eine Liste'''
        for criteria_list in criteria_list_list:
            points =    self.count_characteristc_points(criteria_list)
            self.criteria_points.append(points)

    def count_characteristc_points(self,criteria_list):
        ''' Aufgerufen durch set-characteristic-points; zählt Übereinstimmungen der eingetragenen Merkmalen mit den
        Kriterienlisten und gibt diese zurück'''
        criteria_points =   0
        for criteria in criteria_list:
            if any(criteria in value.lower() for value in self.characteristics):
                criteria_points += 1
        return criteria_points
# ----------------------------------------------------------------------------------------------------------------------
    def insert_name(self):
        '''Global aufgerufen; erhält die Wahrscheinlichkeit und den Namen des Tieres durch set_animal und fragt,
            ob der Name eingetragen werden soll'''
        proof_animal = self.set_animal()
        if input(f'das Tier ist {proof_animal[0]} ein/eine {proof_animal[1]}, soll der Name eingetragen werden? (ja/nein)') == 'ja':
            self.name   =   proof_animal[1]

    def set_animal(self):
        ''' Durch insert_name aufgerufen; erhält die Wahrscheinlichkeit des Tieres mit den meisten Merkmalübereinstimmungen
             von set_probability und gibt Wahrscheinlichkeit und Name des Tieres zurück'''
        max_index   =   self.criteria_points.index(max(self.criteria_points))
        return self.set_probability(max_index), animal_list[max_index]

    def set_probability(self, max_index):
        ''' Durch set_animal aufgerufen und gibt die Wahrscheinlichkeit zurück'''
        probability    =   probability_list[self.criteria_points[max_index]]
        return probability
# ----------------------------------------------------------------------------------------------------------------------
    def set_stadium(self):
        '''Global aufgerufen; vergleicht die Größe mit dem, eines durchschnittlichen Erwachsenen
        und gibt das Entwicklungsstadium zurück'''
        if self.name in average_animal_size_weight:
            average_size, average_weight = average_animal_size_weight[self.name]
            if self.size <= 1 / 4 * average_size or self.weight <= 1 / 15 * average_weight:
                self.stadium = 'Baby'
            elif self.size <= 2 / 3 * average_size or self.weight <= 2 / 3 * average_weight:
                self.stadium = 'jugendlich'
            else:
                self.stadium = 'erwachsen'
        else:
            self.stadium = 'unbekannt'
# ----------------------------------------------------------------------------------------------------------------------
    def __ge__(self, other):
        average_size = average_animal_size_weight[self.name]
        return average_size[0] >= other.condition

    def __repr__(self):
        return self.name + ' ' + self.stadium
