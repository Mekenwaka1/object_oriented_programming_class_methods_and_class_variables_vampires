class Vampire:

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

    def drink_blood(self):
        self.drank_blood_today = True 

    @classmethod
    def sunrise(cls):
        for curr_vampire in cls.coven:
            if ((curr_vampire.in_coffin == False) or (curr_vampire.drank_blood_today == False)):
                cls.coven.remove(curr_vampire)

    @classmethod     
    def sunset(cls):
        for curr_vampire in cls.coven:
            curr_vampire.drank_blood_today = False
            curr_vampire.in_coffin = False        

    def go_home(self):
        self.in_coffin = True
