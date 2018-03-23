class Patient (object):
    id=0
    def __init__ (self,name,allergies):
        patient.id +=1
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        return self
    
class Hospital (object):
    bed_number = 0
    def __init__ (self,hospital_name,capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
    def admit (self,patient):
        if len(self.patients)>=self.capacity:
            print "We cannot accept more patients, we are full!"
        else:
            self.patients.append(patient)
            print self.patients
            Hospital.bed_number += 1
            patient.bed_number = Hospital.bed_number
            return "Admission confirmed"
    def discharge(self, patient):
        patient.bed_number = None
        self.patients.remove(patient)
                    
p1 = Patient("Todd", "Gluten")
p2 = Patient("Brittany", "Gluten, Soy, Dairy, Sesame, Mushroom, Almond")
p3 = Patient("Connie", "Sulfa")

h1 = Hospital("Mercy General",3)
h1.admit(p1)
h1.admit(p2)
h1.admit(p3)
print h1.admit(p1)

print h1.patients

h1.discharge(p1)

print h1.patients
print p1.bed_num
print p2.bed_num