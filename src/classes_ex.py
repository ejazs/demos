
class Person:
  total_objects = 1
  def __new__(cls, *args, **kwargs):
    print(cls.total_objects)
    if cls.total_objects >5:
      raise TypeError('Cannot create more objects')
    cls.total_objects+=1
    return super(Person, cls).__new__(cls)

  def __init__(self, fname, lname, age):
    self.__fname = fname
    self._lname = lname
    self._age   = age

  def fullname(self):
    return '{} {}'.format(self.__fname, self._lname)

  @property
  def get_fullname(self):
    return '{} {}'.format(self.__fname, self._lname)

  


max = Person('Max', 'Payne', 35)
a = Person('Max', 'Payne', 35)
z = Person('Max', 'Payne', 35)
x = Person('Max', 'Payne', 35)
x = Person('Max', 'Payne', 35)
c = Person('Max', 'Payne', 35)

# print(max.fullname())
# max.__fname = 'Mama'
# print(max.get_fullname)

# print(dir(maclsx))