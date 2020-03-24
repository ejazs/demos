'''
Python sorting : List, Tuples, Dictionary and Objects

'''

# simple list sorting

l = [3,1,6,7,2,5]

#Using sort method
l.sort() #This sorts list inplace, returns None

#Using sorted function
new = sorted(l) #This returns new list with sorted values

# Reverse using reverse = True parameter
l.sort(reverse=True)

new = sorted(l, reverse=True)

print(new)

# Sorted can also be used with tuples but it returns a List object instead of Tuple

#Sorting dictionary 
#It sorts dict based on keys

my = {
  'name' : 'John',
  'age'  : 25,
  'salary' : 25000
}

my = sorted(my)

# Sorting based on abs values
l = [-3,-2,-1,1,2,3]

#Extra parameter key runs list from function which is passed before performing sort, in our case it run 'abs'
l = sorted(l, key=abs)

#Sorting Class objects


class Emp():
  _total = 1
  def __new__(cls, *args, **kwargs):
    # print(cls, 'yay')
    if cls._total >=5 :
      raise NameError('Housefull baba')
    cls._total+=1
    return super(Emp, cls).__new__(cls)
  
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def __repr__(self):
    return str(self.name)


ejaz = Emp('Ejaz', 27, 25000)
test = Emp('Test', 21, 5000)
mac = Emp('Mac', 31, 27000)
munna = Emp('Munna', 20, 3000)
emps = [ejaz, test, mac, munna,]
new = sorted(emps, key=lambda emp : emp.salary)
print(new)


  
    

