from abc import ABC, abstractmethod
from candy import CandyCane
from candy import PumpkinCaramelToffee
from candy import CremeEgg

from stuffed_animal import Reindeer
from stuffed_animal import DancingSkeleton
from stuffed_animal import EasterBunny

from toy import SantaWorkshop
from toy import RCSpider
from toy import RobotBunny


class StoreItemFactory(ABC):
    @abstractmethod
    def create_toy(self):
        pass

    @abstractmethod
    def create_stuff_animal(self):
        pass

    @abstractmethod
    def create_candy(self):
        pass


class ChristmasItemFactory(StoreItemFactory):

    def create_candy(self, **kwargs):
        return CandyCane(**kwargs)

    def create_stuff_animal(self, **kwargs):
        return Reindeer(**kwargs)

    def create_toy(self, **kwargs):
        return SantaWorkshop(**kwargs)


class HalloweenItemFactory(StoreItemFactory):

    def create_candy(self, **kwargs):
        return PumpkinCaramelToffee(**kwargs)

    def create_stuff_animal(self, **kwargs):
        return DancingSkeleton(**kwargs)

    def create_toy(self, **kwargs):
        return RCSpider(**kwargs)


class EasterItemFactory(StoreItemFactory):

    def create_candy(self, **kwargs):
        return CremeEgg(**kwargs)

    def create_stuff_animal(self, **kwargs):
        return EasterBunny(**kwargs)

    def create_toy(self, **kwargs):
        return RobotBunny(**kwargs)
