class Call(object):
    def __init__(self,id,name,phone_number,time,reason):
        self.id = id
        self.name = name
        self. phone_number = phone_number
        self.time = time
        self.reason = reason
    def display(self):
        print "Unique ID:", self.id
        print "Caller Name:", self.name
        print "Caller Phone Number:", self.phone_number
        print "Time of Call:", self.time
        print "Reason for Call:", self.reason
        return self

class CallCenter(object):
    def __init__ (self):
        self.calls = []
        self.queue_size = 0
    def add (self,call):
        self.calls.append(call)
        self.calls.sort(key=lambda calls: calls.time)
        self.queue_size +=1
        return self
    def remove (self):
        self.calls.pop(0)
        self.queue_size -=1
        return self
    def info (self):
        for i in self.calls:
            print "Caller Name: {}, Phone Number: {}, Time in Queue: {}, Calls in queue: {}".format(i.name,i.phone_number,i.time,self.queue_size)
    def findRemove (self,number):
        counter=0
        for value in self.calls:
            if value.phone_number == number:
                self.calls.pop(counter)
                self.queue_size -=1
            counter+=1
        return self
    def sort (self):
        self.calls.sort(key=lambda calls: calls.time)
        return self

CallCenter1 = CallCenter()
call1 = Call (1234, "John","555-555-5555","5.05","Annoyed")
call2 = Call (1235, "Jane", "444-444-4444", "5.01", "Payments")
call3 = Call (1236,"Javier","777-777-7777","5.02","Complaint")
CallCenter1.add(call1).add(call2).add(call3).info()