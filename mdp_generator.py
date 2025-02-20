import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
carrac_spec = ['&','#','@','+','-','_','?','!','%']
list_concat= alphabet+ carrac_spec

class mdp_genr :
    def __init__(self):
        self.nb_lettre = random.randint(8,10)
        self.nb_car_spe = random.randint(2,4)
        self.mdp = ""

    def generate(self):
        j = 0
        for i in range(0,self.nb_lettre):
            char = random.choice(list_concat)
            if char in carrac_spec:
                j+=1
                if j != 2:
                    self.mdp+= char
            else:
                self.mdp+= char
    


