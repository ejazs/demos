a= [10,15,3,99,5]
b= [10,15,13,89,5]
diff = 0
for x,y in zip(a,b):
  diff+= abs(x-y)
print(diff)
print(diff/len(a))
def a():
  pass




# text = '''
# This is my text and fere i am writing it
# '''

# find = 'fere'
# replace = 'here'

# for x in text:
#   if x == find:
#     print('Found')
#     x = replace

# print(text)

# # txt = text.split(' ')
# # for x in txt:
# #   if x == find:
# #     x = replace

# # for x in range(len(txt)):
# #   if txt[x]==find:
# #     print('Found')
# #     txt[x]=replace

# # text = ' '.join(txt)
# # print(text)

# # # Fire, Police, Sanitation | range(1,7) | F+P+S == 12 | P even

# # police = []
# # fire   = []
# # sanitization = []

# # for x in range(1,7):
# #   for y in range(1,7):
# #     for z in range(1,7):
# #       if x+y+z == 12 and x!=y and x!=z and y!=z:
# #         if x%2 == 0:
# #           police.append(x)
# #         elif y%2 ==0:
# #           police.append(y)
# #         ek









# # # for x in range(1,10):
# # #   for y in range(1,10):
# # #     for z in range(1,10):
# # #       print(x,y,z)

# # # from itertools import permutations



# # # # '''
# # # # Write a function that prints the least integer that is not present in a given list and cannot be 
# # # # represented by the summation of the sub-elements of the list.

# # # # E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4,
# # # #  and if a = [1,2,2,5,7] then the least non-representable integer is 18.

# # # # Hide answer

# # # # '''
# # # # # import copy
# # # # # def less(a):
# # # # #   new = copy.deepcopy(a)
# # # # #   for x in a:
# # # # #     for y in a:
# # # # #       if new[x]!=new[y]:
# # # # #         new.append(x+y)
# # # # #   new = sorted(new)
# # # # #   print(new)
# # # # #   for x in range(1,max(new)):
# # # # #     if x not in new:
# # # # #       return x
  
# # # # import copy 
# # # # def less(l):
# # # #   new = copy.deepcopy(l)
# # # #   for x in range(len(l)):
# # # #     for y in range(len(l)):
# # # #       print(l[x]+l[y])
# # # #       if x==y :
# # # #         continue
# # # #       new.append(l[x]+l[y])
# # # #   new = sorted(new)

# # # #   for x in range(1,max(new)):
# # # #     if x not in new:
# # # #       return x
# # # #   #return new  

# # # # a = [1,2,2,5,7]

# # # # print('less(a)', less(a))