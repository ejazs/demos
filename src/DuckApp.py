class QuackAbility:
  def quack(self):
    return NotImplementedError

class Quack(QuackAbility):
  def quack(self):
    return 'Quack'

class Queek(QuackAbility):
  def quack(self):
    return 'Queek'

class Duck:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  @property
  def get_name(self):
    return self.name

  def get_color(self):
    return self.color

  def __str__(self):
    return self.name


class MallardDuck(Duck):
  def __init__(self, name, color, type):
    self.type = type
    super().__init__(name, color)

a = MallardDuck('a', 'blue', 'fly')
print(a.get_color())