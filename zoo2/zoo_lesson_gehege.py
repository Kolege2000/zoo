class Gehege:
    def __init__(self, kapazitaet):
        self.capacity   =   kapazitaet

class Grosstiergehege(Gehege):
    def __init__(self, kapazitaet, name, standort, bedingung_mindestgroesse):
        super().__init__(kapazitaet=kapazitaet//2)
        self.name       =   f'{name}gehege'
        self.position   =   standort
        self.condition  =   bedingung_mindestgroesse
        self.animals    =   []

class Mitteltiergehege(Gehege):
    def __init__(self, kapazitaet, name, standort, bedingung_mindestgroesse):
        super().__init__(kapazitaet=kapazitaet//4)
        self.name       =   f'{name}Gehege'
        self.position   =   standort
        self.condition  =   bedingung_mindestgroesse
        self.animals    =   []

class Kleintiergehege(Gehege):
    def __init__(self, kapazitaet, name, standort, bedingung_mindestgroesse):
        super().__init__(kapazitaet=kapazitaet//4)
        self.name       =   f'{name}Gehege'
        self.position   =   standort
        self.condition  =   bedingung_mindestgroesse
        self.animals    =   []