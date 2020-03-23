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
    """
    Factory for the StoreItem.
    """
    @abstractmethod
    def create_toy(self):
        """
        Creates Items: Toy
        :return:
        """
        pass

    @abstractmethod
    def create_stuff_animal(self):
        """
        Creates Items: Stuffed Animals
        :return:
        """
        pass

    @abstractmethod
    def create_candy(self):
        """
        Creates Items: Candy
        :return:
        """
        pass


class ChristmasItemFactory(StoreItemFactory):
    """
    Holiday: Christmas Factory class.
    """

    def create_candy(self, **kwargs):
        """
        Creates the candy.
        :param kwargs: Attributes to initialize the candy.
        :return: CandyCane Object.
        """
        return CandyCane(**kwargs)

    def create_stuff_animal(self, **kwargs):
        """
        Creates the Stuffed Animal.
        :param kwargs: Attributes to initialize the Stuffed Animal.
        :return: Reindeer Object.
        """
        return Reindeer(**kwargs)

    def create_toy(self, **kwargs):
        """
        Creates the Toy.
        :param kwargs: Attributes to initialize the toy.
        :return: SantaWorkshop Object.
        """
        return SantaWorkshop(**kwargs)


class HalloweenItemFactory(StoreItemFactory):
    """
    Holiday: Halloween Factory class.
    """

    def create_candy(self, **kwargs):
        """
        Creates the candy.
        :param kwargs: Attributes to initialize the candy.
        :return: PumpkinCaramelToffee Object.
        """
        return PumpkinCaramelToffee(**kwargs)

    def create_stuff_animal(self, **kwargs):
        """
        Creates the Stuffed Animal.
        :param kwargs: Attributes to initialize the Stuffed Animal.
        :return: DancingSkeleton Object.
        """
        return DancingSkeleton(**kwargs)

    def create_toy(self, **kwargs):
        """
        Creates the Toy.
        :param kwargs: Attributes to initialize the toy.
        :return: RCSpider Object.
        """
        return RCSpider(**kwargs)


class EasterItemFactory(StoreItemFactory):
    """
    Holiday: Easter Factory class.
    """

    def create_candy(self, **kwargs):
        """
        Creates the candy.
        :param kwargs: Attributes to initialize the candy.
        :return: CremeEgg Object.
        """
        return CremeEgg(**kwargs)

    def create_stuff_animal(self, **kwargs):
        """
        Creates the Stuffed Animal.
        :param kwargs: Attributes to initialize the Stuffed Animal.
        :return: EasterBunny Object.
        """
        return EasterBunny(**kwargs)

    def create_toy(self, **kwargs):
        """
        Creates the Toy.
        :param kwargs: Attributes to initialize the toy.
        :return: RobotBunny Object.
        """
        return RobotBunny(**kwargs)
