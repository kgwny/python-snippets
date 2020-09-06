# Standクラス
class Stand(object):
    def __init__(self, name):
       self.name = name

# SuperStnadクラス
class SuperStand(Stand):
    def __init__(self, name, function):
        super(SuperStand, self).__init__(name)
        self.function = function

# EvolutionStandクラス
class EvolutionStand(SuperStand):
    def __init__(self, name, function, skill):
        super(EvolutionStand,self).__init__(name, function)
        self.skill = skill

    def trigger(self):
        self.skill = self.function * self.skill

stand1 = Stand('ハーミットパープル')
print(stand1.name)

stand2 = SuperStand('承太郎', 'スタープラチナ')
print(stand2.name, stand2.function)

stand3 = SuperStand('ディオ', 'ワールド')
print(stand3.name, stand3.function)

stand3 = EvolutionStand('スタープラチナ・ザ・ワールド', 'ド', 5)
stand3.trigger()
print(stand3.name, stand3.skill)
