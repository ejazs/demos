class EmptyClass:
  def name(self):
    return 'mama'

e = EmptyClass()
print(e.name())
# # class MyClass:

# #   def __init__(self, val):
# #     self._a = self.__set_a(val)

  
# #   def __get_a(self):
# #     return self._a

# #   def __set_a(self, val):
# #     # print('val',val>1)
# #     if val>1:
# #       self._a = val
# #     else:
# #       self._a= 'ejaz'
# #     #return self._a

# #   a = property(__get_a, __set_a)

# # z = MyClass(val=0)
# # # print(z.a)



# class Person:

#   def __init__(self, val):
#     self._val = self.set_val=val

#   @property
#   def get_val(self):
#     return str(self._val)

#   @get_val.setter
#   def set_val(self, val):
#     print('her')
#     self._val= val if len(val)>10 else 'Mama'
#     #return self._val

# ejaz = Person('Ejaz')
# print(ejaz.get_val)
# # ejaz.set_val='mamamamamm'
# # print(ejaz.get_val)


