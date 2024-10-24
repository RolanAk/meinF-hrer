class Superhero:

    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):

        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def sayname(self):
        print(self.name)

    def nhealth_points(self):
        return int(self.health_points) * 2

    def __str__(self):
         return f"{self.nickname} {self.superpower} {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

Hero = Superhero('Tony Stark', 'Iron man','rich','100','I am Iron man')

Hero.sayname()
print(Hero)
print(Hero.nhealth_points())
print(len(Hero.catchphrase))