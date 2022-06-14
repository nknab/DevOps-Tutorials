class Person:
    def __init__(self, _name) -> None:
        self.name = _name
        self.life_points = 100

    def hit(self, _person) -> None:
        _person.life_points -= 10

    def is_dead(self) -> bool:
        if self.life_points > 0:
            return False
        return True

class Wizard(Person):
    def __init__(self, _name) -> None:
        super().__init__(_name)
        self.life_points = 80

    def hit(self, _person) -> Person:
        _person.life_points -= 15
        return _person


