class Gehege:
    def __init__(self, kapazitaet):
        self.capacity   =   kapazitaet

class Grosstiergehege(Gehege):
    def __init__(self, kapazitaet, standort, bedingung_mindestgroesse):
        super().__init__(kapazitaet=kapazitaet//2)
        self.position   =   standort
        self.condition  =   bedingung_mindestgroesse
        self.animals    =   []

class Mitteltiergehege(Gehege):
    def __init__(self, kapazitaet, standort, bedingung_mindestgroesse):
        super().__init__(kapazitaet=kapazitaet//4)
        self.position   =   standort
        self.condition  =   bedingung_mindestgroesse
        self.animals    =   []

class Kleintiergehege(Gehege):
    def __init__(self, kapazitaet, standort):
        super().__init__(kapazitaet=kapazitaet//4)
        self.position   =   standort
        self.condition  =   None
        self.animals    =   []