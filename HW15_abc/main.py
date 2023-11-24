from abc import ABC, abstractmethod
from typing import Type


class Car(ABC):

    @staticmethod
    def ride():
        return 'машина едет'

    @abstractmethod
    def accelerate(self, seconds):
        pass

    @abstractmethod
    def fly(self):
        pass


class Airplane(ABC):
    @staticmethod
    def fly():
        return 'самолёт летит'

    @abstractmethod
    def accelerate(self, seconds):
        pass


class Lada(Car):
    def accelerate(self, sec):
        return f'Данная машина разгоняется до 100 км/ч за {sec} секунд'

    def fly(self):
        return 'Данная машина может взлететь'


class BMW(Car):
    def accelerate(self, sec):
        return f'Данная машина разгоняется до 100 км/ч за {sec} секунд'

    def fly(self):
        return 'Данная машина может взлететь'


class Ferrari(Car):
    def accelerate(self, sec):
        return f'Данная машина разгоняется до 100 км/ч за {sec} секунд'

    def fly(self):
        return 'Данная машина может взлететь'


class Tu_123(Airplane):
    def accelerate(self, sec):
        return f'Данная машина разгоняется до 100 км/ч за {sec} секунд'


class Bs_ff(Airplane):
    def accelerate(self, sec):
        return f'Данная машина разгоняется до 100 км/ч за {sec} секунд'


# Машины
lada_granta = Lada()
bmw_f10 = BMW()
ferrari_italia = Ferrari()

# Самолёты
tu_123 = Tu_123()
bs_ff = Bs_ff()


def main():
    lada_granta.ride()
    bmw_f10.ride()
    bmw_f10.accelerate(5.2)
    bmw_f10.fly()
    ferrari_italia.accelerate(3.2)
    ferrari_italia.fly()
    tu_123.fly()
    bs_ff.accelerate(5)

    exclusive = [lada_granta, bmw_f10, ferrari_italia, tu_123, bs_ff]

    for i in exclusive:
        print(i.fly())


if __name__ == '__main__':
    main()
