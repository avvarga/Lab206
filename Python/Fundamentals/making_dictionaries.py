name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
  new_dict = {}
  new_dict = zip(list1,list2)
  new_dict = dict(new_dict) 
  return new_dict
print(make_dict(name,favorite_animal))