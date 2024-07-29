class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __get_seconds(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или тип Clock")
        if isinstance(other, Clock):
            return other.seconds
        return other

    def __add__(self, other):
        sc = self.__get_seconds(other)
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        sc = self.__get_seconds(other)
        self.seconds += sc
        return self

    def __sub__(self, other):
        sc = self.__get_seconds(other)
        return Clock(self.seconds - sc)

    def __isub__(self, other):
        sc = self.__get_seconds(other)
        self.seconds -= sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c1 -= 13
print(c1.get_time())
