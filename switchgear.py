from abc import ABC, abstractmethod


class Switchgear(ABC):
    @abstractmethod
    def __init__(self, current, percent=.2):
        assert (0 < percent <= 1), "Folga do disjuntor must be greater than 0 until 1"

    @abstractmethod
    def calculate(self):
        pass


class SwitchgearAdapter(Switchgear):
    pass

class CircuitBreaker(Switchgear):
    def __init__(self, current, percent=.2):
        super().__init__(current, percent)
        self.table = [10, 16, 20, 25, 32, 40, 63, 70, 80, 100, 125, 160, 175, 200, 225, 250, 400, 630, 800, 1200]
        self.current = current * (1 + percent)

    def calculate(self):
        for x in self.table:
            if x >= self.current:
                return x
        return 0


class Fuse(Switchgear):
    def __init__(self, current, percent=.2):
        super().__init__(current, percent)

    def calculate(self):
        for x in self.table:
            if x >= self.current:
                return x
        return 0