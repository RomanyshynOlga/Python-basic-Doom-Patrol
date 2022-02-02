from abc import ABC, abstractmethod

stages = {0: 'None', 1: 'Flowering', 2: 'Green', 3: 'Red'}


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests

    def show_the_garden(self):
        print(f"I have {self.vegetables} and {self.fruits} and {self.pests}")


class Vegetables(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Fruits(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Tomato(Vegetables):
    def __init__(self, tomatoes_index, vegetable_type):
        self.tomatoes_index = tomatoes_index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        return self.state == 3

    def grow_info(self):
        print(f'{self.vegetable_type} - {self.tomatoes_index}: {stages[self.state]}')

    def get_vegetables_state(self):
        return self.state


class TomatoBush:
    def __init__(self, number_of_tomatos, number_of_pests):
        self.all_tomatoes = [Tomato('Cherry', index) for index in range(number_of_tomatos)]
        self.all_pests = [Pests(index, 'Vegetables', self.all_tomatoes)
                          for index in range(number_of_pests)]

    def grow_all(self):
        for tomato in self.all_tomatoes:
            tomato.grow()

    def is_ripe_all(self):
        return all([tomato.is_ripe() for tomato in self.all_tomatoes])

    def harvest(self):
        self.all_tomatoes = []

    def is_ripe_for_pests(self):
        return any([tomato.get_vegetables_state() > 1 for tomato in self.all_tomatoess])

    def eaten_by_pests(self):
        self.all_tomatoes = []


class Apple(Fruits):
    def __init__(self, apple_index, fruit_type):
        self.apple_index = apple_index
        self.fruit_type = fruit_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        return self.state == 3

    def grow_info(self):
        print(f'{self.fruit_type} - {self.apple_index}: {stages[self.state]}')

    def get_apples_state(self):
        return self.state


class AppleTree:
    def __init__(self, number_of_apple, number_of_pests):
        self.all_apples = [Apple('White', index) for index in range(number_of_apple)]
        self.all_pests = [Pests(index, 'Fruits', self.all_apples) for index in range(number_of_pests)]

    def grow_all(self):
        for apple in self.all_apples:
            apple.grow()

    def is_ripe_all(self):
        return all([apple.is_ripe() for apple in self.all_apples])

    def harvest(self):
        self.all_apples = []

    def is_ripe_for_pests(self):
        return any([apple.get_apples_state() > 1 for apple in self.all_apples])

    def eaten_by_pests(self):
        self.all_apples = []


class Gardener:
    def __init__(self, name, plants_list, save_trees):
        self.save_trees = save_trees
        self.name = name
        self.plants_list = plants_list

    def take_care(self):
        print("watering the plants")
        for plant in self.plants_list:
            plant.grow_all()

    def harvest(self):
        for plant in self.plants_list:
            if plant.is_ripe_all:
                print('Harvesting...')
                plant.harvest()
            else:
                print("It's not ready for harvest")

    def destruction_pests(self, pests_type):
        for i in range(len(self.pests_list)):
            for j in range(len(self.pests_list[i])):
                if self.pests_list[i][j].pest_type == pests_type:
                    self.pests_list[i][j].time_to_die()
                    self.pests_list[i][j] = ""
                    self.save_trees[pests_type] = True

        for i in self.save_trees.keys():
            if self.save_trees[i]:
                print(f"{i} pests are dead!")


class Pests:
    def __init__(self, pests_type, pests_quantity, plants_list):
        self.pests_type = pests_type
        self.pests_quantity = pests_quantity
        self.plants_list = plants_list

    def eat_plants(self):
        for plant in self.plants_list:
            if plant.is_ripe_for_pests():
                plant.harvest()

    def time_to_die(self):
        del self



apple_tree = AppleTree(3, 2)
tomato_bush = TomatoBush(4, 1)
print(tomato_bush.all_tomatoes)
print(apple_tree.all_apples)
gardener = ('Igor',[tomato_bush, apple_tree])
print(gardener)
print(tomato_bush.all_tomatoes)