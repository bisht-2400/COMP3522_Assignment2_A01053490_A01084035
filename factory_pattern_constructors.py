from abc import ABC

from toys import DollHouse, RCSpider, RobotBunny, Toy
from stuffed_animals import Reindeer, DancingSkeleton, StuffedAnimal, EasterBunny
from candy import CandyCane, CremeEgg, PumpkinCaramelToffee, Candy
import abc


class InventoryFactory(abc.ABC):
    @abc.abstractmethod
    def create_toy(self) -> Toy:
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self) -> StuffedAnimal:
        pass

    @abc.abstractmethod
    def create_candy(self) -> Candy:
        pass


class HalloweenInventoryFactory(InventoryFactory):

    def create_stuffed_animal(self) -> DancingSkeleton:
        pass

    def create_candy(self) -> PumpkinCaramelToffee:
        pass

    def create_toy(self) -> RCSpider:
        pass


class ChristmasInventoryFactory(InventoryFactory):
    def create_stuffed_animal(self) -> Reindeer:
        pass

    def create_candy(self) -> CandyCane:
        pass

    def create_toy(self) -> DollHouse:
        pass


class EasterInventoryFactory(InventoryFactory):
    def create_stuffed_animal(self) -> EasterBunny:
        pass

    def create_candy(self) -> CremeEgg:
        pass

    def create_toy(self) -> RobotBunny:
        pass
