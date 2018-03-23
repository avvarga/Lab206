class product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self,tax):
        return self.price*tax
    def returned(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in the box, like new":
            self.status = "For Sale"
        elif reason == "open box":
            self.status = "used"
            self.price = self.price*0.8
        return self
    def display (self):
        print (self.price,self.item_name,self.weight,self.brand,self.status)
        return self

product1=product(200,"Jacket",5,'Harley')
product1.returned('open box').display()