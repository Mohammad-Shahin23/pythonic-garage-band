class Musician:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    
    def get_instrument(self):
        pass
    
    def play_solo(self):
        pass


class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []
    
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        self.instances.append(self)
    
    def __repr__(self):
        return f"Band instance. Name = {self.name}"
    
    def __str__(self):
        return f"{self.name} band"
    
    def play_solos(self):
        return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
        return cls.instances
    
if __name__ == "__main__":

    jimi = Guitarist("Jimi ")
    stan = Bassist("stan")
    ginger = Drummer("Ginger Baker")

    # Creating a band with the musicians
    band = Band("The Experience", [jimi, stan, ginger])

    # Printing the band name and its members
    print(band)
    for member in band.members:
        print(member)