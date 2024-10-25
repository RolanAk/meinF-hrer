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
        return self.health_points * 2

    def __str__(self):
         return f"{self.nickname} {self.superpower} {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

Hero = Superhero('Tony Stark', 'Iron man','rich',100,'I am Iron man')

Hero.sayname()
print(Hero)
print(Hero.nhealth_points())
print(len(Hero.catchphrase))
print('\n')

class Superhero1(Superhero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def nhealth_points(self):
        return self.health_points ** 2
        self.fly = True

    def phrase(self):
        print('True in the True_phrase')


nHero1 = Superhero1('steve rogers','captainAmerica',
                    'super soldier',100, 'I can do this all day', 100)


print(nHero1.nhealth_points())
nHero1.phrase()
print('\n')



class Superhero2(Superhero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def nhealth_points(self):
        return self.health_points ** 2
        self.fly = True

    def phrase(self):
        print('True in the True_phrase')

nHero2 = Superhero2('Bruce banner', 'hulk',
                    'radioactivePower', 100, 'hulk smash', 100)

print(nHero2.nhealth_points())
nHero2.phrase()
print('\n')



class villain(Superhero1):

    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, crit):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.crit = crit


    def gen_x(self):
        ...

    def crit1(self):
        return self.damage ** 2

    def __str__(self):
        return f"{Superhero1.__str__(self)} crit: {self.damage}"


villain1 = villain('Johann Shmidt', 'red skull', 'warp',
                   100, 'Cut off one head, two more shall take its place', 100,100)


