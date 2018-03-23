# Part I

class MathDojo (object):
    def __init__(self):
        self.result = 0
    def add (self,*number):
        self.number = number
        for value in number:
            self.result += value
        return self
    def subtract (self,*number):
        self.number = number
        for value in number:
            self.result -= value
        return self

md=MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

# Part III

class MathDojo(object):
   def __init__(self):
       self.result=0        
   def add(self,*number):
       for value in number:
           if isinstance(value,list) or isinstance(value,tuple):
               for list_value in value:
                   self.result+=list_value
           else:
               self.result+=value
       return self
   def substract(self,*number):
       for value in number:
           if isinstance(value,list) or isinstance(value,tuple):
               for list_value in value:
                   self.result-=list_value
           else:
               self.result-=value
       return self
md=MathDojo()
print md.add([1], 3,4,(1,2)).add([3,5,7,8], [2,4.3,1.25]).substract((1,2),2, [2,3], [1.1,2.3]).result