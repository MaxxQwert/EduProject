from abc import ABCMeta, abstractmethod


class VehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def buzz(self):
        raise NotImplementedError

    @abstractmethod
    def start_engine(self, status: bool) -> bool:
        raise NotImplementedError

    @abstractmethod
    def refuel(self, val: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def draw(self, val: int) -> bool:
        raise NotImplementedError