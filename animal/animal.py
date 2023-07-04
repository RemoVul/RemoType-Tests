class Animal:
    weight = 50
    hair = "black"
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.name +  "is eating."

    def drink(self):
        return self.name +  "is drinking."
    
    def get_name(self):
        return self.name

Animal().weight = "Ahmed"
Animal().hair = 50
