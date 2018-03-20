class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles +=10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -=5
        if self.miles>0:
            return self
        else:
            print "Cannot go backwards!"



bike1=Bike(200,25)
bike1.ride().ride().ride().reverse().displayinfo()

bike2=Bike(400,50)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3=Bike(100,15)
bike3.reverse().reverse().reverse().displayinfo()