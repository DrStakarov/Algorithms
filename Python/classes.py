class Hello:
    # attributes
    name = "Nick"
    hairColor = "black"
    age = "[redacted]"
    
    # methods
    def sayHello(self):
        print(f"The guys name is {self.name}")
        print(f"{self.name} says hello!")
        
    def stats(self):
        print(f"The guys age is {self.age} and hair color is {self.hairColor}")
        
objectSpeaker = Hello()

objectSpeaker.sayHello()
objectSpeaker.stats()