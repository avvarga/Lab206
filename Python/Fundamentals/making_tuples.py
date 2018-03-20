# making tuples out of a dictionary
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def making_duples(dict):
    y=[]
    x=[]
    z=[]
    for key,value in dict.items(): # break the dictionary into 2 lists
        y.append(key)
        x.append(value)
    z=zip(y,x) # puts both lists together
    print z
making_duples(my_dict)