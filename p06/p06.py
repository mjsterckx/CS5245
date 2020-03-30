
class Animal:
    def __init__(self, name=None):
        self._name = name
        self._hunger_level = 0

    def set_hunger_level(self, hunger_level):
        self._hunger_level = max(0, min(10, hunger_level))

    def get_hunger_level(self):
        return self._hunger_level

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def sleep(self):
        print('sleeping...')
        self.set_hunger_level(10)

    def roam(self):
        print('animal moves...')
        self.set_hunger_level(self.get_hunger_level() + 1)
        
    def make_noise(self):
        raise NotImplementedError('make_noise not implemented')

    def eat(self):
        raise NotImplementedError('eat not implemented')


class Pet:
    def play(self):
        raise NotImplementedError('play not implemented')
    
    def be_friendly(self):
        raise NotImplementedError('be_friendly not implemented')


class Canine(Animal):
    def roam(self):
        print('canines like to roam in packs...')
        self.set_hunger_level(self.get_hunger_level() + 1)


class Feline(Animal):
    def roam(self):
        print('felines like to roam alone...')
        self.set_hunger_level(self.get_hunger_level() + 1)


class Wolf(Canine):
    def make_noise(self):
        print('growl...')

    def eat(self):
        print('rip with teeth...')
        self.set_hunger_level(self.get_hunger_level() - 2)
        

class Cat(Feline, Pet):
    def make_noise(self):
        print('meow...')

    def eat(self):
        print('pick...')
        self.set_hunger_level(self.get_hunger_level() - 3)
    
    def play(self):
        print('frolic...')

    def be_friendly(self):
        print('purr...')


class Dog(Canine, Pet):
    def make_noise(self):
        print('bark...')

    def eat(self):
        print('slop...')
        self.set_hunger_level(self.get_hunger_level() - 3)

    def play(self):
        print('scamper...')

    def be_friendly(self):
        print('sniff...')


class Lion(Feline):
    def make_noise(self):
        print('roar...')

    def eat(self):
        print('rip with teeth...')
        self.set_hunger_level(self.get_hunger_level() - 2)


class Hippo(Animal):
    def make_noise(self):
        print('blub...')

    def eat(self):
        print('slurp...')
        self.set_hunger_level(self.get_hunger_level() - 1)


class Zoo:
    def __init__(self, name=None):
        self._name = name
        self._zoo_animals = []

    def add_animal(self, animal):
        self._zoo_animals.append(animal)

    def test_animals(self):
        print('zoo name: ' + self._name)
        print('number of animals: ' + str(len(self._zoo_animals)))
        for animal in self._zoo_animals:
            print('name: ' + animal.get_name())
            animal.sleep()
            animal.make_noise()
            while animal.get_hunger_level() > 0:
                animal.eat()
            print('hunger_level: ' + str(animal.get_hunger_level()))
            animal.roam()
            if isinstance(animal, Pet):
                animal.play()
                animal.be_friendly()
            print('-------------------')


def main():
    zoo = Zoo('zoo')
    zoo.add_animal(Dog('dan the dog'))
    zoo.add_animal(Wolf('wanda the wolf'))
    zoo.add_animal(Cat('clyde cat'))
    zoo.add_animal(Hippo('harry the hippo'))
    zoo.add_animal(Lion('lily the lion'))
    zoo.test_animals()


if __name__ == '__main__':
    main()
